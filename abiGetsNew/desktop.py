import PySimpleGUI as sg
import windowRuns
import sys
import grabApi
import functions as fun
import guiFunctions as guiFun
import json
import os
from datetime import datetime
from hexbytes import HexBytes
from web3 import Web3
import webbrowser

def read_hex(hb):
    h = "".join(["{:02X}".format(b) for b in hb])
    return h
def getDateTime():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
def changeGlob(x,y):
    globals()[x] = y
    return y
def homeIt():
    changeGlob('home',os.getcwd())
    if changeGlob('slash','/') not in home:
        changeGlob('slash','\\')
    return home,slash
def addressVerify(va,y):
    return tryCheckSum(str(y))
def uintVerify(va,y):
    return f.isInt(y)
def checkSum(x):
        return w3.toChecksumAddress(x)
def tryCheckSum(add,x):
    try:
        y = Web3(Web3.HTTPProvider(findLsJsSpec(getInfos(),'add',add,'RPC'))).toChecksumAddress(str(x))
        return y
    except:
        return False
def isLs(ls):
    if type(ls) is list:
        return True
    return False
def isUintSt(x):
    if x[:len('uint')] == 'uint' and str(x).lower() in ['uint8','uint16','uint32','uint64','uint128','uint256']:
        return True
    return False
def isIntSt(x):
    if x[:len('int')] == 'int' and str(x).lower() in ['int8','int16','int32','int64','int128','int256']:
        return True
    return False
def isInt(x):
  if type(x) is int:
    return True
  return False
def checkBool(x):
  if str(x).lower() in ['true','t','0','yes','y']:
    return 'True'
  elif str(x).lower() in ['false','f','1','no','n']:
      return 'False'
  return False
def lsNum():
    return str('1,2,3,4,5,6,7,8,9,0').split(',')
def isNum(x):
    if isInt(x):
        return True
    for k in range(0,len(str(x))):
        if str(x)[k] not in lsNum():
            return False
    return True
def denyInp(ty,va,fun,ans,exp):
    return 'your '+str(ty)+' input of '+str(ans)+' for variable '+str(va)+' in function '+str(fun)+' was denied for '+exp
def verify(ty,va,fun,ans):
    return specificverifyInput(ty,va,ty,ans,fun,'your '+str(ty)+' input for '+str(va)+' in functin '+str(fun)+' is '+str(ans)+' that ok?')
#Int8 — [-128 : 127]
#Int16 — [-32768 : 32767]
#Int32 — [-2147483648 : 2147483647]
#Int64 — [-9223372036854775808 : 9223372036854775807]
#Int128 — [-170141183460469231731687303715884105728 : 170141183460469231731687303715884105727]
#Int256 — [-57896044618658097711785492504343953926634992332820282019728792003956564819968 : 57896044618658097711785492504343953926634992332820282019728792003956564819967]#


#UInt8 — [0 : 255]
#UInt16 — [0 : 65535]
#UInt32 — [0 : 4294967295]
#UInt64 — [0 : 18446744073709551615]
#UInt128 — [0 : 340282366920938463463374607431768211455]
#UInt256 — [0 : 115792089237316195423570985008687907853269984665640564039457584007913129639935]
def ifVarisLsApp(x):
    if type(varis['inputs']['inpCurr'][-1]) is list:
        varis['inputs']['inpCurr'][-1].append(x)
    else:
        varis['inputs']['inpCurr'][-1] = x
def inputAddress(window,values,key,ty,va,func):
    vals,isLs,n = values[key],False,''
    if ty[-len('ls'):] == 'ls':
        isLs = True
        vals = str(vals).split(',')
    vals = fun.mkLs(vals)
    for k in range(0,len(vals)):
        val = vals[k]
        if 'address' in ty:
            ans = tryCheckSum(values['addressChooseLs'],val)
            if ans == False:
                window[key+'__exp'].update(value=denyInp(ty,va,func,val,' bad checksum address'))
                window[key+'__verified'].update(value=False)
                return
            n = n + str(ans)+','
        elif 'uint' in ty:
            ans = isNum(val)
            if ans == False:
                window[key+'__exp'].update(value=denyInp(ty,va,func,val,' is not an integer'))
                window[key+'__verified'].update(value=False)
                return
        elif 'bool' in ty:
            ans = checkBool(val)
            if ans == False:
                window[key+'__exp'].update(value=denyInp(ty,va,func,val,' is not an bool'))
                window[key+'__verified'].update(value=False)
                return
            n = n + str(ans)+','
    if n != '':
        window[key].update(value=n[:-1])
    window[key+'__verified'].update(value=True)
    window[key+'__exp'].update(value='good to go')
    return 
def getDeffs(x,y):
  getDeffs(x,y)
  if y == None:
    return globals()[x]()
  return globals()[x](y)
def doFuncs(function):
  getDeffs('view_all',None)
  funName = function.split('(')[0]
  if function[-len('()'):] == '()':
    return getDeffs(funName,None)
  inps = mkLs(getDefVaris(funName))
  js = {'inputs':[],'name':[]}
  for i in range(0,len(inps)):
          spl = inps[i].split('__')
          js['inputs'].append(spl[0])
          if isLs(spl):
            if len(spl)>1:
              js['name'].append(spl[1])
  ifInput(js)
  send_it(getDeffs(funName,varis['inputs']['inpCurr']))
  return 
def getAskList(nets):
    return [[sg.Text('functions:'),sg.Text(nets, key='functions',default_value=nets[0]), sg.Push()],[sg.OK('OK'),sg.Button('Show'),sg.Button('Exit')]]
def ProgressBar():
    from rpcListNew import rpcs as rpcLs
    return [[sg.Frame('scan progress',[[sg.Text('',key='progTitle')],[guiFun.ProgressBar({'val':100, "orientation":'h', "size":(len(rpcLs),20), "key":'progressbar',"enable_events":True,"bar_color":theme_dict['PROGRESS']})],[sg.Cancel()]], size=(920, 100), pad=((20,20), (20, 10)),  expand_x=True,  relief=sg.RELIEF_GROOVE, border_width=3)]]
def getInfos():
    path,ls = 'infos',[]
    adds = fun.lsDir(path)
    for k in range(0,len(adds)):
        add = adds[k]
        path = 'infos'
        ls.append({'add':add,'network':'','net':'','name':'','chainId':'','path':'','folders':[]})
        path = fun.crPa(path,add)
        netNames = fun.lsDir(path)
        for i in range(0,len(netNames)):
            netName = netNames[i]
            ls[-1]['network']=netName
            path = fun.crPa(path,netName)
            nets = fun.lsDir(path)
            for c in range(0,len(nets)):
                net = nets[c]
                ls[-1]['net']=net
                path = fun.crPa(path,net)
                ls[-1]['path']=path
                ls[-1]['folds']=fun.lsDir(path)
                ls[-1]['blockExplorer'] = json.loads(fun.reader(fun.crPa(path,'info.json')))['rpc']['blockExplorer']
                ls[-1]['RPC'] = json.loads(fun.reader(fun.crPa(path,'info.json')))['rpc']
                ls[-1]['RPCLink'] = json.loads(fun.reader(fun.crPa(path,'info.json')))['rpc']['RPC']
                ls[-1]['chainId'] = json.loads(fun.reader(fun.crPa(path,'info.json')))['rpc']['chainId']
                ls[-1]['ContractName'] = json.loads(fun.reader(fun.crPa(path,'info.json')))['source']['ContractName']
    return ls
def startCont(path):
    sys.path.insert(0, path)
    import dothefunx
    dothefunx.windowDesk = windowDesk
    dotheFunx.startIt()
    sys.path.insert(0, home)
def remFroLs(ls,x):
    lsN = []
    for k in range(0,len(ls)):
        if ls[i] != x:
            lsN.append(ls[i])
    return lsN
def remLsFroLs(ls,ls2):
    lsN = []
    for k in range(0,len(ls)):
        if ls[k] not in ls2:
            lsN.append(ls[k])
    return lsN
def crPaAll(ls):
    pa = fun.crPa(ls[0],ls[1])
    for k in range(2,len(ls)):
        pa = fun.crPa(pa,ls[k])
    return pa
def updateChoose(window,values,add):
    stLs = ['network','net','ContractName','path']
    lsAdd =  getAllSt(getInfos(),'add')
    window['addressChooseLs'].update(values=lsAdd)
    window['addressChooseLs'].update(value=add)
    for k in range(0,len(stLs)):
        window[stLs[k]+'ChooseLs'].update(values=findLsJsSpec(getInfos(),'add',add,stLs[k]))
        window[stLs[k]+'ChooseLs'].update(value=findLsJsSpec(getInfos(),'add',add,stLs[k])[0])
def mkTxnLink(add,st,x):
    return crPaAll([findLsJsSpec(getInfos(),'add',add,'blockExplorer'),st,x])
def getC(k,n):
    if k != 0:
        return n
    return ''
def displayAllRpc(js):
    ls,n = ['netName','ContractName','net','network','chainId','RPCLink',],''
    for k in range(0,len(ls)):
        if ls[k] in js:
            get = js[ls[k]]
            n = n + getC(k,' - ')+str(get)
    return n
def displayAllRpcLs(ls):
    n = ''
    for k in range(0,len(ls)):
        n = n + displayAllRpc(ls[k])+'\n'
    return n
def displayAllLs(ls):
    n = ''
    for k in range(0,len(ls)):
        n = n + displayAllRpc(ls[k])+'\n'
    return n
def displayAllLsI(ls,ls2):
    n = ''
    for k in range(0,len(ls)):
        n = n + ls2[int(ls[k])]+'\n'
    return n
def updateProgBar(window,val,k):
    progress_bar = window['progressbar']
    progress_bar.UpdateBar(k)
    keys = fun.getKeys(val)
    window['progTitle'].update(value=val)
def findItI(ls,x):
    for k in range(0,len(ls)):
        if ls[k] == x:
            return k
def findAllI(ls,x):
    lsN = []
    for k in range(0,len(ls)):
        if ls[k] == x:
            lsN.append(k)
    return lsN
def getRpcProgress(rpcLs,prev,window,add):
    for k in range(0,len(rpcLs)):
      if len(remLsFroLs(getInfos(),prev)) >0:
          found = guiFun.yNPopUp(displayAllLs(remLsFroLs(getInfos(),prev)))
          if found == 'Yes':
              return 
          if found == 'No':
              prev.append(displayAllRpc(remLsFroLs(getInfos(),prev)))
      updateProgBar(window,'scanning: '+str(displayAllRpc(rpcLs[k]))+'\nfound: '+str(len(remLsFroLs(getInfos(),prev)))+' new contracts'+'\n'+displayAllLs(remLsFroLs(getInfos(),prev)),getUpdateTick(k,len(rpcLs)))
      grabApi.deriveAnyInfo(add,k)
    return
def getGasEvents(js):
    ls = ['Link','gasSpeed','intrinsicGas']
    for k in range(0,len(ls)):
        js[ls[k]+'__event'] = js['contract']+'__'+js['function']+'__'+ls[k]
        if  js[ls[k]+'__event'] in js['values']:
            js[ls[k]] = js['values'][js[ls[k]+'__event']]
    return js
def addToJs(js,st,x):
    js[st] = x
    return js
def widowMain(window):
      while True:
        global allTabs
        event, values = window.read()
        window.Refresh()
        jsVars= {}
        jsVars = addToJs(jsVars,'add',values['addressChooseLs'])
        jsVars = addToJs(jsVars,'gasSpeed','fastest')
        jsVars = addToJs(jsVars,'values',values)
        jsVars = addToJs(jsVars,'valKeys',fun.getKeys(values))
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            break
        elif '__input__' in event:
            spl = event.split('__')
            inputAddress(window,values,event,spl[3],spl[4],spl[2])
        elif event == 'Submit':
            window['output'].update(value='')
            contract = values['group_contracts'].split('tab__')[-1]
            function = values[contract+'__functions'].split('tab__'+contract+'__')[-1]
            jsVars = addToJs(jsVars,'contract',contract)
            jsVars = addToJs(jsVars,'function',function)
            jsVars = addToJs(jsVars,'varPref',contract+'__input__'+function)
            jsVars = addToJs(jsVars,'contFun',contract+'__'+function)
            jsVars = addToJs(jsVars,'inputs',None)
            jsVars = getGasEvents(jsVars)
            if jsVars['function'] == 'viewOnly':
                getDeffsImp(jsVars['gasSpeed'],jsVars['add'],values[jsVars['contFun']],jsVars['inputs'])
            else:
                lsEvent = ['verified','Link','TXN','exp','verified','inputs']
                for k in range(0,len(lsEvent)):
                    jsVars = addToJs(jsVars,lsEvent[k],[])
                for k in range(0,len(jsVars['valKeys'])):
                    if jsVars['varPref'] in jsVars['valKeys'][k]:
                        lsFound = ['inputs',jsVars['valKeys'][k]]
                        for j in range(0,len(lsEvent)):
                            if jsVars['valKeys'][k][-len('__'+lsEvent[j]):] == '__'+lsEvent[j]:
                                lsFound = [lsEvent[j],jsVars['valKeys'][k]]
                        jsVars[lsFound[0]].append(values[lsFound[1]])
                if False not in jsVars['verified']:
                    ans = getDeffsImp(jsVars['gasSpeed'],jsVars['add'],jsVars['function'],cleanLs(jsVars['inputs']))
                    if ans is not None:
                        if jsVars['intrinsicGas'] != 'default':
                            ans['gas'] = int(values[jsVars['intrinsicGas']])
                        ans['gas'] = ans['gas']*10
                        sent = getSendIt(jsVars['add'],ans)
                        if sent is not None:
                            print(read_hex(sent))
                            window[jsVars['Link'+'__event']].update(value=mkTxnLink(jsVars['add'],'tx','0x'+str(read_hex(sent))))
                else:
                    print('you have unverified inputs:\n'+displayAllLsI(findAllI(jsVars['verified'],False),jsVars['exp']))
                    
        elif '_TXN' in event:
            webbrowser.open(values[event.replace('__TXN','__Link')])
        elif event == 'addTab':
            window['group_contracts'].add_tab()
        elif event == 'getABI':
            if 'tab__'+findLsJsSpec(getInfos(),'add',jsVars['add'],'ContractName') not in allTabs:
                window['group_contracts'].add_tab(getTabs(window,jsVars['add'],getFuncFuns(jsVars['add'])))
                if 'nullTab' in values:
                    window['nullTab'].update(visible=False)
        if event == 'addressChooseLs':
            updateChoose(window,values,values['addressChooseLs'])
        elif event == 'RUN':
              from rpcListNew import rpcs as rpcLs
              jsVars['add'],prev = values['runAdd'],getInfos()
              getRpcProgress(rpcLs,prev,window,jsVars['add'])
              found = remLsFroLs(getInfos(),prev)
              updateProgBar(window,'done: found '+str(len(found))+'\n'+displayAllRpcLs(found),getUpdateTick(len(rpcLs),len(rpcLs)))
              getInfos()
              updateChoose(window,jsVars['values'],jsVars['add'])
        elif event == 'Edit Me':
              sg.execute_editor(__file__)
        elif event == 'Version':
              sg.popup_scrolled(sg.get_versions(), keep_on_top=True)
        elif event == 'File Location':
              sg.popup_scrolled('This Python file is:', __file__)
        window.refresh()
        #window.close()
def getAllSt(lsJs,st):
    lsN =[]
    for k in range(0,len(lsJs)):
        lsN.append(lsJs[k][st])
    return lsN
def findLsJsSpec(lsJs,st,na,st2):
    for k in range(0,len(lsJs)):
        if lsJs[k][st] == na:
            return lsJs[k][st2]
    return False
def getSheetPath(add):
    return findLsJsSpec(getInfos(),'add',add,'path')
def getFile(st):
    return fun.reader(fun.crPa(findLsJsSpec(getInfos(),'add',getAllSt(getInfos(),'add')[0],'path'),st))
def getDeffsImp(gas,add,x,y):
    sys.path.insert(0, getSheetPath(add))
    import funcSheet
    import importlib
    importlib.reload(funcSheet)
    import funcSheet
    funcSheet.gasSpeed = gas
    funs = funcSheet.getDeffs(x,y)
    sys.path.insert(0, home)
    return funs
def getWall(add):
    sys.path.insert(0, getSheetPath(add))
    import funcSheet
    import importlib
    importlib.reload(funcSheet)
    import funcSheet
    funs = funcSheet.account_1.address
    sys.path.insert(0, home)
    return funs
def getSendIt(add,tx):
    sys.path.insert(0, getSheetPath(add))
    import funcSheet
    import importlib
    importlib.reload(funcSheet)
    import funcSheet
    funs = funcSheet.send_it(tx)
    sys.path.insert(0, home)
    return funs
def getFunVars(x):
    sys.path.insert(0, getSheetPath(x))
    import funcSheet
    import importlib
    importlib.reload(funcSheet)
    import funcSheet
    funs = funcSheet.getDefVaris(x)
    sys.path.insert(0, home)
    return funs
def getFuncFuns(add):
    sys.path.insert(0, getSheetPath(add))
    import funcSheet
    import importlib
    importlib.reload(funcSheet)
    import funcSheet
    funs = funcSheet.getFunList()
    sys.path.insert(0, home)
    return funs
def startCont(path):
    sys.path.insert(0, path)
    import dothefunx
    dotheFunx.startIt()
    sys.path.insert(0, home)
def toggle(val):
    if val == True:
        return False
    return True
def askFunkFuncs():
    return getAskList(getFuncFuns())
def getVarsFroFun(x):
    return fun.mkLs(x.replace(x.split('(')[0]+'(','')[:-1].split(','))
def askInput(ty,va,fun):
    return specificAskInput(ty,va,fun,'please input '+str(ty)+' for variable '+str(va)+' in function'+str(fun)+':')
def askBool(ty,va,fun):
    return specificAskInput(ty,va,fun,'please input '+str(ty)+' for variable '+str(va)+' in function'+str(fun)+':')
def gasSpeedCombo(js):
    gasLs = ['safeLow','average','fast','fastest']
    return sg.Combo(gasLs, key=js['name']+'__'+js['fun']+'__gasSpeed',default_value=gasLs[-2],enable_events=True)
def getIntrinsicGas(js):
    return sg.Input('default',key=js['name']+'__'+js['fun']+'__intrinsicGas',size=(10,1))
def browsButton(js):
    return sg.Button('last TXN',key=js['name']+'__'+js['fun']+'__TXN',enable_events=True)
def getLinkInp(js):
    return sg.Input(mkTxnLink(js['add'],'address',getWall(js['add'])),key=js['name']+'__'+js['fun']+'__Link',disabled=True,size=(len('https://testnet.snowtrace.io/address/0xF52F0fbc9c9FefB846d45c4015f5ee1939b1A9F1'),1))
def mkVisible(window,st,boolIt):
    window[st].update(visible=boolIt)
def cleanLs(ls):
    lsN = []
    for i in range(0,len(ls)):
        if '' != ls[i]:
            lsN.append(ls[i])
    return lsN
def getUpdateTick(curr,max):
    return int(curr*(100/max))
def dispLs(x):
    if str(x)[-len('ls'):] == 'ls':
       x = str(x)[:-len('ls')]+'[]'
    return str(x)
def mkvartQ(window,js):
    dispType = str(js['type'])
    varKey = str(js['name'])+'__'+'input__'+str(js['fun'])+'__'+str(js['type'])+'__'+str(js['var'])
    varVeriKey = varKey+'__verified'
    varExpKey = varKey+'__exp'
    inp = sg.Input('',size = getSize(str(js['type'])), key=varKey,enable_events=True)
    deny = 'your '+str(dispLs(js['type']))+' input of None for '+str(js['var'])+' in function '+str(js['fun'])+' was denied due to no input'
    if 'bool' in js['type']:
        inp = sg.Combo(['True','False'], key=varKey,enable_events=True)
    if str(js['type'])[-len('ls'):] == 'ls':
        inp = guiFun.txtInputs({"title":"","size":getSize(str(js['type'])),"key":varKey,"autoscroll":True,"pad":(0,0),"change_submits":True,"enable_events":True})
    check = guiFun.checkBox({"title":'verified',"visible":True,"key":varVeriKey,"default":False,"pad":(0,0),"disabled":True,})
    exp = sg.Input(deny,key = varExpKey,size=(len('your address input of 0x514910771AF9Ca65af840dff83E8264EcF986CA for spender in function decreaseApproval was denied for  bad checksum address')+5,1),disabled=True)
    return [sg.Frame('',[[sg.Text(str(js['var'])+': ',font='Any 15'),inp,sg.Text(str(dispLs(js['type'])),font='Any 15'),check,exp]],pad=(0, (10, 0)), border_width=0, expand_x=True, expand_y=True, element_justification='v')]
def getTabs(window,add,ls):
    global allTabs
    tabs = []
    name = findLsJsSpec(getInfos(),'add',add,'ContractName')
    lsNoVar = []
    for k in range(0,len(ls)):
        js = {'name':name,'fun':ls[k].split('(')[0],'type':'','var':'','add':add}
        vars = getFunVars(ls[k].split('(')[0])
        if len(vars[0]) != 0:
            tabs.append([[sg.Text("function: "),sg.T(str(ls[k])),sg.Text("TXN speed: "),gasSpeedCombo(js),sg.Text("intrinsic gas: "),getIntrinsicGas(js),sg.Text("last TXN: "),getLinkInp(js),browsButton(js)]])
            for i in range(0,len(vars)):
                spl = cleanLs(fun.mkLs(vars[i].split('__')))
                js['type'] = spl[0]
                if len(spl)>1:
                    js['var'] = spl[1]
                tabs[-1].append(mkvartQ(window,js))
            tabs[-1] = sg.Tab(str(js['fun']),[[sg.Column(tabs[-1],key=name+'__getCol', pad=(0, (10, 0)),  expand_x=True, expand_y=True, grab=True)]],key ='tab__'+name+'__'+str(js['fun']))
        if len(vars[0]) == 0:
            lsNoVar.append(js['fun'])
        updateProgBar(window,'compiling '+str(js['fun'])+'\n'+str(len(tabs))+' out of '+str(len(ls))+'functions',getUpdateTick(k,len(ls)))
    updateProgBar(window,'done \n'+str(len(ls))+' out of '+str(len(ls))+' functions',getUpdateTick(len(ls),len(ls)))
    tabs.append(sg.Tab('viewOnly',[[sg.Column([[sg.Combo(lsNoVar,key=name+'__viewOnly',default_value=lsNoVar[0],enable_events=True)]],key=name+'__getCol', pad=(0, (10, 0)),  expand_x=True, expand_y=True, grab=True)]],key ='tab__'+name+'__viewOnly'))
    allTabs.append('tab__'+name)
    return sg.Tab(name,[[sg.TabGroup([tabs],key=name+"__functions")]],key ='tab__'+name)
def getSize(x):
    if 'uint' in x:
        return (23+5,5)
    if 'bool' in x:
        return (len('true')+5,5)
    if x == 'net':
        return (len('Ethereum')+5,5)
    if x == 'path' or 'bytes' in x:
        return (len('infos/0x710823129ae7ed40a171e922b3928d4a04f30ce9/Avalanche/Testnet')+5,5)
    if x == 'network':
        return (len('TestNet')+5,5)
    return (len('0x710823129ae7ed40a171e922b3928d4a04f30ce9')+5,5)
def getNetDrops(titleLs,stLs):
    lsAdd = getAllSt(getInfos(),'add')
    layout = [[sg.T('Choose Existing')],[sg.T('existing address: '),guiFun.dropDown({"ls":lsAdd,"key":'addressChooseLs',"size":getSize('address'),"default_value":lsAdd[0],"visible":True,"enable_events":True})]] 
    for k in range(0,len(titleLs)):
        ls = findLsJsSpec(getInfos(),'add',lsAdd[0],stLs[k])
        layout.append([sg.T(titleLs[k]+': '),guiFun.dropDown({"ls":ls,"key":stLs[k]+'ChooseLs',"size":getSize(stLs[k]),"default_value":ls,"visible":True,"enable_events":True})])
    lsButtons = [[sg.Button('getABI',key='getABI',enable_events=True)]]
    for k in range(0,len(lsButtons)):
        layout.append(lsButtons[k])
    return layout
def mkBlanks(titleLs,stLs):
    lsAdd = ['None']
    layout = [[sg.T('existing address: '),guiFun.dropDown({"ls":lsAdd,"key":'addressChooseLs',"size":getSize('address'),"default_value":lsAdd[0],"visible":True,"enable_events":True})]] 
    for k in range(0,len(titleLs)):
        ls = ['None']
        layout.append([sg.T(titleLs[k]+': '),guiFun.dropDown({"ls":ls,"key":stLs[k]+'ChooseLs',"size":getSize(stLs[k]),"default_value":ls,"visible":True,"enable_events":True})])
    lsButtons = [[sg.Button('getABI',key='getABI',enable_events=True)],[sg.Text('derive Source From Address', font='Any 20')],[sg.Input('',key='runAdd'), sg.Text('input contract address')],[sg.T('searches All Networks')],[sg.Button('RUN'), sg.Button('checkSum')]]
    for k in range(0,len(lsButtons)):
        layout.append(lsButtons[k])
    return layout
def blockDefaults():
    tabLay = [[sg.Tab('x',[[sg.T('enter a contract address below')]],key ='nullTab',visible=True)]]
    nets = mkBlanks(['network','network Name','contract Name','path'],['network','net','ContractName','path'])
    if len(getInfos()) != 0:
    #    tabLay = [[getTabs(getAllSt(getInfos(),'add')[0],getFuncFuns(getAllSt(getInfos(),'add')[0]))]]
        nets = getNetDrops(['network','network Name','contract Name','path'],['network','net','ContractName','path'])
    top_banner = [[sg.Text('Dashboard', font='Any 20', background_color=jsFormat["DARK_HEADER_COLOR"], enable_events=True, grab=False),sg.Push(background_color=jsFormat["DARK_HEADER_COLOR"]),sg.Text(getDateTime(), font='Any 20', background_color=jsFormat["DARK_HEADER_COLOR"])],]
    top  = [[sg.Push(), sg.Text('Contract Station', font='Any 20'), sg.Push()]]#,[sg.T('input contract address')],[sg.T('start utilizing your Smart Contract')]]
    output = [sg.Frame('', [[sg.T('output')],[sg.Output(size=(100, 10),key='output', font='Courier 10')]], pad=((20,20), (20, 10)),  expand_x=True,  relief=sg.RELIEF_GROOVE, border_width=3)]
    block_1 = [sg.Frame('', [[sg.TabGroup(tabLay,key="group_contracts")],[sg.Button('Submit',key='Submit',visible=True,enable_events=True),sg.Button('verify',key='verify',visible=True,enable_events=True)]], pad=((20,20), (20, 10)),  expand_x=True,  relief=sg.RELIEF_GROOVE, border_width=3)]
    block_2 = [sg.Frame('',nets, pad=((20,20), (20, 10)),  expand_x=True,  relief=sg.RELIEF_GROOVE, border_width=3)]
    get = [sg.Frame('',[[sg.Text('derive Source From Address')],[sg.Input('',key='runAdd'), sg.Text('input contract address')],[sg.T('searches All Networks')],[sg.Button('RUN'), sg.Button('checkSum')]], pad=((20,20), (20, 10)),  expand_x=True,  relief=sg.RELIEF_GROOVE, border_width=3)]
    #derive = [sg.Frame('',[block_2], pad=((20,20), (20, 10)),  expand_x=True,  relief=sg.RELIEF_GROOVE, border_width=3)]
    return [top_banner,top,block_1,output,block_2,ProgressBar(),get]
def desktopTheme(ls):
  sg.theme_add_new('Dashboard', theme_dict)
  sg.theme('Dashboard')
  widowMain(sg.Window('Dashboard PySimpleGUI-Style', blockDefaults(), margins=(0,0), background_color=jsFormat["BORDER_COLOR"],keep_on_top=False, no_titlebar=False, resizable=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_LOC_EXIT)),
def simpleFileOpener():
  fname = ''
  if len(sys.argv) == 1:
      layout = [[sg.Text('Document to open')],[sg.Input(), sg.FileBrowse()],[sg.CloseButton('Open'), sg.CloseButton('Cancel')]]
      window = sg.Window('My Script', layout)
      event, values = window.read()
      window.close()
      fname = values['-FNAME-']
  else:
      fname = sys.argv[1]
  if not fname:
      sg.popup("Cancel", "No filename supplied")
      raise SystemExit("Cancelling: no filename supplied")
#test_menus()
global lsAskGlob,jsFormat,theme_dict,allTabs
allTabs = []
theme_dict = {'BACKGROUND': '#2B475D','TEXT': '#FFFFFF','INPUT': '#F2EFE8','TEXT_INPUT': '#000000','SCROLL': '#F2EFE8','BUTTON': ('#000000', '#C2D4D8'),'PROGRESS': ['#FFFFFF', '#C7D5E0'],'BORDER': 0,'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}
jsFormat = {"BORDER_COLOR":'#C7D5E0',"DARK_HEADER_COLOR":'#1B2838',"BPAD_TOP":((20,20), (20, 10)),"BPAD_LEFT":((20,10), (0, 0)),"BPAD_LEFT_INSIDE":(0, (10, 0)),"BPAD_RIGHT":((10,20), (10, 0))}
lsAskGlob = ''
homeIt()
desktopTheme(blockDefaults())
