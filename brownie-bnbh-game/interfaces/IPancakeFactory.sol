// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

interface IPancakeFactory {
    function getPair(address _input1, address _input2) external view returns (address);
}
