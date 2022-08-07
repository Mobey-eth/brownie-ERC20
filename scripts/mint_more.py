from brownie import accounts
from scripts.helpful_scripts import get_account
from scripts.deploy_token import deploy_token
import time
from brownie import NinaCoin, accounts

# function was internal lol


def mint_more():
    account = get_account()
    token_adr = deploy_token()
    token_adr._mint(accounts[1], 1000, {"from": account})
    print("minted more")
    time.sleep(1)


def getbal():
    account = get_account()
    token_adr = deploy_token()
    bal = token_adr.balanceOf(account)
    print(f"The bal is {bal}")


def main():
    getbal()
