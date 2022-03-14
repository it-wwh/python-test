// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// # bsc-main合约地址
// pancake_router_address = '0x10ED43C718714eb63d5aA57B78B54704E256024E'
// pancake_factory_address = '0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73'
// wbnb_address = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'
// busd_address = '0xe9e7cea3dedca5984780bafc599bd69add087d56'
// usdt_address = '0x55d398326f99059ff775485246999027b3197955'
contract SwapRouterRush {
    address public owner;
    address public swapFactory;
    address public WETH;
    IPancakeRouter public cakeRouter;
    address[] public path;
    address public tokenA;
    address public tokenB;
    uint256 public priceBase = 1 gwei;
    PriceLimit public priceLimit;

    struct PriceLimit {
        uint256 min; // already multipy priceBase
        uint256 max;
    }

    event Done(uint256 price, uint256 pay, uint256 left);

    constructor(address _cakeRouter) {
        owner = msg.sender;
        cakeRouter = IPancakeRouter(_cakeRouter);
        swapFactory = cakeRouter.factory();
        WETH = cakeRouter.WETH();
    }

    receive() external payable {}

    function swapExactETHForToken() public {
        address _pair = IPancakeFactory(swapFactory).getPair(tokenA, tokenB);
        require(_pair != address(0), "no pair");
        require(address(this).balance > 0, "no balance");

        uint256 _pay = address(this).balance;
        uint256[] memory amountsOut = cakeRouter.getAmountsOut(_pay, path);
        uint256 _price = (amountsOut[amountsOut.length - 2] * priceBase) / amountsOut[amountsOut.length - 1];
        if (_price >= priceLimit.max) {
            _pay = 0;
        } else if (_price > priceLimit.min) {
            // 价格在最小与最大值之间，按价格比例购入
            _pay = (_pay * (priceLimit.max - _price)) / (priceLimit.max - priceLimit.min);
            if (_pay > address(this).balance) {
                _pay = address(this).balance;
            }
        }
        if (_pay > 0) {
            cakeRouter.swapExactETHForTokens{value: _pay}(1, path, owner, block.timestamp);
        }
        uint256 _left = address(this).balance;
        TransferHelper.safeTransferETH(owner, _left);
        emit Done(_price, _pay, _left);
    }

    function setRouter(address _cakeRouter) public {
        require(msg.sender == owner, "not owner");
        cakeRouter = IPancakeRouter(_cakeRouter);
        swapFactory = cakeRouter.factory();
    }

    function setParams(
        address[] memory _path,
        uint256 _minPrice,
        uint256 _maxPrice
    ) public {
        require(msg.sender == owner, "not owner");
        require(_path[0] == WETH, "path[0] must be WETH");
        tokenA = _path[_path.length - 2];
        tokenB = _path[_path.length - 1];
        path = _path;
        priceLimit = PriceLimit(_minPrice, _maxPrice);
    }

    function withdraw(uint256 amount) public {
        require(msg.sender == owner, "not owner");
        TransferHelper.safeTransferETH(owner, amount);
    }
}

library TransferHelper {
    function safeTransferETH(address to, uint256 value) internal {
        (bool success, ) = to.call{value: value}(new bytes(0));
        require(success, "TransferHelper: ETH_TRANSFER_FAILED");
    }
}

interface IPancakeRouter {
    function factory() external pure returns (address);

    function WETH() external pure returns (address);

    function swapExactETHForTokens(
        uint256 amountOutMin,
        address[] memory path,
        address to,
        uint256 deadline
    ) external payable;

    function getAmountsOut(uint amountIn, address[] calldata path) external view returns (uint[] memory amounts);
}

interface IPancakeFactory {
    function getPair(address tokenA, address tokenB) external view returns (address pair);
}
