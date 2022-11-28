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
    i = 0
    while str(x[i]) != str(k):
        i = i + 1
    return i
def ifSome(x,ls,js):
    if x not in js:
        js[x] = {}
    if len(ls) >0:
        js[x]['keys']=ls
    return js,ls
def keyIt(js,sa):
    if 'keys' in js:
        txt = js['json']
        key = js['keys']
        for i in range(0,len(key)):
            f.pen(txt[key[i]],f.crPa([sa,key[i]+'.json']))
            js[key[i]] = {'json':txt[key[i]],'keys':keys(txt[key[i]])}
        
    return js
def whileKeys(x,sa,start):
    jsOg = {'names':[start],str(start):{'json':x,'keys':keys(x)}}
    jsNew = jsOg[['names'][0]]
    txt =jsOg['json']
    key = jsOg['keys'] 
    for i in range(0,len(key)):
        nKe = key[i]
        jso = txt[nKe]
        f.pen(txt[key[i]],f.crPa([sa,key[i]+'.json']))
        js[key[i]] = {'json':jso[nKe],'keys':keys(jso[nKe])}

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
       
def createInp(x):
    scanner_url = print_scan()
    ask = askGets()
    #for i in range(0,len(x)):
    #    if 'funs.' not in x[i]:
    #        js['asks'].append('funs.'+x[i])
    #ask = find.createAsk(js)
    if '()' not in str(ask):
        lss = []
        og = ask.split('(')[0]+'('
        n = ask.split('(')[1].split(')')[0].split(',')
        for i in range(0,len(n)):
            n_a = n[i]
            ad = ''
            n_d = n[i].split('_')[0]
            n_z  = safeSplit(n[i],'_',1)
            if n_z != None:
                if len(n_z) >= len('ls'):
                    if 'ls' in n_z:
                        if n_z[-2:] == 'ls':
                            ad = ' as list'
                            n_d = safeSplit(n[i],'_',0)[-2:]
                            n_a = n_a.replace(safeSplit(n[i],'_',0)+'_',safeSplit(n[i],'_',0)[-2:]+'_')
            if 'address' in n_d:
                ask = input(' please input '+str(n_a)+ad)
                nn = grab.checkSum(str(ask))
            elif 'uint' in n_d:
                if 'uint256' in n_d and 'blocktime' not in n_z :
                    ok = 'n'
                    while str(ok).lower() == 'n' or str(ok).lower() == 'no':
                        ask = input(' please input '+str(n_a)+ad+' (input will be multiplied by 10^'+str(int(dec))+' if * is added to the end of the input): ')
                        if '*' in str(ask):
                            ask = int(float(int(ask.split('*')[0]))*float(str('1e'+str(int(dec)))))
                        ok = input('your input is '+str(int(ask))+' is that ok?')
                    nn = int(ask) 
                else:
                    ask = input(' please input '+str(n_a)+ad)
                    nn = int(ask)
            elif 'bool' in n_d:
                ask = input(' please input '+str(n_a)+ad)
                if str(ask) == '1':
                    nn = True
                else:
                    nn = False
            else:
                ask = input(' please input '+str(n_a)+ad)
                nn = str(ask)
            if ad != '':
                nn = [nn]
            lss.append(nn)
        og = og +str(lss)[1:-1]+')'
    else:
        og = str(ask)
    f.pen('import sys\nimport currFun.funcSheet as funs\nsys.path.insert(0, "'+str(home)+'")\nimport functions as f\ndef pen(paper, place):\n\twith open(place, "w") as f:\n\t\tf.write(str(paper))\n\t\tf.close()\n\t\treturn\ntxt = None\ninp = "'+str(og).split('(')[1].split(')')[0]+'"\nif inp == "":\n\tfuns.'+og+'\n\tpen(txt,"answer.txt")\nelse:\n\task = input("did you want to send this? '+str(og).split('(')[0]+','+str(og).split('(')[1].split(')')[0]+'?")\n\tif str(ask).lower() != "n" and str(ask).lower() != "no":\n\t\ttxt = str(funs.'+og+')\n\t\tpen(txt,"answer.txt")','currFun/do_it.py')
    import currFun.do_it as do 
    ans = f.reader('answer.txt')
    if str(ans) != 'None':
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
        #account_1 = w3.eth.account.privateKeyToAccount(key.p)
        #cont = w3.eth.contract(ask,abi = abi)
        #dec = decimal()
        ex = ''
        while ex != 'exit':
            ex = input('would you like to view all viewable variables in the contract?')
            if str(ex).lower() != 'n' and str(ex).lower() != 'no':
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
def loadKey(x):
   load_dotenv()
   
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



