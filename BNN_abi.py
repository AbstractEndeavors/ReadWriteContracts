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
def make_all_sheets():
        f.pen(f.check_sum(add),'curr_adds.txt')
        abi = exists_make(get_abi(),'abi_fold/'+str(add)+'.json')
        fun.go(add,abi)
        funs,asks,call,fun_all,fun_sheet = parse.parse_it(fun.add)
        f.pen(fun_sheet,'functions_fold/'+str(fun.add)+'.py')
def make_fun_sheets():
        funs,asks,call,fun_all,fun_sheet = parse.parse_it(add)
        return fun_sheet
def make_all_abi():
        abi_file = 'abi_fold/'+str(add)+'.json'
        x = get_abi()
        f.pen(x,'abi.txt')
        return f.jsIt(x)
def make_abi():
    file = 'abi_fold/'+str(add)+'.json'
    get = get_abi()
    f.pen(get,file)
    #make_fun_sheets()
def print_scan():
    info = f.jsIt(f.reader(crPa('currFun','info.json')))
    print(info)
    li = info['scanner']
    if 'api-' in info['scanner']:
        li = info['scanner'].split('api.'.replace('.','-'))[1]
    print('https://'+li+'/address/'+str(info['add']))
    clipboard.copy('https://'+li+'/address/'+str(info['add']))
    return 'https://'+li
def get_hash(x):
    spl = 'api.'
    if 'api-' in scanners:
        li = scanners.split(spl.replace('.','-'))[1]
    print('https://'+li+'/tx/'+str(x))
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
    print(hx(tx_hash))
def find_it(x,k):
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
        infos = ['network','chainId','RPC','explorer','scanner','w3','source']
        for i in range(0,len(infos)-2):
                js[infos[i]] = info[i]
        
        f.pen(info[-1][0]['SourceCode'],f.crPa([fold,'SourceCode.json']))
        f.pen(info[-1][0]['ABI'],f.crPa([fold,'ABI.json']))
        
        f.pen(js,crPa(fold,'info.json'))
        info = parse.parse_it(add,fold)
        infos = ['funs','asks','call','funAll','funSheet']
        input(infos)
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
                add = grab.tryCheckSum(input('please enter an address for the contract youd like to pull'))
                if add != False:
                        info = grab.getSource(add)
                        if 'ContractName' in info[-1][0]:
                                if find.boolAsk('is contract '+str(add)+' associated with the name '+str(info[-1][0]['ContractName'])+'?') == True:
                                        return info,add,info[-1][0]['ContractName']
                print('looks like '+str(add)+' was not a valid address, the checksum didnt verify, we will let you know if it is or isnt on the network once we get a valid address') 
def createAbi(x):
    go = 2
    while go == 2:
        if len(varis['names']) == 0:
                chooseAbi()
        js = {'calls':[['to choose new network','to change network','add another contract','add switch contract','to change wallets','to switch wallets']['newNetwork','changeNet','newCont','changeCont','switchWaLL','newWall']],'asks':[varis['names'],varis['names']],'inquiry':['which contract would you like to use?']}
        ask = f.createAsk(js)
        if str(ask) == '0':
            return 'exit'
        if str(ask) == '1':
            return 'new'
        if str(ask) == '2':
            envs = 'main','poor','tester','migrate'
            for i in range(0,len(envs)):
                n = n + str(alph[i])+') '+str(envs[i])+'\n'
            ask_env = input(n)
            k_env = int(find_it(alph,str(ask_env)))
            f.pen('.env_'+envs[k_env],'new_key.txt')
            global key
            import p_k as key
            go = 2
        else:
            go = 1
    
    k = varis['adds'][int(find_it(alph,str(ask)))]
    return k
def go():
        expo = float(1e-18)
        exi = createAbi(varis['network'])
        print(exi,varis['names'])
        if str(exi) == 'exit':
            return
        if str(exi) != 'new':
            global add,dec 
            name = name_ls[exi]
            add = f.check_sum(str(add_js[name]))
            dec = decimal()
            try:
                f.make_dir('functions_fold/'+str(name))
            except:
                print()
            path = 'functions_fold/'+str(name)+'/'
            fun_file = 'functions_fold/'+str(add)+'.py'
            fun_og_file = 'functions_fold/'+str(name)+'/'+str(add)+'.py'
            fun_ab_file = 'functions_fold/'+str(name)+'/abi_funs.py'
            abi_file = 'abi_fold/'+str(add)+'.json'
            print(fun_ab_file)
            
            #f.pen(abi_file,'functions_fold/'+str(name)+'/'+str(add)+'.json')
            fun = f.readerC(fun_file)
            abi = f.readerC(abi_file)
            funs,asks,call,fun_all,fun_sheet = parse.parse_it(add)
            abi = f.readerC(abi_file)
            func = f.readerC(fun_file)
            f.pen(fun_sheet,'abi_funs.py')
            f.pen(fun_sheet,'functions_fold/'+str(add)+'.py')
            f.pen(fun_sheet,'functions_fold/'+str(name)+'/abi_funs.py')
            f.pen(fun_sheet,'functions_fold/'+str(name)+'/'+str(add)+'.py')
            f.pen('import functions_fold.'+str(name)+'.abi_funs as funies','abi_funs.py')
            f.copy_it(fun_ab_file,os.getcwd(),'abi_funs.py')
            import abi_funs as a_fun
            a_fun.view_all()
            if str(exi) == 'exit':
                exit()
            if str(exi) != 'new':
                scanner_url = print_scan()
                abi = make_all_abi()
                account_1 = w3.eth.account.privateKeyToAccount(key.p)
                cont = w3.eth.contract(add,abi = abi)
                dec = decimal()
                
                ex = ''
                while ex != 'exit':
                    ex = input('would you like to view all viewable variables in the contract?')
                    if str(ex).lower() != 'n' and str(ex).lower() != 'no':
                            a_fun.view_all()
                    f.pen(fun_sheet,fun_file)
                    ex = createInp(call)
def createInp(x):
   
    scanner_url = print_scan()
    calls = f.jsIt(f.reader(crPa('currFun','allCalls.json')))
    input(calls)
    js = {'calls':[['to choose new contract'],['new cont']],'asks':calls['asks'],'inquiry':['which function would you like to use?']}
    ask = find.createAsk(js)
    #for i in range(0,len(x)):
    #    if 'funs.' not in x[i]:
    #        js['asks'].append('funs.'+x[i])
    #ask = find.createAsk(js)
    if str(ask) == '0':
        return 'exit'
    k = int(find_it(alph,str(ask)))
    print('going')
    
    if '()' not in str(x[k]):
        og = x[k].split('(')[0]+'('
        print(og)
        n = x[k].split('(')[1].split(')')[0].split(',')
        if type(n) is not list:
            n = [n]
        inp = []
        print('inputs for '+str(x[k].split('funs.')[1]))
        for i in range(0,len(n)):
            n_a = n[i]
            ad = ''
            n_d = n[i].split('_')[0]
            n_z  = n[i].split('_')[1]
            if n[i].split('_')[0][-2:] == 'ls':
                ad = ' as list'
                n_d = n[i].split('_')[0][:-2]
                n_a = n_a.replace(n[i].split('_')[0]+'_',n[i].split('_')[0][:-2]+'_')
            if 'address' in n_d:
                ask = input(' please input '+str(n_a)+ad)
                nn = f.check_sum(str(ask))
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
            inp.append(nn)
        og = og +str(inp)[1:-1]+')'
    else:
        og = str(x[k])
    f.pen('import abi_funs as funs\nimport functions as f\ndef pen(paper, place):\n\twith open(place, "w") as f:\n\t\tf.write(str(paper))\n\t\tf.close()\n\t\treturn\ntxt = None\ninp = "'+str(og).split('(')[1].split(')')[0]+'"\nif inp == "":\n\t'+og+'\n\tpen(txt,"answer.txt")\nelse:\n\task = input("did you want to send this? '+str(og).split('(')[0]+','+str(og).split('(')[1].split(')')[0]+'?")\n\tif str(ask).lower() != "n" and str(ask).lower() != "no":\n\t\ttxt = str('+og+')\n\t\tpen(txt,"answer.txt")','do_it.py')
    import do_it as do 
    ans = f.reader('answer.txt')
    print('going')
    print(k)
    if str(ans) != 'None':
        send_it(ans)
        print('going')
        tx = json.loads(str(do.txt).replace("'",'"'))
        tx["nonce"] = w3.eth.getTransactionCount(f.check_sum(tx['from']))
        signed_tx = w3.eth.account.sign_transaction(tx, key.p)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print('going')
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
    js = {}
    js['networks'] = listFolds('variables')
    js = createJsLs(js['networks'],js)
    for i in range(0,len(js['networks'])):
        fold = f.crPa(['variables',js['networks'][i]])
        js[js['networks'][i]] = listFolds(fold)
    f.pen(js,f.crPa(['variables','varis.json']))
    return js
def copyAndStart(path):
        f.copyIt(crPa(path,'funcSheet.py'),'currFun')
        f.copyIt(crPa(path,'info.json'),'currFun')
        f.copyIt(crPa(path,'allCalls.json'),'currFun')
        f.copyIt(crPa(path,'ABI.json'),'currFun')
        input(f.reader(crPa('currFun','allCalls.json')))
        allCalls = f.jsIt(f.reader(crPa('currFun','allCalls.json')))
        input('star')
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
   w3.eth.account.privateKeyToAccount(priv.getKey(x))
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
def askAbi(js):
   wallJs = f.existsMake({'types':['main','poor','tester','migrate'],'names':[],'adds':{'adds':[]},'main':{'names':[]},'poor':{'names':[]},'tester':{'names':[]},'migrate':{'names':[]}},'walls/wallsJs.json')
   while True:
     js = {'calls':[['exit','to choose new network','to change network','add another contract','add switch contract','to add new wallet wallets','to switch wallets'],['exit','newNetwork','changeNet','newCont','changeCont','switchWaLL','newWall']],'asks':[varis['networks'],varis['networks']],'inquiry':['which contract would you like to use?']}
     ask = find.createAsk(js)
     input(ask)
     if str(ask) == 'newNetwork':
         return getContLoop()
     if str(ask) == 'changeNet':
         return otherStart()
     if str(ask) == 'exit':
         exit()
     if str(ask) == 'newCont':
         return chooseAbi()
     if str(ask) == 'changeCont':
         otherStart()
         return 
     if str(ask) == 'newWall':
        getWallName(wallJs)
     if str(ask) == 'switchWaLL':
         chooseExistingWallet()
     return ask
def askAdd():
   checkVarFold()
   varis = f.existsMakeJs({'networks':[]},'variables/varis.json')
   js = {'calls':[['to choose new contract'],['newCont']],'asks':[varis['networks'],varis['networks']],'inquiry':['looks like you have prior contracts on the folowing networks:']}
   return askAbi(js)
def crPa(x,y):
   return f.crPa([x,y])
def checkCurrAbis():
   if len(varis['networks']) == 0:
      #js = {'calls':[],'asks':['choose new contract'],'inquiry':['looks like there are no prior abis found:']}
      copyAndStart(chooseAbi())
def checkIfCurrInfoExists():
   if f.exists(crPa('current','info.json')):
      curr = json.loads(f.reader(currPa('current','info.json')).replace("'",'"'))
      if 'path' in curr:
         if false not in [f.exists(crPa(curr['path'],'funcSheet.py')),f.exists(crPa(curr['path'],'info.json')),f.exists(crPa(curr['path'],'allCalls.json')),f.exists(crPa(curr['path'],'ABI.json'))]:
            if 'add' in curr:
               if find.boolAsk('looks like the last used address is '+curr['add']+', associated with the name '+curr['name']+' on the '+curr['network']+' network using RPC address '+curr['RPC']+' did you want to use this one?'):
                    copyAndStart(curr['path'])    
def otherStart():
  net = askAdd()
  path = f.crPa(['variables',net])
  if str(net) in varis:
      js = {'calls':[['to choose new contract'],['newCont']],'asks':[varis[str(net)],varis[str(net)]],'inquiry':['please choose a contract:']}
      copyAndStart(crPa(path,askAbi(js)))
global home,slash,varis
home,slash = f.homeIt()
f.mkDirLs(['currFun'])
f.mkDirLs(['variables'])
f.mkDirLs(['walls'])
varis = checkVarFold()
while True:
  path = 'variables'
  checkCurrAbis()
  varis = checkVarFold()
  checkIfCurrInfoExists()
  otherStart()



