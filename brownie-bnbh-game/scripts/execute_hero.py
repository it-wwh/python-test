#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from brownie import accounts, interface, network


def main():
    bnbHero_token_address = '0xD25631648E3Ad4863332319E8E0d6f2A8EC6f267'
    bnbHero_address = '0xde9fFb228C1789FEf3F08014498F2b16c57db855'
    bnbHero_character_address = '0x6DA72F24c56197Dcf6B8920baCb183F6ccca8b01'
    network_name = network.show_active()
    if network_name != 'bsc-main':
        print('network error')
        return
    bnbHero = interface.IBnbHero(bnbHero_address)
    hero_character = interface.ICharacter(bnbHero_character_address)
    bnbHero_token = interface.IERC20(bnbHero_token_address)

    private_keys = [
        # Account 1
        "",
        # Account 2
        ""
    ]

    totalFee = 0
    fee_address = 'Account 1'

    a1 = accounts.add(private_key=private_keys[0])
    before_token_balance = bnbHero_token.balanceOf(a1)

    def fightWithHero(heroId):
        current_hp, hpPerSeconds = hero_character.getHpPoints(heroId, True)
        hpCost = 200
        enemyId = 5
        if heroId in enemy6HeroIds:
            hpCost = 400
            enemyId = 6
        if current_hp < hpCost:
            print('address', accu, 'heroId:', heroId, 'hp not enough to fight')
            return
        # check 是否要升级
        canFight = True
        try:
            bnbHero.fight.call(heroId, enemyId, {'from': accu})
        except ValueError:
            canFight = False

        print('heroId:', heroId, 'enemyId:', enemyId, 'canFight:', canFight)
        # 不能战斗就升级
        if canFight == False:
            before_balance = bnbHero_token.balanceOf(fee_address)
            bnbHero.unLockLevel(heroId, {
                'from': a1,
                'gas': 20_0000,
                'gas_price': '5.000001 gwei'
            })
            end_balance = bnbHero_token.balanceOf(fee_address)
            print('heroId:', heroId, 'level up', 'cost:',
                  (before_balance - end_balance) / 10**18, 'BNBH')

        s_reward = bnbHero.balances(accu)
        bnbHero.fight(heroId, enemyId, {
            'from': accu,
            'gas': 20_0000,
            'gas_price': '5.000001 gwei'
        })
        e_reward = bnbHero.balances(accu)
        fightResult = 'loss'
        reward = 0
        fee = 0.0006
        if s_reward != e_reward:
            fightResult = 'win'
            reward = (e_reward - s_reward) / 10**18
            fee = 0.0007

        print('heroId:', heroId, 'enemyId:', enemyId, 'fightResult:',
              fightResult, 'reward:', reward, 'fee:', fee)
        # 查询是否要升级
        # try:
        #     bnbHero.unLockLevel.call(heroId)
        #     bnbHero.unLockLevel(heroId, {'from': a1})
        #     print('heroId:', heroId, 'level up')
        # except ValueError:
        #     print('heroId:', heroId, 'not to level up')

        fightWithHero(heroId)

    # 英雄升级
    # levelUpHero = []

    totalReward = 0
    accountIdx = 1
    for key in private_keys:
        accu = accounts.add(private_key=key)
        print('account', accountIdx)
        start_balance = accu.balance()
        start_reward = bnbHero.balances(accu)
        heroCount = hero_character.balanceOf(accu)
        heroIdxes = []
        for heroIdx in range(heroCount):
            heroId = hero_character.tokenOfOwnerByIndex(accu, heroIdx)
            heroIdxes.append(heroId)

        print('address', accu, "has hero:", heroCount, 'heroIdxes:', heroIdxes)
        #打副本
        # 打最后一关小怪的hero
        enemy5HeroIds = []
        # 打boss的hero
        enemy6HeroIds = [10719, 79295, 132810]

        for heroId in heroIdxes:
            fightWithHero(heroId)

        end_reward = bnbHero.balances(accu)
        end_balance = accu.balance()
        address_reward = (end_reward - start_reward) / 10**18
        totalReward += address_reward
        print('\033[4;32;47m', 'accountIdx:', accountIdx, 'address:', accu,
              'fight end 本次打怪累计奖励:', address_reward, 'fee',
              (start_balance - end_balance) / 10**18, '\033[0m')
        accountIdx += 1

    end_token_balance = bnbHero_token.balanceOf(a1)
    print('totalReward:', totalReward, 'cost Token:',
          (before_token_balance - end_token_balance) / 10**18, 'BNB totalFee:',
          totalFee, 'BNB')
