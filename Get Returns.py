# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MRBSBdZUTbeNy-jCKZfr0A17FE4TOL2R
"""

import yfinance as yf
import pandas as pd

def get_stock_data(symbol):

    data = yf.download(symbol, group_by='Ticker')


    print("数据列名：\n", data.columns)

    if isinstance(data.columns, pd.MultiIndex):

        prices = data[(symbol, 'Close')]
    else:
        prices = data['Close'] if 'Close' in data.columns else None

    if prices is None:
        print(f"Error: 无法找到 '{symbol}' 的收盘价数据。")
        return None

    return prices

def get_returns(pricevec):
    """
    计算每日收益率。
    """
    n = len(pricevec)
    if n < 2:
        return None

    ratiovec = pricevec[1:n] / pricevec[:n-1]
    returns = ratiovec - 1
    return returns

symbol = 'GS'
prices = get_stock_data(symbol)

if prices is not None:
    print("成功下载数据，首5行：")
    print(prices.head())

    returns = get_returns(prices.values)
    print("\n计算出的收益率：")
    print(returns[:5])