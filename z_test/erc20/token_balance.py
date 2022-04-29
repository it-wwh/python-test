import json
import time
from json import JSONEncoder
import os

from tqdm import tqdm
from web3 import Web3

# 本地运行需要设置代理
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"

web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161"))
contract_address = "0x59d1e836F7b7210A978b25a855085cc46fd090B5"
from_block_number = 14171601
to_block_number = 14211601
is_connected = web3.isConnected()

with open('IERC20.json', 'r') as f:
    abi = json.load(f)
token_contract = web3.eth.contract(address=contract_address, abi=abi)


# 指定区块查询账户ERC20余额
def get_token_balance(_address: str):
    _balance = 0
    try:
        _balance = token_contract.functions.balanceOf(_address).call(block_identifier=to_block_number)
    except Exception as e:
        time.sleep(5)
        print("获取用户余额失败，正在重试。。。\n{}".format(e))
        _balance = get_token_balance(_address)
    return _balance


# 指定区块查询ERC20token用户
def get_address_list(from_block, to_block):
    address_list = set()
    try:
        transfer_events = token_contract.events.Transfer.createFilter(fromBlock=from_block, toBlock=to_block)
        for event in transfer_events.get_all_entries():
            address_list.add(str(event['args']['from']))
            address_list.add(str(event['args']['to']))
    except ValueError:
        print("Transfer事件过多，开始批量执行。。。")
        count = 0
        while from_block < to_block:
            count = count + 1
            _to_block = from_block + 1000
            if _to_block >= to_block:
                _to_block = to_block
            print("【获取用户列表】执行第 {} 次: {}->{}".format(count, from_block, _to_block))
            transfer_events = token_contract.events.Transfer.createFilter(fromBlock=from_block, toBlock=_to_block)
            for event in transfer_events.get_all_entries():
                address_list.add(str(event['args']['from']))
                address_list.add(str(event['args']['to']))
            from_block = _to_block + 1
    export_user_address(address_list)
    return address_list


class setEncoder(JSONEncoder):
    def default(self, obj):
        return list(obj)


# 防止网络连接中断，导出用户地址
def export_user_address(_address_list: set):
    json_data = json.dumps(_address_list, indent=4, cls=setEncoder)
    with open('./address.json', 'w') as a:
        json.dump(json_data, a, ensure_ascii=False, indent=4)


# 读取用户地址
def read_user_address():
    with open('./address.json') as a:
        address_list = json.loads(json.load(a))
    return address_list


if __name__ == '__main__':
    print("web3 is connected: {}".format(is_connected))
    if is_connected is True:
        print("get token balance start")
        result = {}
        # for address in tqdm(read_user_address()):
        for address in tqdm(get_address_list(from_block=from_block_number, to_block=to_block_number)):
            balance = get_token_balance(web3.toChecksumAddress(address))
            if balance > 0:
                result[address] = str(balance)
        with open('./token_balance.json', 'w') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        print("get token balance end")
