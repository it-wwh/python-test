#!/usr/bin/python
# -*- coding: UTF-8 -*-

import click
from brownie import *


#  brownie run --network bsc-test ./scripts/deploy.py
def main():
    print(f"You are using the '{network.show_active()}' network")
    account = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
    print(f"You are using: 'account' [{account.address}]")
    # (string memory name, string memory symbol, uint8  decimals, uint256  initial_supply
    account.deploy(SimpleToken, 'Simple Token', "ST", 18, (10 ** 9), publish_source=True)
