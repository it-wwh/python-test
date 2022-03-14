# -*- coding: utf-8 -*-
from brownie import *
import os

os.environ["http_proxy"] = "http://127.0.0.1:10809"
os.environ["https_proxy"] = "http://127.0.0.1:10809"


# brownie run --network rinkeby ./scripts/publish_source.py
def main():
    print(f"You are using the '{network.show_active()}' network")
    dao_token = DaoToken.at("0x6d3964dd2eaf9214311a0fc300bb8ea81f8bfb67")
    DaoToken.publish_source(dao_token)
