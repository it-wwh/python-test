import click
from brownie import *
import os

os.environ["http_proxy"] = "http://127.0.0.1:10809"
os.environ["https_proxy"] = "http://127.0.0.1:10809"


#  brownie run --network rinkeby ./scripts/deploy.py
def main():
    print(f"You are using the '{network.show_active()}' network")
    account = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
    print(f"You are using: 'account' [{account.address}]")
    # (string memory name, string memory symbol, uint8  decimals, uint256  initial_supply
    account.deploy(SimpleToken, 'Simple Token', "ST", 18, (10 ** 9), publish_source=True)
