import json

import requests

headers = {
    'authority': 'www.cryptogladiator.org',
    'origin': 'https://www.cryptogladiator.cc',
    'referer': 'https://www.cryptogladiator.cc/',
    'token': 'f47d1a71b4ecd0905ac06f93dee941ffut',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Content-Type': 'application/json',
}


# 升级
def stages(_count: str):
    data = '{"StagesReqMsg":{"name":"StagesReqMsg","owner_id":3272,"dr_id":' + _count + ',"role_id":["1817","1894","1895","1891","1892"]}}'
    response = requests.post('https://www.cryptogladiator.org/rpgGame/public/index.php/game/Rpg/gameEntrance',
                             headers=headers, data=data)
    pass


# 获得钻石
def reward(_count: str):
    data = '{"TerritoryRewardReqMsg":{"name":"TerritoryRewardReqMsg","owner_id":3272,"ter_id":' + _count + '}}'
    response = requests.post('https://www.cryptogladiator.org/rpgGame/public/index.php/game/Rpg/gameEntrance',
                             headers=headers, data=data)
    data = json.loads(response.text)
    print(data['Success'])
    pass


if __name__ == '__main__':
    # 升级
    # count = 101
    # for i in range(350):
    #     stages(str(i + count))
    #     print(i)

    # 获取砖石 10001-10020
    count = 10001
    for i in range(5):
        reward(str(i + count))
        print(i)
