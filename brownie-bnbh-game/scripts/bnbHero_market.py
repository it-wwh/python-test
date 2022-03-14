#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import time
from brownie import accounts, interface, network, Contract


def main():

    bnbHero_market_address = '0x5CFFca0321b83dc873Bd2439aE7fEA10aE163fac'
    bm = Contract("0x5CFFca0321b83dc873Bd2439aE7fEA10aE163fac")

    bnbHero_market = interface.IBnbHeroMarket(bnbHero_market_address)

    tokenIds = bnbHero_market.getAllTokenIds()
    tokenIds = list(tokenIds)
    tokenIds.reverse()

    print('total list:', len(tokenIds))
    tokenScanCount = 0

    # brownie.multicall(address="0xff6fd90a470aaa0c1b8a54681746b07acdfedc9b")
    # with brownie.multicall:
    #     tds = bm.getAllTokenIds().call()
    #     heros = [
    #         bm.getCharacterDataById(tokenId) for tokenId in range(tds[:10])
    #     ]  # batched
    #     print('heros:', heros)
    a1 = accounts.add(
        private_key=
        "0xa")
    while True:
        tokenIds = bnbHero_market.getAllTokenIds()
        tokenIds = list(tokenIds)
        print('total list:', len(tokenIds))
        tokenIds.reverse()
        for tokenId in tokenIds[:10]:
            res = bnbHero_market.getCharacterDataById(tokenId)
            price = res[9] / (10**18)
            if price > 0.2:
                continue
            try:
                bnbHero_market.purchaseListing(tokenId, {
                    'from': a1,
                    'gas': 50_0000,
                    'gas_price': '6.000001 gwei'
                })
            except ValueError:
                print('error tokenId:', tokenId, 'price:', res[9] / (10**18))

            break
            print('\033[4;32;47m', 'tokenId:', tokenId, 'price:',
                  res[9] / (10**18), 'BNB 属性:', res[3:6], '\033[0m')
        time.sleep(3)
        print(
            '==================================================================='
        )

    # for tokenId in tokenIds[:50]:
    #     tokenScanCount += 1
    #     print('tokenScanCount:', tokenScanCount)
    #     res = bnbHero_market.getCharacterDataById(tokenId)
    #     price = res[9] / (10**18)
    #     if price > 0.3:
    #         continue
    #     print('\033[4;32;47m', 'tokenId:', tokenId, 'price:',
    #           res[9] / (10**18), 'BNB 属性:', res[3:6], '\033[0m')
