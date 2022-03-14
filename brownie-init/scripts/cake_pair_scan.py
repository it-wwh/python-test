#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import time

import click
from brownie import accounts, interface, network


# brownie run --network bsc-main ./scripts/cake_pair_scan.py
def main():
    print(f"You are using the '{network.show_active()}' network")
    account = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
    # account = accounts.add(private_key="0xaaa")
    print(f"You are using: 'account' [{account.address}]")

    path = []
    deadline = time.time() + 600 * 30
    # 10 gwei
    gas_price = int(10 * (10 ** 9))
    # buy count
    amount_eth_desired = int(1 * (10 ** 18))
    # pool limit
    bnb_liquidity = int(300 * (10 ** 18))
    usdt_liquidity = int(200000 * (10 ** 18))

    # bsc-main 合约地址
    # LOA: 0x94b69263FCA20119Ae817b6f783Fc0F13B02ad50
    token_address = '0x94b69263FCA20119Ae817b6f783Fc0F13B02ad50'

    pancake_router_address = '0x10ED43C718714eb63d5aA57B78B54704E256024E'
    pancake_factory_address = '0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73'
    wbnb_address = '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c'
    busd_address = '0xe9e7cea3dedca5984780bafc599bd69add087d56'
    usdt_address = '0x55d398326f99059ff775485246999027b3197955'

    router = interface.IPancakeRouter(pancake_router_address)
    factory = interface.IPancakeFactory(pancake_factory_address)

    def getPairAddress(address1, address2):
        pair = factory.getPair(address1, address2)
        if pair == '0x0000000000000000000000000000000000000000':
            return False, pair
        return True, pair

    # 组装 path
    while True:
        # check wbnb-token exist
        exist, pair_address = getPairAddress(token_address, wbnb_address)
        if exist:
            path = [wbnb_address, token_address]
            erc20 = interface.IERC20(wbnb_address)
            wbnb_balance = erc20.balanceOf(pair_address)
            print('\033[4;32;47m', 'wbnb-token pair create pair_address:', pair_address, " >>> ",
                  wbnb_balance / (10 ** 18), '\033[0m')
            if wbnb_balance > bnb_liquidity:
                break
            else:
                print('\033[4;31;47m', 'wbnb not enough >>> ', bnb_liquidity / (10 ** 18), '\033[0m')
        # check busd-token exist
        exist, pair_address = getPairAddress(token_address, busd_address)
        if exist:
            path = [wbnb_address, busd_address, token_address]
            erc20 = interface.IERC20(busd_address)
            busd_balance = erc20.balanceOf(pair_address)
            print('\033[4;32;47m', 'busd-token pair create pair_address:', pair_address, " >>> ",
                  busd_balance / (10 ** 18), '\033[0m')
            if busd_balance > usdt_liquidity:
                break
            else:
                print('\033[4;31;47m', 'busd not enough >>> ', usdt_liquidity / (10 ** 18), '\033[0m')
        # check usdt-token exist
        exist, pair_address = getPairAddress(token_address, usdt_address)
        if exist:
            path = [wbnb_address, usdt_address, token_address]
            erc20 = interface.IERC20(usdt_address)
            usdt_balance = erc20.balanceOf(pair_address)
            print('\033[4;32;47m', 'usdt-token pair create pair_address:', pair_address, " >>> ",
                  usdt_balance / (10 ** 18), '\033[0m')
            if usdt_balance > usdt_liquidity:
                break
            else:
                print('\033[4;31;47m', 'usdt not enough >>> ', usdt_liquidity / (10 ** 18), '\033[0m')

        print('now:', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
              'token lp not create or liquidity not enough !')
        # sleep for 3 second
        time.sleep(3)

    print('path', path, 'balance', account.balance())
    # 下单
    while True:
        try:
            router.swapExactETHForTokens(
                1, path, account, deadline, {
                    'from': account,
                    'gas': 30_0000,
                    'value': amount_eth_desired,
                    'gas_price': gas_price
                })
            break
        except Exception as exception:
            print("the transaction fails, continue to send the transaction:", exception)
            time.sleep(3)
