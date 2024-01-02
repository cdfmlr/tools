#!/usr/bin/env python3
import re
import sys
from datetime import datetime


def date_to_port(date_str) -> int:
    """date to port num: '23-10-08' -> 23108."""
    # 解析日期字符串，例如'23-10-08'
    Yy, Mm, Dd = map(int, date_str.split('-'))
    Y = Yy // 10
    y = Yy % 10
    M = Mm // 10
    m = Mm % 10
    D = Dd // 10
    d = Dd % 10

    # 计算端口号
    port = Y * 10000 + y * 1000 + (M + D * 2) * 100 + m * 10 + d

    return port


def port_to_date(port: int) -> str:
    """port num to date: 23108 -> '23-10-08'."""
    port = int(port)
    # 从端口号反向计算日期
    Y = port // 10000
    y = (port // 1000) % 10
    MD = (port // 100) % 10
    M = MD % 2
    D = MD // 2
    m = (port // 10) % 10
    d = port % 10

    # 格式化日期字符串
    date_str = f'{Y}{y}-{M}{m}-{D}{d}'

    return date_str


def convert_print_date(date_str: str):
    """prints the converting from 'date' -> port num and the reverse"""
    # 打印日期到端口号的转换
    port = date_to_port(date_str)
    print(f'Date: {date_str} -> Port: {port}')

    # 打印端口号到日期的转换
    date_str_from_port = port_to_date(port)
    print(f'Port: {port} -> Date: {date_str_from_port}')


def today() -> str:
    """today's date in YY-MM-DD: 2023-10-18 -> '23-10-18'"""
    # Get today's date
    today_date = datetime.now().date()

    # Format the date as "YY-MM-DD"
    formatted_date = today_date.strftime("%y-%m-%d")

    return formatted_date


if __name__ == '__main__':
    date_str = today()

    if len(sys.argv) == 2 and re.match(r'\d{2}-\d{2}-\d{2}', sys.argv[1]):
        date_str = sys.argv[1]
    else:
        print(f'Usage: {sys.argv[0]} <Yy-Mm-Dd>\n')
        print(f'---- Today: $ python src.py {date_str} ----')
    
    convert_print_date(date_str)

