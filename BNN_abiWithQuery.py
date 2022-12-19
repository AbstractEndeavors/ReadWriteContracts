from web3 import Web3
import json
import clipboard
import webbrowser
import subprocess
import os
import sys
import pyperclip
import functions as f
import grabAbi as grab
import fileFinder as find
import networkChoose as choose
import parse_funs as parse
import manyNet as many
import pK as priv
import PySimpleGUI as sg
import inputVars as inpAsk
import guiNetAndAsk as guiNet

def specificverifyInput(inType,inVar,outType,outVar,fun,ask):
    asky = ''
    layout = [[sg.Text(ask), sg.Yes()],
            [sg.Text('choose anther '+outVar+' input:'), sg.No()],
            [sg.Yes(), sg.No()]]
    window = sg.Window('Window Title', layout)
    while asky == '':             
        event, values = window.read()
        print(values)
        if event in (sg.WIN_CLOSED, 'Cancel'):
            asky = False
        window.close()
        asky = True
    window.close()  
    return asky
def specificAskInput(inType,inVar,fun,ask):
    asky = ''
    y = asky
    layout = [
        [sg.Text(inType + ' '+ inVar), sg.Push(), sg.Input('', key=inType)],
        [sg.Text('Input Verification'), sg.Push(), sg.Input('', disabled=True, key='verify')],
        [sg.OK('OK'),sg.Button('Show'), sg.Button('Exit'),]]
    window = sg.Window(fun, layout)
    while asky == '':
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            asky = 'exit'
        if event == sg.OK() or event == 'OK':
            asky = values[inType]
        elif event == 'Show':
            x_string = values[inType]
            if 'address' in inType:
                y = addressVerify(inType,x_string)
                if y == False:
                    y = 'checkSum was unable to verify '+x_string+' '+inType
                else:
                    y = inType+' is good to go!'
            if 'uint' in inType:
                y = uintVerify(inVar,x_string)
                if y == False:
                    y = x_string+'is not a valid '+inType+' input'
                else:
                    y = inType+' is good to go!'
            window['verify'].update(value=y)
    window.close()
    return asky
def askContractAddress(inType,inVar,ask):
    asky = ''
    y = asky
    layout = [
        [sg.Text(inType + ' '+ inVar), sg.Push(), sg.Input('', key=inType)],
        [sg.Text('Input Verification'), sg.Push(), sg.Input('', disabled=True, key='verify')],
        [sg.OK('OK'),sg.Button('Show'), sg.Button('Exit'),]]
    window = sg.Window(ask, layout)
    while asky == '':
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            asky = 'exit'
        if event == sg.OK() or event == 'OK':
            asky = values[inType]
        elif event == 'Show':
            x_string = values[inType]
            if 'address' in inType:
                y = addressVerify(inType,x_string)
                if y == False:
                    y = 'checkSum was unable to verify '+x_string+' '+inType
                else:
                    y = inType+' is good to go!'
            if 'uint' in inType:
                y = uintVerify(inVar,x_string)
                if y == False:
                    y = x_string+'is not a valid '+inType+' input'
                else:
                    y = inType+' is good to go!'
            window['verify'].update(value=y)
    window.close()
    return asky
def askList(nets):
    y = []
    sg.set_options(suppress_raise_key_errors=False, suppress_error_popups=False, suppress_key_guessing=False)
    layout = [[sg.Text('functions:'),sg.Combo(nets, key='functions'), sg.Push()],
    [sg.OK('OK'),sg.Button('Show'),sg.Button('Exit')]]

    window = sg.Window('Window Title', layout, finalize=True)
    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.OK() or event == 'OK':
            return values['functions']
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
    window.close()
def addressVerify(va,y):
    return grab.tryCheckSum(str(y))
def uintVerify(va,y):
    return f.isInt(y)
def createSelectList():
    layout = [[sg.Listbox(values=lsN, size=(30, 6))]]
    window = sg.Window('To Do List Example', layout)
    print(window)
def print_scan():
    info = f.jsIt(f.reader(crPa('currFun','Info.json')))
    li = info['scanner']
    if 'api-' in info['scanner']:
        li = info['scanner'].split('api.'.replace('.','-'))[1]
    return 'https://'+li
def get_hash(x):
    spl = 'api.'
    if 'api-' in scanners:
        li = scanners.split(spl.replace('.','-'))[1]
    return 'https://'+li
def decimal():
    try:
        dec = cont.functions.decimals().call()
        return dec
    except:
        return 18
def keys(js):
    lsN = []
    if type(js) is str:
        return lsN
    for key, value in js.items():
        lsN.append(key)
    return lsN
def send_it(ans):
    tx = f.jsIt(ans)
    tx["nonce"] = w3.eth.getTransactionCount(check_sum(tx['from']))
    tx['gas'] = w3.eth.estimateGas({'to': check_sum(tx['to']), 'from': check_sum(tx['from']), 'value': tx['value']})
    signed_tx = w3.eth.account.sign_transaction(tx, key.p)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
def findIt(x,k):
    for i in range(0,len(x)):
        if x[i] == k:
            return i
def chooseAbi():
        return getContLoop()
def getABInet():
        names = varis['names']
        for i in range(0,len(names)):
                varis[names[i]] = f.jsIt(reader(f.crPa(f.crPa(['variables',names]),'info.json')))
def getContLoop():
        while True:
                add = askContractAddress('address','contractAddress','please enter an address for the contract youd like to pull')
                import RPCFolder.RPCSettings as RPCset
                rp = guiNet.askList(many.getAllSource(add))
                sys.path.insert(0, "RPCFolder")
                #rp = RPCset.askList(f.jsRead('RPCList.json'))
                sys.path.insert(0, str(home))
                input(rp)
                if rp == 'Auto':
                    rp = guiNet.askList(many.getAllSource(add))
                #else:
                #    extractFromJs(f.jsIt(rp['RPC']))
                if guiNet.simpleBool('is contract '+str(add)+' that youre looking for associated with the name '+str(rp['contName'])+'?') == True:
                    return many.saveSoureces(add,getSource(add,stripWeb(f.jsIt(rp['RPC'])['blockExplorer']))[0],f.jsIt(rp['RPC']))#,add,rp['contName'],rp['RPC']
                print('looks like '+str(add)+' was not a valid address, the checksum didnt verify, we will let you know if it is or isnt on the network once we get a valid address')
def safeSplit(x,y,k):
    if y in x:
        z = x.split(y)
        if len(z) > k:
            return z

def listFolds(x):
    lsN = []
    ls = find.foldList(x)
    for i in range(0,len(ls)):
        n = f.crPa([x,ls[i]])
        if find.isFold(n):
            lsN.append(n.split('/')[-1])
    return lsN
def createJsLs(ls,js):
    for i in range(0,len(ls)):
        js[ls[i]] = []
    return js
def getCurrFoldAndPrevPath(x,y):
    fold = f.createPath(x,y)
    currLs = listFolds(fold)
    return fold,currLs
def ifNoInJsLsandJsJs(js,x,y):
    if x not in js:
        js[x] = [y]
    if y not in js:
        js[y] = {}
    return js
def ifNoInJsjs(js,x):
    if x not in js:
        js[x] = {}
    return js
def checkVarFold():
    varis={}
    varis['adds'] = {}
    varis['adds']['all'] = []
    varis['jsAll'] = {'names':[],'contracts':{}}
    varis['netNames'] = listFolds('variables')
    varis = createJsLs(varis['netNames'],varis)
    networkNames = varis['netNames']
    for i in range(0,len(networkNames)):
        netName = networkNames[i]
        varis[netName] ={}
        pa1,currNets = getCurrFoldAndPrevPath('variables',netName)
        for kk in range(0,len(currNets)):
            currNet = currNets[kk]
            varis[netName] = ifNoInJsLsandJsJs(varis[netName],'currNets',currNet)
            pa2,chainIds = getCurrFoldAndPrevPath(pa1,currNet)
            for k in range(0,len(chainIds)):
                chainId = chainIds[k]
                pa3,adds = getCurrFoldAndPrevPath(pa2,chainId)
                varis[netName][currNet] = ifNoInJsLsandJsJs(varis[netName][currNet],'chainIds',chainId)
                for c in range(0,len(adds)):
                    addr = adds[c]
                    pa4,rpcs = getCurrFoldAndPrevPath(pa3,addr)
                    varis[netName][currNet][chainId] = ifNoInJsLsandJsJs(varis[netName][currNet][chainId],'adds',addr)
                    for j in range(0,len(rpcs)):
                        rpcN = rpcs[j]
                        pa5,files = getCurrFoldAndPrevPath(pa4,rpcN)
                        varis[netName][currNet][chainId][addr] = ifNoInJsLsandJsJs(varis[netName][currNet][chainId][addr],'rpcs',rpcN)
                        if False not in [f.exists(crPa(pa5,'funcSheet.py')),f.exists(crPa(pa5,'Info.json')),f.exists(crPa(pa5,'allCalls.json')),f.exists(crPa(pa5,'ABI.json'))]:
                            varis['adds']['all'].append(addr)
                            varis['adds'][addr] = pa5
                            Info = f.jsIt(f.reader(crPa(pa5,'Info.json')))
                            name = addr
                            if name not in varis['jsAll']['contracts']:
                                varis['jsAll']['names'].append(name)
                                varis['jsAll']['contracts'][name] = {'RPCs':[],'SourceCode':[]}
                            varis['jsAll']['contracts'][name]['RPCs'].append(Info['RPC'])
                            varis['jsAll']['contracts'][name]['SourceCode'].append(Info)
    f.pen(varis,f.crPa(['variables','varis.json']))
    return varis
def copyAndStart(path):
        f.copyIt(crPa(path,'dothefunx.py'),'currFun')
        f.copyIt(crPa(path,'funcSheet.py'),'currFun')
        f.copyIt(crPa(path,'Info.json'),'currFun')
        f.copyIt(crPa(path,'allCalls.json'),'currFun')
        f.copyIt(crPa(path,'ABI.json'),'currFun')
        f.copyIt(crPa(path,'allWallVar.json'),'currFun')
        import currFun.funcSheet as func
        sys.path.insert(0, createPath(home,"currFun"))
        askLoop = True
        import dothefunx as doEm
        while askLoop == True:
            doEm.func.hubbub()
        #allCalls = f.jsIt(f.readerC(crPa('currFun','allCalls.json')))
        #if guiNet.simpleBool('would you like to view all viewable variables in the contract?'):
        #    find.createAsk(func.view_all())
        #ex = createInp(allCalls['call'])
def chooseExistingWallet(name):
   wallJs = f.existsMake({'types':['main','poor','tester','migrate'],'names':[],'adds':{'adds':[]},'main':{'names':[]},'poor':{'names':[]},'tester':{'names':[]},'migrate':{'names':[]}},'walls/wallsJs.json')
   while True:
      js = {'calls':[['change name','change address associated with name','pick new name'],['changeName','changeAddress','new']],'asks':[wallJs['names'],wallJs['names']],'inquiry':['looks like the name '+name+' is taken, did you want to exit and use that one? with the associated key and address of '+wallJs[name]['add']]}
      ask = find.createAsk(js)
      if ask == 'changeAddress':
         changeEnv(name)
         return
      if name in wallJs['names']:
         loadKey(name)
         return
      if ask == 'new':
         getWallName(wallJs)
def changeEnv(name):
   path = 'walls/'+name+'.env'
   f.pen('privateKey = '+input('please enter the private key:'),path)
   js[name]['add'] = w3.eth.account.privateKeyToAccount(priv.getKey(name))
   f.pen(js,'walls/wallJs.json')
   loadKey('walls/'+name+'.env')
   return 
def getWallName(wallJs):      
   wallJs = f.existsMake({'types':['main','poor','tester','migrate'],'names':[],'adds':{'adds':[]},'main':{'names':[]},'poor':{'names':[]},'tester':{'names':[]},'migrate':{'names':[]}},'walls/wallsJs.json')
   while True:
      name = input('what would you like to call the wallet?: ')
      if name not in wallJs['names']:
         changeEnv(name)
      js = {'calls':[],'asks':[['change name','change address associated with name','pick new name','choose an existing wallet'],['changeName','changeAddress','new','existing']],'inquiry':['looks like the name '+name+' is taken, did you want to exit and use that one? with the associated key and address of '+wallJs[name]['add']]}
      ask = find.createAsk(js)
      if ask == 'changeAddress':
         changeEnv(name)
         return
      if ask == 'existing':
         chooseExistingWallet()
         return
def deriveAllWeb3FromInfo(x):
   currInfo = getNetworkInfo(x)
def askGets():
    calls = f.jsIt(f.reader(crPa('currFun','allCalls.json')))
    asks['asks'] = [calls['asks'],calls['asks']]
    asks['inq'] = ['which function would you like to use?']
    return askAbi()
def askNet():
   asks['asks'] = [varis['networks'],varis['networks']]
   asks['inq'] = ['which network would you like to use?']
   return askAbi()
def askNetAbi(net):
   asks['asks'] = [varis[net]['adds'],varis[net]['adds']]
   asks['inq'] = ['which contract would you like to use?']
   return askAbi()
def askAllAbis():
   asks['asks'] = [varis['adds']['all'],varis['adds']['all']]
   asks['inq'] = ['which contract would you like to use?']
   return askAbi()
def askAbi():
   asks['calls'] = [['exit','to change network','add another contract','add switch contract','to add new wallet wallets','to switch wallets','switch to All Address Select'],['exit','changeNet','newCont','changeCont','switchWaLL','newWall','swtchAllAbis']]
   while True:
      ask = find.createAsk(asks)
      if str(ask) == 'changeNet':
         askNet()
      elif str(ask) == 'exit':
         exit()
      elif str(ask) == 'newCont':
         return chooseAbi()
      elif str(ask) == 'changeCont':
         otherStart()
      elif str(ask) == 'newWall':
        getWallName(wallJs)
      elif str(ask) == 'switchWaLL':
         chooseExistingWallet()
      elif str(ask) == 'swtchAllAbis':
         askAllAbis()
      elif ask in asks['asks'][1]:
          return ask
def saveSoureces(add,SourceCode,rpc):
    many.saveSoureces(add,SourceCode,rpc)
def getSource(add,scans):
    return many.getSource(add,scans)
def stripWeb(x):
    return many.stripWeb(x)
def extractFromJs(js):
    nativeCurrency,network,RPC,chainId,blockExplorer,scanner,w3 = many.extractRPCdata(js)
    return nativeCurrency,network,RPC,chainId,blockExplorer,scanner,w3
def getNetworkInfo(path):
   if path.split(slash)[-1] != 'info.json':
      if find.isFold(path) == False:
         return False
      path = crPa(path,'info.json')
   if find.isFile(path) == False:
      return False
   netName,chainId,rpc,nativeCurrency,explorer,scanner,w3  = grab.deriveFrom(f.jsIt(f.jsIt(f.reader(path))))
   return netName,chainId,rpc,nativeCurrency,explorer,scanner,w3                                 
def askAdd():
   checkVarFold()
   js = {'calls':[['to choose new contract'],['newCont']],'asks':[varis['networks'],varis['networks']],'inq':['looks like you have prior contracts on the folowing networks:']}
   return guiNet.askList(varis['jsAll'])
def createPath(x,y):
    return f.createPath(x,y)
def crPa(x,y):

   return f.createPath(x,y)
def checkCurrAbis():
   if len(varis['adds']['all']) == 0:
      copyAndStart(getContLoop())
def checkIfCurrInfoExists():
   if f.exists(crPa('current','info.json')):
      curr = json.loads(f.reader(currPa('current','info.json')).replace("'",'"'))
      if 'path' in curr:
         if False not in [f.exists(crPa(curr['path'],'funcSheet.py')),f.exists(crPa(curr['path'],'info.json')),f.exists(crPa(curr['path'],'allCalls.json')),f.exists(crPa(curr['path'],'ABI.json'))]:
            if 'add' in curr:
               if find.boolAsk('looks like the last used address is '+curr['add']+', associated with the name '+curr['name']+' on the '+curr['network']+' network using RPC address '+curr['RPC']+' did you want to use this one?'):
                    copyAndStart(curr['path'])    
def otherStart():
   net = askNet()
   copyAndStart(crPa('variables',crPa(net[0]['RPC']['info']['path'],askNetAbi(net))))
def useExistingABIs():
    import RPCFolder.RPCSettings as RPCset
    sys.path.insert(0, "RPCFolder")
    rp = RPCset.askList(f.jsRead('RPCList.json'))
    #askList(varis['jsAll'])['info']['path']
    copyAndStart(guiNet.askList(rp))
global home,slash,varis,wallJs,netName,chainId,rpc,nativeCurrency,explorer,scanner,w3,asks
asks = {'call':[],'ask':[],'inq':[]}
home,slash = f.homeIt()
f.mkDirLs(['currFun'])
f.mkDirLs(['variables'])
f.mkDirLs(['walls'])
currInfo = getNetworkInfo('currFun')
if currInfo != False:
   netName,chainId,rpc,nativeCurrency,explorer,scanner,w3 = currInfo

varis = checkVarFold()
#useExistingABIs()
copyAndStart(getContLoop())
checkCurrAbis()
#  
#  checkIfCurrInfoExists()
#  otherStart()
      


