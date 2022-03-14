#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from brownie import (
    SwapRouter,
    Contract,
    network,
    config,
    accounts,
    interface
)


# brownie run --network bsc-main ./scripts/test.py
def main():
    swap = SwapRouter.at("0x6B8303000723bFF6d6f04Dd5b52Ed05da6f4749D")
    print(swap.owner())
    print(swap.swapFactory())
    print(swap.WETH())
    print(swap.path(0))
    print(swap.path(1))
    print(swap.tokenA())
    print(swap.tokenB())
