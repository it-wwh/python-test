#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import click
from brownie import *
import os

os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"


# brownie run --network bsc-test ./scripts/deploy.py
def main():
    print(f"You are using the '{network.show_active()}' network")
    account = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
    print(f"You are using: 'account' [{account.address}]")
    account.deploy(TestERC1155, publish_source=True)
