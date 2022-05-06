from brownie import FundMe
from scripts.helper_scripts import get_account


def fund():
    fund = FundMe[-1]
    account = get_account()
    entrance_fee = fund.getEntranceFee()
    print(entrance_fee)
    print(f"Current entrance fee is {entrance_fee}")
    print("Funding")
    fund.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund = FundMe[-1]
    account = get_account()
    print("Withdrawing...")
    fund.withdraw({"from": account})


def main():
    fund()
    withdraw()
