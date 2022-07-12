#!/usr/bin/env python

import logging
import os

from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = "Ci3AurTkvwD4MCw6ZlNVhZtqZF5DJLHz66A5LKsm9iR2kHEHt4LGC6QL1kPV1bgQ"
secret = "M2JAqAQnhXYEAcmFaTszeXx9SvcUNcNfvW9S9mWSbqVf08L6ChwjWZMS4sZVIh8w"

os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"

if __name__ == '__main__':
    spot_client = Client(key, secret)
    logging.info(spot_client.coin_info())
