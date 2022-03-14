from decimal import Decimal

from web3 import Web3

web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
isConnected = web3.isConnected()
blockNumber = web3.eth.block_number


# 查找区块
def get_block(block):
    return web3.eth.get_block(block)


# 查询账户余额
def get_balance(address: str):
    return web3.eth.get_balance(address)


# 查找交易
def get_transaction(tx_id):
    return web3.eth.get_transaction(tx_id)


if __name__ == '__main__':
    print('web3 test start')
    # print(isConnected)
    # print(blockNumber)
    # print(get_block(1))
    # print(get_block("latest"))
    # print(get_balance('0x38AabFFc1239788232025B37610Dd0FE7EB3aD73'))
    # print(web3.fromWei(get_balance('0x38AabFFc1239788232025B37610Dd0FE7EB3aD73'), 'ether'))
    # print(web3.toWei(Decimal('3841357.360894980500000001'), 'ether'))
    # print(get_transaction('0x3eca56130f24789c1dcc59f5482f0ddba29f435c725733c6dd0f8a1cfd611cea'))
    print(web3.isAddress('0x38AabFFc1239788232025B37610Dd0FE7EB3aD73'))
pass
