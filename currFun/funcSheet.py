from web3 import Web3
import sys
import os
home = os.getcwd()
sys.path.insert(0, "/home/bigrugz/Documents/python_scripts/newScripts")
import pK as key
import networkChoose as choose
import json
import functions as f
sys.path.insert(0, str(home))
home,slash = f.homeIt()
def LIDO():
	x = cont.functions.LIDO().call()
	f.pen(x,"ask.txt")
	print("LIDO"," is ",x)
	return x
def TREASURY():
	x = cont.functions.TREASURY().call()
	f.pen(x,"ask.txt")
	print("TREASURY"," is ",x)
	return x
def recoverERC20(address__token,uint256__amount):
	x = cont.functions.recoverERC20(address__token,uint256__amount).call()
	f.pen(x,"ask.txt")
	print("recoverERC20"," is ",x)
	return x
def recoverERC721(address__token,uint256__tokenId):
	x = cont.functions.recoverERC721(address__token,uint256__tokenId).call()
	f.pen(x,"ask.txt")
	print("recoverERC721"," is ",x)
	return x
def withdrawRewards(uint256__maxAmount):
	x = cont.functions.withdrawRewards(uint256__maxAmount).call()
	f.pen(x,"ask.txt")
	print("withdrawRewards"," is ",x)
	return x
def view_all():
	print("LIDO",":",f.printHex(cont.functions.LIDO().call()))
	print("TREASURY",":",f.printHex(cont.functions.TREASURY().call()))
	
global network,chainId,rpc,explorer,scanner,w3,nonce
add = "0x388C818CA8B9251b393131C08a736A67ccB19297"
abi = f.readerC(f.crPa(["variables/Ethereum/0x388C818CA8B9251b393131C08a736A67ccB19297","ABI.json"]))
network,chainId,rpc,explorer,scanner,w3 = "Ethereum","0x1","https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161","https://etherscan.io","etherscan.io",Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161"))

cont = w3.eth.contract(add,abi = abi)
account_1 = w3.eth.account.privateKeyToAccount(key.p)
nonce = w3.eth.getTransactionCount(account_1.address)