// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

interface IPancakeRouter {
    function swapExactETHForTokens(
        uint256 amountOutMin,
        address[] memory path,
        address to,
        uint256 deadline
    ) external payable;
}
