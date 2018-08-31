#!/usr/bin/python

import argparse


def find_max_profit(prices):
    if len(prices)==1:
      return 0
    else:
      #Initialize max_profit equal to the first pair of prices
      max_profit = prices[1] - prices[0]
    # for each price in prices after the first one:
    for i in range(1, len(prices)):
        # for each price after price at i:
        for price in prices[i+1:]:
            # get the difference, if difference greater than current difference then save to max_profit
            if (price - prices[i]) > max_profit:
                max_profit = price-prices[i]
    return max_profit


if __name__ == '__main__':
    # You can test your implementation by running
    # `python stock_prices.py [prices]` where prices is comprised of
    # space-separated integer values
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
