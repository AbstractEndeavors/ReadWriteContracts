import requests
import json
from web3.contract import ContractEvent
from web3.contract import Contract
from web3._utils.events import get_event_data
from web3 import Web3
from web3.auto import w3
import networkChoose as choose
import functions as f
def stripWeb(x):
    if 'http' in x:
        x = x.replace('https','').replace('http','')
        while x[0] in [':',slash] and len(x)>1:
            x = x[1:]
    return x.split(slash)[0]
def sites(A):
    U = [A]
    for url in U:
        X = str(U[0])
        r = requests.get(X)
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
def chooseIt():
    global netName,chainId,rpc,nativeCurrency,explorer,scanner,w3
    netName,chainId,rpc,nativeCurrency,explorer,scanner,w3 = chooseIt()
    netName,chainId,rpc,nativeCurrency,explorer,scanner = f.eatAllLs([netName,chainId,rpc,nativeCurrency,explorer,scanner],[' ',''])
def getAbi(add):
    global netName,chainId,rpc,nativeCurrency,explorer,scanner,w3
    return sites('https://api.'+str(scanner)+'/api?module=contract&action=getabi&address='+checkSum(str(add))+'&apikey='+str(apiKey(scanner))) 
def getSource(add):
    chooseIt()
    return netName,chainId,rpc,nativeCurrency,explorer,scanner,w3,sites('https://api.'+str(scanner)+'/api?module=contract&action=getsourcecode&address='+checkSum(str(add))+'&apikey='+str(apiKey(scanner)))
def checkSum(x):
    return w3.toChecksumAddress(x)
def chooseIt():
    global netName,chainId,rpc,nativeCurrency,explorer,scanner,w3
    netName,chainId,rpc,nativeCurrency,explorer,scanner,w3 = choose.mains()
    return netName,chainId,rpc,nativeCurrency,explorer,scanner,w3
def getRPC(js):
    if 'RPC' in js:
        return js['RPC']
    return False
def ifAnyNameInAll(js):
    net = ''
    needs = ['netName','chainId','RPC','nativeCurrency','blockExplorer','scanner']
    for i in range(0,len(needs)):
        nee = needs[i]
        if nee not in js:
            js[nee] = ''
        if nee in js:
            if js[nee] in ['',False,' ',None]:
                if net != '':
                    if nee in net:
                       js[nee] = net[nee]
            elif findAnyId(js[nee],nee) != False:
                net = findAnyId(js[nee],nee)
                if nee in net:
                   js[nee] = net[nee]
    return js
def getChainId(js):
    nee = needs[i]
    for k in range(0,len(find)):
        if getRPC(js) == find[k]['RPC']:
            return find[k]['chainId']
    return False
def getExplorer(js):
    if 'blockExplorer' in js:
        return js['blockExplorer']
    elif getScanner(js) != False:
        return 'https://'+str(getScanner(js))
    return False
def getScanner(js):
    if 'scanner' in js:
        return js['scanner']
    elif getExplorer(js) != False:
        return stripWeb(getExplorer(js))
    return False
def getNetName(js):
    if 'networkName' in js:
        return js['networkName']
    elif 'chainId' in js:
        if findAnyId(js['chainId'],'chainId') != False:
            net = findAnyId(js['chainId'],'chainId')
            return netName
    return False
def findAnyId(x,st):
    allN = allNets()
    names = allN['names']
    for i in range(0,len(names)):
        net = allN[names[i]]
        for k in range(0,len(net)):
            if st in net[k]:
                if net[k][st] == x:
                    return net
    return False,False
def allNets():
    return choose.allNets()
def deriveFrom(js):
    js = ifAnyNameInAll(js)
    netName,chainId,rpc,nativeCurrency,explorer,scanner,w3 = js['netName'],js['chainId'],js['RPC'],js['nativeCurrency'],js['blockExplorer'],js['scanner'],Web3(Web3.HTTPProvider(js['RPC']))
    return netName,chainId,nativeCurrency,explorer,rpc,stripWeb(explorer),w3
def tryCheckSum(x):
    try:
        y = w3.toChecksumAddress(x)
        return y
    except:
        return False
global netName,chainId,rpc,nativeCurrency,explorer,scanner,w3,home,slash 
home,slash = f.homeIt()

