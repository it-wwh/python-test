#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import click
from brownie import accounts, network


# brownie run --network bsc-main ./scripts/accounts.py
def main():
    print(f"You are using the '{network.show_active()}' network")
    account = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
    print(f"You are using: 'account' [{account.address}] balance: ", account.balance() / (10 ** 18))
