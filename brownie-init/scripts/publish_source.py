# -*- coding: utf-8 -*-
from brownie import *
import os

os.environ["http_proxy"] = "http://127.0.0.1:10809"
os.environ["https_proxy"] = "http://127.0.0.1:10809"


# brownie run --network rinkeby ./scripts/publish_source.py
def main():
    print(f"You are using the '{network.show_active()}' network")
    simple_token = SimpleToken.at("0x7260929eb0863d0657c43d338ac5ec90bd74bed9")
    SimpleToken.publish_source(simple_token)
