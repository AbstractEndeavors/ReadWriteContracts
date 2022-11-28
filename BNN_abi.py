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
import pK as priv
def print_scan():
    info = f.jsIt(f.reader(crPa('currFun','info.json')))
    li = info['scanner']
    if 'api-' in info['scanner']:
        li = info['scanner'].split('api.'.replace('.','-'))[1]
    clipboard.copy('https://'+li+'/address/'+str(info['add']))
    return 'https://'+li
def get_hash(x):
    spl = 'api.'
    if 'api-' in scanners:
        li = scanners.split(spl.replace('.','-'))[1]
    clipboard.copy('https://'+li+'/tx/'+str(x))
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
        js = {}
        info,add,name = getContLoop()
        fold = f.mkDirLs([crPa(f.mkDirLs([crPa('variables/',info[0])]),add)])
        js = {'path':fold,'add':add,'name':name}
        infos = ['netName','chainId','RPC','nativeCurrency','blockExplorer','scanner']
        for i in range(0,len(infos)):
                js[infos[i]] = info[i]
        f.pen(info[-1][0]['SourceCode'],f.crPa([fold,'SourceCode.json']))
        f.pen(info[-1][0]['ABI'],f.crPa([fold,'ABI.json']))
        f.pen(js,crPa(fold,'info.json'))
        info = parse.parse_it(add,fold)
        infos = ['funs','asks','call','funAll','funSheet']
        for i in range(0,len(infos)-1):
                js[infos[i]] = info[i]
        f.pen(js,crPa(fold,'allCalls.json'))
        f.pen(info[-1],crPa(fold,'funcSheet.py'))
        return fold
def getABInet():
        names = varis['names']
        for i in range(0,len(names)):
                varis[names[i]] = f.jsIt(reader(f.crPa(f.crPa(['variables',names]),'info.json')))
def getContLoop():
        while True:
                add = grab.tryCheckSum(input('please enter an address for the contract youd like to pull?\n'))
                if add != False:
                        info = grab.getSource(add)
                        if 'ContractName' in info[-1][0]:
                                if find.boolAsk('is contract '+str(add)+' associated with the name '+str(info[-1][0]['ContractName'])+'?') == True:
                                        return info,add,info[-1][0]['ContractName']
                print('looks like '+str(add)+' was not a valid address, the checksum didnt verify, we will let you know if it is or isnt on the network once we get a valid address')
def safeSplit(x,y,k):
    if y in x:
        z = x.split(y)
        if len(z) > k:
            return z
def isAddress(x):
    if x[:len('address')] == 'address':
        return True
def isBool(x):
    if x[:len('bool')] == 'bool':
        return True
def isString(x):
    if x[:len('string')] == 'string':
        return True
def isBytes(x):
    if x[:len('bytes')] == 'bytes':
        return True
def isList(x):
    if x[-1] == ']':
        if x[:-1].split('[')[-1] == '':
            return [x],'*',0
        lsN = []
        for i in range(0,int(x[:-1].split('[')[-1])):
            lsN.append(x)    
        return lsN,i,0
    return x,1,0
def indetLoop(ty,k):
    tot = input('indeterminate '+str(ty)+' list, how many inputs will you be appending to it? (will inquire again at this input interval, otherise, inquiry will repeat every loop)')
    deff = f.isInt(tot)
    if deff == False:
        tot = k + 1
    return tot,deff
def listLoop(k,tot):
    print(str(k)+' out of '+str(tot)+' inputs in this list')
def denyInp(ty,va,fun,ans,exp):
    print('your '+str(ty)+' input for '+str(va)+' in function '+str(fun)+'; '+str(ans)+' was denied for '+exp)
def verify(ty,va,fun,ans):
    return find.boolAsk('your '+str(ty)+' input for '+str(va)+' in functin '+str(fun)+' is '+str(ans)+' that ok?')
def askInput(ty,va,fun):
    return input('please input '+str(ty)+' for variable '+str(va)+' in function'+str(fun)+':')
def askBool(ty,va,fun):
    return find.boolAsk('please input '+str(ty)+' for variable '+str(va)+' in function'+str(fun)+':')
def inputUint(ty,va,fun):
    while isUint(ty):
        ast = False
        print('input will be multiplied by 10^'+str(int(dec))+' if * is added to the end of the input)')
        ans = askInput(ty,va,fun)
        if ask[-1] == '*':
            ast,ans = True,ans[:-1]
        if f.isInt(ans):
            if ast == True:
                ans = int(float(int(ans))*float(str('1e'+str(int(dec)))))
            if verify(ty,va,fun,ans):
                ifVarisLsApp(ans)
                return
def ifVarisLsApp(x):
    if type(varis['inputs']['inpCurr'][-1]) is list:
        varis['inputs']['inpCurr'][-1].append(x)
    else:
        varis['inputs']['inpCurr'][-1] = x
def inputAddress(ty,va,fun):
    while isAddress(ty):
        ans = grab.tryCheckSum(str(askInput(ty,va,fun)))
        if ans != False:
            if verify(ty,va,fun,ans) == True:
                ifVarisLsApp(ans)
                return 
        else:
            denyInp(ty,va,fun,ans,' bad checksum address')
def inputBool(ty,va,fun):
    while isBool(ty):
        ans = askBool(ty,va,fun)
        if verify(ty,va,fun,ans):
            if ans == True:
                ifVarisLsApp(ans)
            else:
                ifVarisLsApp(ans)
            return
def inputString(ty,va,fun):
    while isString(ty):
        ans = str(askInput(ty,va,fun))
        if verify(ty,va,fun,ans) == True:
            ifVarisLsApp(ans)
            return
def inputBytes(ty,va,fun):
    while isBytes(ty):
        ans = str(askInput(ty,va,fun))
        if verify(ty,va,fun,ans) == True:
            ifVarisLsApp(ans)
            return
def askAll(ty,va,fun):
    varis['inputs']['typeCurr'].append([ty,va,fun])
    varis['inputs']['inpCurr'].append(ty)
    deff = True
    tyAc,tot,cou = isList(ty)
    if type(ty) is list:
        if tot == '*':
            tot,deff = indetLoop(ty,cou)
        else:
            print('input requres list of a length '+str(tot)+'; the input request will repeat '+str(tot)+' times')
    while cou < tot:
        inputAddress(ty,va,fun)
        inputBool(ty,va,fun)
        inputString(ty,va,fun)
        inputBytes(ty,va,fun)
        cou += 1
        listLoop(cou,tot)
        if deff == False:
            tot = indetLoop(ty,cou)
def ifInput(js):
    lsType = ['address','uint','bool','bytes','string']
    if 'inputs' in js:
        input(js)
        inps = js['inputs']
        for i in range(0,len(inps)):
            if ' ' in inps[i]:
                askAll(inps[i].split(' ')[0],inps[i].split(' ')[-1],js['name'])
            else:
                 askAll(inps[i],inps[i],js['name']) 
def createInp(x):
    scanner_url = print_scan()
    ask = askGets()
    varis['inputs'] = {'typeCurr':[],'inpCurr':[],'funJS':[]}
    varis['inputs']['funJS'].append(f.jsIt(f.reader('allwallvar.json'))['function'][ask.split('(')[0]])
    if 'name' not in varis['inputs']['funJS'][-1]:
        varis['inputs']['funJS'][-1]['name'] = ask.split('(')[0]
    ifInput(varis['inputs']['funJS'][-1])
    og = varis['inputs']['funJS'][-1]['name']+'('+str(varis['inputs']['inpCurr'])[1:-1]+')'
    f.pen('import sys\nimport currFun.funcSheet as funs\nsys.path.insert(0, "'+str(home)+'")\nimport functions as f\ndef pen(paper, place):\n\twith open(place, "w") as f:\n\t\tf.write(str(paper))\n\t\tf.close()\n\t\treturn\ntxt = None\ninp = "'+str(og).split('(')[1].split(')')[0]+'"\nif inp == "":\n\tfuns.'+og+'\n\tpen(txt,"answer.txt")\nelse:\n\task = input("did you want to send this? '+str(og).split('(')[0]+','+str(og).split('(')[1].split(')')[0]+'?")\n\tif str(ask).lower() != "n" and str(ask).lower() != "no":\n\t\ttxt = str(funs.'+og+')\n\t\tpen(txt,"answer.txt")','currFun/do_it.py')
    import currFun.do_it as do 
    ans = f.reader('answer.txt')
    if str(ans) != 'None' and type(bool(ans)) is not bool:
        send_it(ans)
        tx = json.loads(str(do.txt).replace("'",'"'))
        tx["nonce"] = w3.eth.getTransactionCount(f.check_sum(tx['from']))
        signed_tx = w3.eth.account.sign_transaction(tx, key.p)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        p = subprocess.Popen(["firefox", str(scanner_url)+'/tx/'+str(tx_hash.hex())])
        get_hash(str(tx_hash.hex()))
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
def checkVarFold():
    varis = {'adds': {'all': []}, 'networks': []}
    varis['adds'] = {}
    varis['adds']['all'] = []
    varis['networks'] = listFolds('variables')
    varis = createJsLs(varis['networks'],varis)
    for i in range(0,len(varis['networks'])):
        fold = f.crPa(['variables',varis['networks'][i]])
        currFolds = listFolds(fold)
        varis[varis['networks'][i]] = {}
        varis[varis['networks'][i]]['adds'] = []
        currNet = varis['networks'][i]
        for k in range(0,len(currFolds)):
            path = crPa(fold,currFolds[k])
            if False not in [f.exists(crPa(path,'funcSheet.py')),f.exists(crPa(path,'info.json')),f.exists(crPa(path,'allCalls.json')),f.exists(crPa(path,'ABI.json'))]:
              varis['adds']['all'].append(currFolds[k])
              varis[varis['networks'][i]]['adds'].append(currFolds[k])
    f.pen(varis,f.crPa(['variables','varis.json']))
    return varis
def copyAndStart(path):
        f.copyIt(crPa(path,'funcSheet.py'),'currFun')
        f.copyIt(crPa(path,'info.json'),'currFun')
        f.copyIt(crPa(path,'allCalls.json'),'currFun')
        f.copyIt(crPa(path,'ABI.json'),'currFun')
        allCalls = f.jsIt(f.reader(crPa('currFun','allCalls.json')))
        import currFun.funcSheet as func
        if find.boolAsk('would you like to view all viewable variables in the contract?'):
            func.view_all()
        ex = createInp(allCalls['call'])
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
   return askAbi(js)
def crPa(x,y):
   return f.crPa([x,y])
def checkCurrAbis():
   if len(varis['adds']['all']) == 0:
      copyAndStart(chooseAbi())
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
   copyAndStart(crPa('variables',crPa(net,askNetAbi(net))))
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
while True:
  checkCurrAbis()
  checkIfCurrInfoExists()
  otherStart()


