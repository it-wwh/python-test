pragma solidity 0.7.0;

interface IPancakeRouter {
    function swapExactETHForTokens(
        uint256 amountOutMin,
        address[] memory path,
        address to,
        uint256 deadline
    ) external payable;
}
