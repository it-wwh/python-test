#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import time
import click
from brownie import (
    SwapRouterRush,
    Contract,
    network,
    config,
    accounts,
    interface
)


# brownie run --network bsc-main ./scripts/execute_swap.py
def main():
    account = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
    # account = accounts.add(private_key="0xaa")
    chain_name = network.show_active()
    print(f"Deploying to:", chain_name)

    # swap = SwapRouter.at("0x6B8303000723bFF6d6f04Dd5b52Ed05da6f4749D")
    swap = SwapRouterRush.at("0xFEeE3305f9E22537035BC01725d4957aBE0FA9f2")
    nonce = account.nonce
    gas_price = int(35 * (10 ** 9))

    for i in range(600):
        swap.swapExactETHForToken(
            {
                'from': account,
                'gas': 50_0000,
                'gas_price': gas_price,
                'nonce': nonce,
                'required_confs': 0,  # without confirmation
                'allow_revert': True  # allow trx revert
            })
        nonce += 1
        time.sleep(3)
