#!/usr/bin/python3

from brownie import Token, accounts


def main():
    # 第一种：先通过 export-key-as-json.js 生成私钥json
    # account.deploy(rarity, "0x2A8E92800C7B739473Ef77c94cA87D9b7219C3d0", publish_source=True)
    val = input("Enter your account: ")
    account = accounts.load(val)
    return Token.deploy("Test Token", "TST", 18, 1e21, {'from': account})
    # 第二种：先进入环境，导入账户
    # return Token.deploy("Test Token", "TST", 18, 1e21, {'from': accounts[0]})
