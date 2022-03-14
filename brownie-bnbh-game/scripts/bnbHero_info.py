#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import time
from brownie import accounts, interface, network


def main():
    #accu = accounts.load('titan_bsc_arbs_account')
    bnbHero_token_address = '0xD25631648E3Ad4863332319E8E0d6f2A8EC6f267'
    bnbHero_address = '0xde9fFb228C1789FEf3F08014498F2b16c57db855'
    bnbHero_character_address = '0x6DA72F24c56197Dcf6B8920baCb183F6ccca8b01'
    network_name = network.show_active()
    if network_name != 'bsc-main':
        print('network error')
        return
    bnbHero = interface.IBnbHero(bnbHero_address)
    hero_character = interface.ICharacter(bnbHero_character_address)
    # 查询关卡奖励和胜率
    for enemyId in range(7):
        base_reward = hero_character.baseBNBRewards.call(enemyId)
        base_chance = hero_character.baseChances.call(enemyId)
        cost_hp = hero_character.requiredHps.call(enemyId)
        print('enemyId=', enemyId, 'base_reward=', base_reward / 10**18, 'BNB',
              'base_chance=', base_chance / 1000, 'cost_hp=', cost_hp)

    # 查询claim reward需要的费用
    addresses = [
        '0x6e5739F868875f32eD1f662429af922cda4667ED',
        '0x0d735CDe1F52AE7A2BeBe29d6fA17707Bc688587',
        '0xbab78DFF575556F18764347Db7032f43663aB4Bc',
        '0xE45Be2Aae3E2215FBAe316eBdAE722059876Ec7c',
        '0xD1d9d5fFdd7c35A337368561112686fE17538a78',
        '0x62d4a51Cb037897A5064AF9aC27e4414D024f8A0',
        '0x0B54A3432C7AD96251637cD2BEB3FC551F35E54d',
        '0xC545433AFd094777bEE8E0a525927B1E64DDc484',
        '0x4e18E9BAC0D434aD54514CC520fdd136A2Aa3277',
        '0x730e4D656D8D5C78F33bac71C38E5544a53BD764',
        '0xdafed74177cc2ca5dE6E768586B65EA67579da22'
    ]

    count = 0
    for accu in addresses:
        heroCount = hero_character.balanceOf(accu)
        heroIdxes = []
        for heroIdx in range(heroCount):
            count += 1
            heroId = hero_character.tokenOfOwnerByIndex(accu, heroIdx)
            heroIdxes.append(heroId)
            res = hero_character.getHero(heroId, True)
            # 11584的 (18, 4, 9700, 1120, 720, 720)
            current_level = int(res[2] / 1000)
            # print(res)
            amount = bnbHero.getPriceToUnlockLevel(heroId)
            print('heroCount:', count, 'heroId:', heroId, 'from level',
                  current_level, 'to level', current_level + 1, 'cost:',
                  amount / 10**18, 'BNBH')

    ts = time.time()
    totalClaimReward = 0
    addressIdx = 1
    for add in addresses:
        lockTime = bnbHero.unLockTime(add)
        reward = bnbHero.balances(add)
        totalClaimReward += reward
        timespan = ts - lockTime
        taxFee = 20 - timespan * 2 / 86400
        print('addressIdx:', addressIdx, 'address:', add, 'bnbReward:',
              reward / 10**18, 'taxFee:', taxFee)
        addressIdx += 1
    print('totalBnbReward:', totalClaimReward / 10**18, 'BNB')
