#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import time
import click
from brownie import accounts, interface


# brownie run --network bsc-main ./scripts/swap.py
def main():
    account = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
    # account = accounts.add(private_key="0xaa")
    print(f"You are using: 'account' [{account.address}]")

    # bnb、busd、usdt
    transaction_type = 'busd'
    # 10 gwei
    gas_price = int(10 * (10 ** 9))
    # buy count
    amount_eth_desired = int(1 * (10 ** 18))
    deadline = time.time() + 600 * 30

    # bsc-main 合约地址
    # LOA: 0x94b69263FCA20119Ae817b6f783Fc0F13B02ad50
    token_address = '0x94b69263FCA20119Ae817b6f783Fc0F13B02ad50'
    pancake_router_address = '0x10ED43C718714eb63d5aA57B78B54704E256024E'
    wbnb_address = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'
    busd_address = '0xe9e7cea3dedca5984780bafc599bd69add087d56'
    usdt_address = '0x55d398326f99059ff775485246999027b3197955'

    # rinkeby 合约地址
    # ST: 0x7260929eb0863d0657c43d338ac5ec90bd74bed9
    # token_address = '0x7260929eb0863d0657c43d338ac5ec90bd74bed9'
    # pancake_router_address = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D'
    # wbnb_address = '0xc778417E063141139Fce010982780140Aa0cD5Ab'
    # busd_address = '0xD9BA894E0097f8cC2BBc9D24D308b98e36dc6D02'
    # usdt_address = '0xD9BA894E0097f8cC2BBc9D24D308b98e36dc6D02'

    router = interface.IPancakeRouter(pancake_router_address)

    path = []
    if transaction_type == 'bnb':
        path = [wbnb_address, token_address]
    if transaction_type == 'busd':
        path = [wbnb_address, busd_address, token_address]
    if transaction_type == 'usdt':
        path = [wbnb_address, usdt_address, token_address]
    print('path', path)

    while True:
        try:
            router.swapExactETHForTokens(
                1, path, account, deadline, {
                    'from': account,
                    'gas': 30_0000,
                    'value': amount_eth_desired,
                    'gas_price': gas_price,
                    'allow_revert': True  # allow trx revert
                })
            break
        except Exception as exception:
            print("the transaction fails, continue to send the transaction:", exception)
            time.sleep(3)
