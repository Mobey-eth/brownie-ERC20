from web3 import Web3
from brownie import NinaCoin
from scripts.helpful_scripts import get_account
import time

initial_supply = Web3.toWei(1000000, "ether")
account = get_account()


def deploy_token():
    myToken = NinaCoin.deploy(initial_supply, {"from": account})
    print("Deployed token contract!")
    print(myToken.name())
    time.sleep(1)
    return myToken


def main():
    deploy_token()
