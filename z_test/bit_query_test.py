#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

from util import request_util


def run_query(_query):  # A simple function to use requests.post to make the API call.
    headers = {'X-API-KEY': 'BQYaMNRqUujPXjmByJ3CMw2x9tZFlIXD'}
    request = request_util.post_json('https://graphql.bitquery.io/', json.dumps({'query': _query}), headers=headers)

    if request.status_code == 200:
        return json.loads(request.text)['data']
    else:
        raise Exception('Query failed and return code is {}.{}'.format(request.status_code, _query))


# The GraphQL query
query = """
{
  ethereum(network: ethereum) {
    dexTrades(
      baseCurrency: {is: "0x1f9840a85d5af5bf1d1762f925bdaddc4201f984"}
      quoteCurrency: {is: "0xdac17f958d2ee523a2206206994597c13d831ec7"}
      options: {desc: ["block.height", "transaction.index"], limit: 1}
    ) {
      block {
        height
        timestamp {
          time(format: "%Y-%m-%d %H:%M:%S")
        }
      }
      transaction {
        index
      }
      baseCurrency {
        symbol
      }
      quoteCurrency {
        symbol
      }
      quotePrice
    }
  }
}

"""

if __name__ == '__main__':
    result = run_query(query)  # Execute the query
    print('Result - {}'.format(result))
