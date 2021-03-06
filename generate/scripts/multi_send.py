#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import click
from brownie import network, accounts, BatchTransfer, interface


# brownie run --network bsc-test ./scripts/multi_send.py
def main():
    print(f"You are using the '{network.show_active()}' network")
    account = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
    print(f"You are using: 'account' [{account.address}]")

    token_address = '0x815B1c7841D81FDE39D93c5768B1C9ad1B0770De'
    batch_transfer_address = '0xd1BEA303E9Bbe726c093f19eee6B742BA0595Cb2'

    batch_transfer = BatchTransfer.at(batch_transfer_address)
    erc20_token = interface.IERC20(token_address)
    allowance = int(1000000000 * 10 ** 18)

    to_address_list = ['0x7ad50caaa3d77778ef74a18b9e29013648fe0a20', '0xe668b92a13bace33d7bff6354a8d4bda07877c2d',
                       '0x19cc3dbd5abbc2f03737dcfebf9776f9f8bc7fe0', '0xcf7b09e778584c65fb95c01dfdd351ed5bc96b17',
                       '0x36eb907801169f75a1038826e6e792b02a4ca8e9', '0xb9b6afef30045aed6cd0fde317d6449199e012f8',
                       '0x08b767b73e77465b931fa5ede00af0c1cf9c4439', '0x4fd4ed9d654986ac573d3aa5bf143c6693329d9a',
                       '0xee8645198ee1188f5f86d51d98549ab004cf54ff', '0xc57c6429134db31b95d136ce8351762e5d26eb0c',
                       '0x0f84448b0ca4086b45d6b009c24b1211d6787cea', '0x26e8e5822ac2ee937db1957904831be3fd49889f',
                       '0x6b9ad7e4267048f6f0c516c6a451398c5f44e194', '0x1514eb4ece9585932384668a1e888b9a9d48aef5',
                       '0x5eb4b35858b001a431bd3454ea53c689321ddbbf', '0x82b8e33196dd1921904abb5e87dbb210d774abc9',
                       '0x5dd537d0ccfaf2dcd9e7d1cef2dde11793ba76c4', '0x51d85af8203ef33d90d82386c8341a9cb04364ac',
                       '0x60880614edede703e6215eb208d60ec6f9ed328e', '0x7407e809f2759ef36962a445d73d877c10f2a6b4',
                       '0x244045e4e104c5d9507acd22d5b53f231acbc265', '0xeb445af32819fecd5c4624bfcd0c708cf76d0ea6',
                       '0xee8f7dd12b2d60607c9c5c5eac45659dd14c2ebf', '0x326aa8f1141aa98fc4e46b475e7809b89da7e167',
                       '0x6b5f3a60d7f34cff87f20428edad15e835fad3c0', '0x76556030e29d7698fe962466c226e7b6981ece14',
                       '0xb5abd594dec64fd9a0543f93cab3e939e814ccad', '0x3324f86301c61ad640a002146de34061ea9aa7aa',
                       '0x1155f119eeee9be7e7ce88f4655cb9ce212979f3', '0x298c3d17ab53ae2b4500a9b14638b8f5fdd029ba',
                       '0x8eb986b7a504bce701bb11c8c52146e8680f659a', '0x9be1c6ddad17d83ee99875f11595c84adfa716a2',
                       '0x8a2ad3d95e530a4c490e8669d666dd9b2ebbe6b1', '0x239e76782f4078f0b8449fb0487841eb4cebd127',
                       '0xdc7773d46569dc51f33b6a7cf0cccd35688ce472', '0xc4a30797c0eae87b1cba549cc77c2e5e5a4c8929',
                       '0x0f531bac466eba88e73ad2fa37dba73c761b7cf8', '0xef096ef8dc75fdd06ca25d9e0b1af401f75e2e4c',
                       '0x329151008a53050cd4aa918d57af2a04b00ae0c7', '0xe101924970d48b480f68fc97df01a2218403b0db',
                       '0x1d245209b892b7af4b6a0232a4339f3f4195211f', '0x71010061634575d40fbc383bc7244eda44f7aedd',
                       '0x4bc5644eb345172db3787c17ad0def97497bba4f', '0x43062a5a5bdbf154246b661f273246421304f529',
                       '0x29d0675308b39eedbe36ba88e41f3a206d6271c4', '0xc498a493a3f2eee3499c10a0cdd18856c13c959e',
                       '0x29cdb6890695912c94d430c4d2eb919e3380c25b', '0x128a80f40772158ba9b9fae170dbaf7ae12fb34b',
                       '0x357c9eead7bd0157c891eee7fe6e25e90ccaa392', '0x26a6a49649f5d78991256d490f60bcedd8c9b48d',
                       '0xadd75ce4be74c7d6592472f3b4eb3488e859518d', '0xf519c9e290a6dc681be285e3bfebc3ac47b9a858',
                       '0xce8b9a8c371acf70d13239863249edc2a8dc7d58', '0x81fb73e9826400c0acaf18b8d2b80f4b9ce62fa1',
                       '0x28bf2d5ce6ccd332590a85d678b6b47cc0d6350a', '0x340173b1abd70f52dac92b6d270bc7f2c4fac614',
                       '0x4fb25b0ea296d908de30832c9fc862a24074223e', '0xbf6ba9fd2775f56e5109e9e72f2259b820c2f741',
                       '0x03653da3c445bd5c00b7363e4dca33aa8b745a7b', '0xd5f5bbbbc55c3ac6ccde9fdd96ee12379bc9f468',
                       '0xe49e1b06ea2e053bdeb11f686497748b926fee45', '0x453d1f6ba11d85d3c1698934db5d264016104b9a',
                       '0x7ee2f50e4e1421d5ede27083b432ded30250251f', '0x15dbb7b7cc8d1a231b9b72ee24cd0dd7df4c0bce',
                       '0xfa4134ab12c5ded1a0a1801b9a6b0543ee5d9bb2', '0x7f92f980c2361cf58d25815b0c502422e56d2e36',
                       '0x42191794b159a45a2ced28fef3d8156b8838a7b1', '0x8aa13bfd99bd0389a35e7d7ae95f81019907525e',
                       '0xd5842f9fd9d74cb7ff60221f254f79d7bea4f81d', '0xa02d85ec04ca5bb8fb23af1d07301e10a14a66a5',
                       '0xfc34b5b061a519bf5ff6b3196e211d78a0b805f1', '0x0f0dce41ce8bbab45e425c2d81b667efaaef913e',
                       '0x19ff65caf9cd56dd4c8bcab64a4f2ce65f679d4f', '0x897e3168cdd2393bf5d8687c90e95682656579b7',
                       '0x2e8e2ed1d924414857b31ca3e230b918744fb45c', '0x913d791d5824caa5e025c9017dc7d4b584492640',
                       '0x9cfb176a114a3c82756f8fee6d06abc638fc11cb', '0x4f0b29ac9090d83307b42ab8bfb67e297cc78b22',
                       '0xc20cf550c1f2f109aaeb0bbea3d170fd74dfdccb', '0xe3b3e66c3d0e27ac42bbb67de9717f0cc68ea770',
                       '0x9ff8d1a5ffabb0297d9c2f08f34f39b0238c8a25', '0x7ef66aab538492d1c81f4ab5720fc2c50caa23eb',
                       '0x7fd81a1fbba60997025d8a56d7b4050b8d1a7d7b', '0x8d16a28c2d3cf30cb70f21d57c3209ef7db3acb6',
                       '0x0072cb9430ab3beb5b856aa69837e589f5c0c70e', '0x3def0ca312b6a082fb50cc266a640e3f6b60fe2a',
                       '0x49c64fb3c106efbc13bab5cee45c023dce5f22a2', '0x0078f408d05ba3522c90c36d633726373ee09ea7',
                       '0xad7075bc8d176acb4c43f07b79e2b4a049d75c6f', '0xfd72547de8a50cbf4e8fe5532b6ed263a5c1d660',
                       '0x42414336863d25a60ce4b5fb6af71cecd5370e09', '0xebfa038d55b83c8b8875350958258092f6c48e12',
                       '0x89a4803df25150b0262b869305d836c44e46f1d8', '0x3690eb9e3c09da53c527be6c21eff79be56536e9',
                       '0x8ff79a308deebaa891dd108a50454f68878616b7', '0xaee16dc2ee7a0b5d6f31e77063dd224c33b03687',
                       '0xd6dee4214cb486669302d14fa99a8c42008eeefd', '0x38a9f218b0a0190b1aac53a4827da4bfb56d1d4f',
                       '0xbed4b6958692ce8370e0fb6e98206ba827637d9e', '0x50fd429b293094b8ef3e4f1af4535dfae1dce0a9']

    def batchTransferEthAvg():
        to_eth_amount = 1 * (10 ** 18)
        batch_transfer.batchTransferEthAvg(to_address_list, {"from": account, 'value': to_eth_amount})
        pass

    def batchTransferEth():
        _to_address_list = ['0x7ad50caaa3d77778ef74a18b9e29013648fe0a20', '0xe668b92a13bace33d7bff6354a8d4bda07877c2d',
                            '0x19cc3dbd5abbc2f03737dcfebf9776f9f8bc7fe0', '0xcf7b09e778584c65fb95c01dfdd351ed5bc96b17',
                            '0x36eb907801169f75a1038826e6e792b02a4ca8e9']
        to_eth_amount_list = [0.01 * (10 ** 18), 0.02 * (10 ** 18), 0.03 * (10 ** 18), 0.04 * (10 ** 18),
                              0.05 * (10 ** 18)]
        to_eth_amount = 0.15 * (10 ** 18)
        batch_transfer.batchTransferEth(_to_address_list, to_eth_amount_list, {"from": account, 'value': to_eth_amount})
        pass

    def batchTransferTokenAvg():
        erc20_token.approve(batch_transfer_address, allowance, {"from": account})
        to_token_amount_avg = 10 * (10 ** 18)
        batch_transfer.batchTransferTokenAvg(token_address, account, to_address_list, to_token_amount_avg,
                                             {"from": account})
        pass

    def batchTransferToken():
        erc20_token.approve(batch_transfer_address, allowance, {"from": account})
        _to_address_list = ['0x7ad50caaa3d77778ef74a18b9e29013648fe0a20', '0xe668b92a13bace33d7bff6354a8d4bda07877c2d',
                            '0x19cc3dbd5abbc2f03737dcfebf9776f9f8bc7fe0', '0xcf7b09e778584c65fb95c01dfdd351ed5bc96b17',
                            '0x36eb907801169f75a1038826e6e792b02a4ca8e9']
        to_eth_amount_list = [1 * (10 ** 18), 2 * (10 ** 18), 3 * (10 ** 18), 4 * (10 ** 18),
                              5 * (10 ** 18)]
        batch_transfer.batchTransferToken(token_address, account, _to_address_list, to_eth_amount_list,
                                          {"from": account})
        pass

    # batchTransferEthAvg()
    # batchTransferEth()
    # batchTransferTokenAvg()
    # batchTransferToken()
