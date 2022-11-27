import requests
import json
from web3.contract import ContractEvent
from web3.contract import Contract
from web3._utils.events import get_event_data
from web3 import Web3
from web3.auto import w3
import networkChoose as choose
import functions as f
def sites(A):
    U = [A]
    input(U)
    for url in U:
        X = str(U[0])
        input(X)
        r = requests.get(X)
        input(r)
        PS = r.text
        JS = json.loads(PS)['result']
    return JS
def apiKey(scanner):
    if scanner == 'bscscan.com':
        x = 'JYVRVFFC32H2ZSKDY1JZKNY7XV1Y5MCJHM'
    elif scanner == 'polygonscan.com':
        x = 'S6X6NY29X4ARWRVSIZJTG1PJS4IG86B3WJ'
    elif scanner == 'ftmscan.com':
        x = 'WU2C3NZAQC9QT299HU5BF7P8QCYX39W327'
    elif scanner == 'moonbeam.moonscan.io':
        x = '5WVKC1UGJ3JMWQZQAT8471ZXT3UJVFDF4N'
    else:
        x = '4VK8PEWQN4TU4T5AV5ZRZGGPFD52N2HTM1'
    return x
def getAbi(add):
    network,chainId,explorer,rpc,scanner,w3 = chooseIt()
    return sites('https://api.'+str(scanner)+'/api?module=contract&action=getabi&address='+checkSum(str(add))+'&apikey='+str(apiKey(scanner))) 
def getSource(add):
    network,chainId,explorer,rpc,scanner,w3 = chooseIt()
    return network,chainId,explorer,rpc,scanner,w3,sites('https://api.'+str(scanner)+'/api?module=contract&action=getsourcecode&address='+checkSum(str(add))+'&apikey='+str(apiKey(scanner)))
def checkSum(x):
    return w3.toChecksumAddress(x)
def chooseIt():
    network,chainId,explorer,rpc,scanner,w3 = choose.mains()
    network,chainId,explorer,rpc,scanner = f.eatAllLs([network,chainId,rpc,explorer,scanner],[' ',''])
    return network,chainId,explorer,rpc,scanner,w3
def tryCheckSum(x):
    try:
        y = w3.toChecksumAddress(x)
        return y
    except:
        return False
global network,chainId,explorer,rpc,scanner,w3


