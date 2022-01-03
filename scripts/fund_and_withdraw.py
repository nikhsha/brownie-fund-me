from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    fund_me.fund({"from": account, "value": entrance_fee + 10})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def get_price():
    fund_me = FundMe[-1]
    return fund_me.getPrice()


def main():
    fund_me = FundMe[-1]

    print(fund_me.getPrice())

    entrance_fee = fund_me.getEntranceFee()
    conversion_rate = fund_me.getConversionRate(entrance_fee)
    print(f"current entry fee is {entrance_fee}")
    print(f"converted that is {conversion_rate}")
    fund()
    # withdraw()
