import os
import json
def homeIt():
    curr = os.getcwd()
    slash = '//'
    if '//' not in str(curr):
        slash = '/'
    changeGlob('slash',slash)
    changeGlob('home',curr)
    return home,slash
def changeGlob(x,v):
    globals()[x] = v
homeIt()
import sys
sys.path.insert(0, os.getcwd().replace(os.getcwd().split(slash)[-1],''))
import functions as f
import PySimpleGUI as sg
import webbrowser
def simpleBool(ask):
    asky = ''
    layout = [[sg.Text(ask)],
            [sg.Yes(), sg.No()]]
    window = sg.Window('Window Title', layout)
    while asky == '':             
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            asky = False
        window.close()
        asky = True
    window.close()  
    return asky
def ifVarIsNotNone(x):
    if x is not None:
        return True
    return False
def noJsBlank(js,ls):
    for i in range(0,len(ls)):
        lsY = ls[i]
        if ifxInjs(js,lsY):
            if js[lsY] == '':
                return False
    return True
def strWholeLs(ls):
    lsN = []
    for i in range(0,len(ls)):
        lsN.append(str(ls[i]))
    return lsN
def findIt(x,k):
    for i in range(0,len(x)):
        if x[i] == k:
            return i
def jsIt(js):
    return json.loads(str(js).replace("'",'"'))
def ifInLocals(x):
    if x in locals():
        return True
    return False
def loading(meter,i,k,key,msg):
    sg.one_line_progress_meter(meter, i, k-1, key,msg)
def ifLsLenEq1(ls):
    ls = makeLs(ls)
    if len(ls) == 1:
        return True
    return False
def getAllLsJsFromLs(ls,st,js):
    lsN = []
    for i in range(0,len(ls)):
        lsY = ls[i]
        if ifxInjs(js,lsY):
            if ifxInjs(js[lsY],st):
                lsN = combineLsS(js[lsY][st],lsN)
     
    return lsN
def combineLsS(ls,lsN):
    for i in range(0,len(ls)):
        lsY = ls[i]
        if isLs(lsY):
            for k in range(0,len(lsY)):
                lsN.append(lsY[k])
        else:
            lsN.append(lsY)
    return lsN
        
def makeSpaceAroundStr(st,k):
    n = ''
    if isStr(st) == False:
        st = str(st)
        k = k-len(st)
    k2 = makeAnyIntRound(float(k/2))
    for i in range(0,k2):
        n = n + ' '
    return n + st + n
def getHighInLs(ls):
    ls.sort()
    if len(ls)>0:
        return ls[-1]
    return 15
def isFloat(k):
    if type(k) is float:
        return True
def isAnyFloat(k):
    if isFloat(k):
        return True
    if isStr(k) == False:
        k = str(k)
    spl = k.split('.')
    if len(spl) != 2:
        return False
    for i in range(0,len(spl)):
        if ifAllInts(spl[i]) == False:
            return False
    return True
def isInt(k):
    if type(k) is int:
        return True
    return False
def isAnyInt(k):
    if isInt(k):
        return True
    if isStr(k) == False:
        k = str(k)
    spl = k.split('.')
    if isLs(spl) == True:
        if len(spl) == 2:
            for i in range(0,len(spl)):
                if ifAllInts(spl[i]) == False:
                    return False
            return True
    if ifAllInts(spl) == False:
        return False
    return True
def makeAnyInt(k):
    if isAnyInt(k) == False:
        return False
    spl = k.split('.')
    if isLs(spl) == False:
        spl = [spl]
    return int(spl[0])
def makeAnyIntRound(k):
    if isAnyInt(k) == False:
        return False
    if isFloat(k) == True:
        spl = str(k).split('.')
    if isLs(spl) == False:
        spl = [spl]
    if len(spl) == 2:
        if float('0.'+spl[1]) > float(1/2):
            return int(spl[0]) + 1
        return int(spl[0])
    return int(spl[0])
            
    return int(spl[0])
def isLs(ls):
    if type(ls) is list:
        return True
    return False
def makeLs(ls):
    if isLs(ls) == False:
        ls = [ls]
    return ls
def isStr(x):
    if type(x) is str:
        return True
    return False
def ifAllInts(x):
    lsN,ints = [],getAllInts()
    if isStr(x) == False:
        x = str(x)
    for i in range(0,len(x)):
        if x[i] not in ints:
            return False
    return True
def getAllInts():
    return str('0,1,2,3,4,5,6,7,8,9').split(',')         
def LsStrToLsLen(ls):
    lsN = []
    for i in range(0,len(ls)):
        if isStr(ls[i]):
            lsN.append(len(ls[i]))
        elif isAnyInt(ls[i]):
            lsN.append(ls[i])
    return lsN
def getLongest(ls,x):
    return getHighInLs(LsStrToLsLen(getListFroLsJs(ls,x)))
def ifxInjs(js,x):
    if x not in js:
        return False
    return True
def ifJsXEqY(js,x,y):
    if ifxInjs(js,x):
        if js[x] == y:
            return True
    return False
def getLsJsXEqY(ls,x,y):
    lsN=[]
    for i in range(0,len(ls)):
        if ifJsXEqY(ls[i],x,y):
            lsN.append(ls[i])
    return lsN    
def getListFroLsJs(ls,x):
    lsN = []
    for i in range(0,len(ls)):
        print(ls,x)
        if ifxInjs(ls[i],x):
            print(ls[i][x])
            if ifxInjs(lsN,ls[i][x]) == False:
                lsN.append(ls[i][x])
    print(lsN)
    return lsN



def askList(nets):
    allNetNameRpcs = getAllLsJsFromLs(nets['names'],'RPCs',nets)
    selRpc = jsIt(getAllLsJsFromLs(nets['names'],'RPCs',nets))
    lsN = ['nativeCurrency','network','chainId','RPC']
    jsN = {}
    for i in range(0,len(lsN)):
        sel = lsN[i]
        print(jsN)
        nativeCurrAskLs = getListFroLsJs(allNetNameRpcs,sel)
        longNativeCurrAskLs = makeSpaceAroundStr('choose'+sel,getLongest(allNetNameRpcs,sel))
        jsN[sel] = {'ask':nativeCurrAskLs,'len':len(longNativeCurrAskLs)}
    sg.set_options(suppress_raise_key_errors=False, suppress_error_popups=False, suppress_key_guessing=False)
    menu_def = [['File', ['Open', 'Save', 'Exit',]],
                ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
                ['Help', 'About...'],]
    sgTop = [sg.Menu(menu_def)]
    
    sg1 = [sg.Text('Input Verification'),sg.Combo(nets['names'],key='contractName'),sg.Push()]
    sg2 = [sg.Text('network:'),sg.Combo(jsN['network']['ask'], key='network',size=(jsN['network']['len'], 1)), sg.Push()]
    sg3 = [sg.Text('nativeCurrency:'),sg.Combo(jsN['nativeCurrency']['ask'], key='nativeCurrency',size=(jsN['nativeCurrency']['len'], 1)), sg.Push()]
    sg4 = [sg.Text('chainId:'),sg.Combo(jsN['chainId']['ask'], key='chainId',size=(jsN['chainId']['len'], 1)), sg.Push()]
    sg5 = [sg.Text('RPC:'),sg.Combo(jsN['RPC']['ask'],key ='RPC',size=(jsN['RPC']['len'], 1)), sg.Push()]
    sgButtons = [sg.OK('OK'),sg.Button('Show'),sg.Button('Exit')]
    if ifLsLenEq1(nets['names']):
        sg1 = [sg.Text('contractName:'),sg.Input(nets['names'][0], disabled=True, key='contractName')]
    if ifLsLenEq1(jsN['network']['ask']):
        sg2 = [sg.Text('network:'),sg.Input(jsN['network']['ask'][0], disabled=True, key='network')]
    if ifLsLenEq1(jsN['nativeCurrency']['ask']):
        sg3 = [sg.Text('nativeCurrency:'),sg.Input(jsN['nativeCurrency']['ask'][0], disabled=True, key='nativeCurrency')]
    if ifLsLenEq1(jsN['chainId']['ask']):
        sg4 = [sg.Text('chainId:'),sg.Input(jsN['chainId']['ask'][0], disabled=True, key='chainId')]
    if ifLsLenEq1(jsN['RPC']['ask']):
        sg5 = [sg.Text('RPC:'),sg.Input(jsN['RPC']['ask'][0], disabled=True, key='RPC')]
    layout = [sgTop,sg1,sg2,sg3,sg4,sg5,sgButtons]
    window = sg.Window('Window Title', layout, finalize=True)
    while True:             # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Show':
            change = False
            if values['contractName'] !='':
                print(nets[values['contractName']])
                selRpc = jsIt(nets[values['contractName']])
                change = True
            while change == True:
                sellRPCbef = selRpc
                if ifVarIsNotNone(values) == True:
                    if ifxInjs(values,'network'):
                        if values['network'] !='':
                            sg2 = [sg.Text('network:'),sg.Input(values['network'][0], disabled=True, key='network')]
                            selRpc = getLsJsXEqY(selRpc,'network',values['network'])
                elif ifVarIsNotNone(value) ==True:
                    if ifxInjs(value,'network'):
                        if value['network'] !='':
                            sg2 = [sg.Text('network:'),sg.Input(value['network'][0], disabled=True, key='network')]
                            selRpc = getLsJsXEqY(selRpc,'network',value['network'])
                        else:
                            window['network'].update(values=getListFroLsJs(selRpc,'network'))
                if ifVarIsNotNone(values) == True:
                    if ifxInjs(values,'nativeCurrency'):
                        if values['nativeCurrency'] !='':
                            sg3 = [sg.Text('nativeCurrency:'),sg.Input(values['nativeCurrency'][0], disabled=True, key='nativeCurrency')]
                            selRpc = getLsJsXEqY(selRpc,'nativeCurrency',values['nativeCurrency'])
                        else:
                            window['nativeCurrency'].update(values=getListFroLsJs(selRpc,'nativeCurrency'))
                elif ifVarIsNotNone(value) ==True:
                    if ifxInjs(value,'nativeCurrency'):
                        if value['nativeCurrency'] !='':
                            sg3 = [sg.Text('nativeCurrency:'),sg.Input(values['nativeCurrency'][0], disabled=True, key='nativeCurrency')]
                            selRpc = getLsJsXEqY(selRpc,'nativeCurrency',value['nativeCurrency'])
                if ifVarIsNotNone(values) == True:
                    if ifxInjs(values,'chainId'):
                        if values['chainId'] !='':
                            sg4 = [sg.Text('chainId:'),sg.Input(values['chainId'][0], disabled=True, key='chainId')]
                            selRpc = getLsJsXEqY(selRpc,'chainId',values['chainId'])
                        else:
                            window['chainId'].update(values=getListFroLsJs(selRpc,'chainId'))
                elif ifVarIsNotNone(value) ==True:
                    if ifxInjs(value,'chainId'):
                        if value['chainId'] !='':
                            sg4 = [sg.Text('chainId:'),sg.Input(value['chainId'][0], disabled=True, key='chainId')]
                            selRpc = getLsJsXEqY(selRpc,'chainId',value['chainId'])
                if ifVarIsNotNone(values) == True:
                    if ifxInjs(values,'RPC'):
                        if values['RPC'] !='':
                            sg4 = [sg.Text('RPC:'),sg.Input(values['RPC'][0], disabled=True, key='RPC')]
                            selRpc = getLsJsXEqY(selRpc,'RPC',values['RPC'])
                        else:
                            window['RPC'].update(values=getListFroLsJs(selRpc,'RPC'))
                elif ifVarIsNotNone(value) ==True:
                    if ifxInjs(value,'RPC'):
                        if value['RPC'] !='':
                            sg4 = [sg.Text('chainId:'),sg.Input(value['RPC'][0], disabled=True, key='RPC')]
                            selRpc = getLsJsXEqY(selRpc,'RPC',value['RPC'])
                if sellRPCbef != selRpc:
                    change = True
                else:
                    change = False
        elif event == 'OK':
            if ifLsLenEq1(selRpc):
                window.close()
                return selRpc[0]
    window.close()
def lsJsX(ls,x):
    lsN = []
    for i in range(0,len(ls)):
        if x in ls[i]:
            lsN.append(ls[i][x])
    return lsN
def chooseDefaultRPC():
    
    rpcLs = f.jsRead('RPCList.json')
    netName = rpcLs['names'][0]
    menu_def = [['File', ['Open', 'Save', 'Exit',]],
                ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
                ['Help', 'About...'],]
    layout = [[sg.Menu(menu_def)],[sg.Text('NetworkName'),sg.Combo(rpcLs['names'],key='NetworkName')],
    [sg.Text('network:'),sg.Combo(lsJsX(rpcLs[netName],'network'), key='network')],

    [sg.Text('nativeCurrency:'),sg.Combo(lsJsX(rpcLs[netName],'nativeCurrency'), key='nativeCurrency'), sg.Push()],
    [sg.Text('chainId:'),sg.Combo(lsJsX(rpcLs[netName],'chainId'), key='chainId'), sg.Push()],
    [sg.Text('RPC:'),sg.Combo(lsJsX(rpcLs[netName],'RPC'),key ='RPC'), sg.Push()],[sg.OK('OK'),sg.Button('Show'),sg.Button('Exit')],
    [sg.OK('OK'),sg.Button('Show'),sg.Button('Auto'),sg.Button('Exit')]]

    window = sg.Window('Window Title', layout, finalize=True)

    event, values = window.read()
    if event == 'Auto':
        return 'Auto'
    if event == 'Show':
            if values['NetworkName'] !='' or values['NetworkName'] != NetWas:
                selRpc = f.jsIt(rpcLs[values['NetworkName']])
                NetWas = values['NetworkName']
                print(selRpc)
                change = True
                while change == True:
                    sellRPCbef = selRpc
                    if ifVarIsNotNone(values) == True:
                        if ifxInjs(values,'network'):
                            if values['network'] !='':
                                sg2 = [sg.Text('network:'),sg.Input(values['network'][0], disabled=True, key='network')]
                                selRpc = getLsJsXEqY(selRpc,'network',values['network'])
                    elif ifVarIsNotNone(value) ==True:
                        if ifxInjs(value,'network'):
                            if value['network'] !='':
                                sg2 = [sg.Text('network:'),sg.Input(value['network'][0], disabled=True, key='network')]
                                selRpc = getLsJsXEqY(selRpc,'network',value['network'])
                            else:
                                window['network'].update(values=getListFroLsJs(selRpc,'network'))
                    if ifVarIsNotNone(values) == True:
                        if ifxInjs(values,'nativeCurrency'):
                            if values['nativeCurrency'] !='':
                                sg3 = [sg.Text('nativeCurrency:'),sg.Input(values['nativeCurrency'][0], disabled=True, key='nativeCurrency')]
                                selRpc = getLsJsXEqY(selRpc,'nativeCurrency',values['nativeCurrency'])
                            else:
                                window['nativeCurrency'].update(values=getListFroLsJs(selRpc,'nativeCurrency'))
                    elif ifVarIsNotNone(value) ==True:
                        if ifxInjs(value,'nativeCurrency'):
                            if value['nativeCurrency'] !='':
                                sg3 = [sg.Text('nativeCurrency:'),sg.Input(values['nativeCurrency'][0], disabled=True, key='nativeCurrency')]
                                selRpc = getLsJsXEqY(selRpc,'nativeCurrency',value['nativeCurrency'])
                    if ifVarIsNotNone(values) == True:
                        if ifxInjs(values,'chainId'):
                            if values['chainId'] !='':
                                sg4 = [sg.Text('chainId:'),sg.Input(values['chainId'][0], disabled=True, key='chainId')]
                                selRpc = getLsJsXEqY(selRpc,'chainId',values['chainId'])
                            else:
                                window['chainId'].update(values=getListFroLsJs(selRpc,'chainId'))
                    elif ifVarIsNotNone(value) ==True:
                        if ifxInjs(value,'chainId'):
                            if value['chainId'] !='':
                                sg4 = [sg.Text('chainId:'),sg.Input(value['chainId'][0], disabled=True, key='chainId')]
                                selRpc = getLsJsXEqY(selRpc,'chainId',value['chainId'])
                    if ifVarIsNotNone(values) == True:
                        if ifxInjs(values,'RPC'):
                            if values['RPC'] !='':
                                sg4 = [sg.Text('RPC:'),sg.Input(values['RPC'][0], disabled=True, key='RPC')]
                                selRpc = getLsJsXEqY(selRpc,'RPC',values['RPC'])
                            else:
                                window['RPC'].update(values=getListFroLsJs(selRpc,'RPC'))
                    elif ifVarIsNotNone(value) ==True:
                        if ifxInjs(value,'RPC'):
                            if value['RPC'] !='':
                                sg4 = [sg.Text('chainId:'),sg.Input(value['RPC'][0], disabled=True, key='RPC')]
                                selRpc = getLsJsXEqY(selRpc,'RPC',value['RPC'])
                    if sellRPCbef != selRpc:
                        change = True
                    else:
                        change = False
            
    if event == sg.WIN_CLOSED or event == 'Exit':
        close.window()
    elif event == 'OK':
        rpcLs['default'] = {'networkName':values['NetworkName'][0]}
        for i in range(0,len(lsV)):
            rpcLs['default'][lsV[i]] = values[lsV[i]][0]
        
def AddRPC():
    sg.set_options(suppress_raise_key_errors=False, suppress_error_popups=False, suppress_key_guessing=False)
    menu_def = [['File',  'Save', 'Exit',],
                ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
                ['Help', 'About...'],]
    sgTop = [sg.Menu(menu_def)]

    layout = [[sg.Text('Network Name'),sg.Input('',key='NetworkName'),sg.Push()],[sg.Text('network'),sg.Combo(['Mainnet','TestNet'],key='network'),sg.Push()],[sg.Text('nativeCurrency'),sg.Input('',key='nativeCurrency'),sg.Push()],[sg.Text('chainId'),sg.Input('',key='chainId'),sg.Push()],[sg.Text('RPC'),sg.Input('',key='RPC'),sg.Push()],[sg.Text('BlockExplorer'),sg.Input('',key='BlockExplorer'),sg.Push()],[sg.Text('RPC'),sg.Input('',key='contractName'),sg.Push()]]
    sgButtons = [sg.OK('OK'),sg.Button('Show'),sg.Button('Exit')]
    layout = [sgTop,layout,sgButtons]
    window = sg.Window('RPC Settings', layout, finalize=True)
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        webbrowser.get(chrome.open(value['BlockExplorer']))
        webbrowser.get(chrome.open(value['RPC']))
    if event == 'OK':
        rpcLs = f.jsRead('RPCList.json')
        if value['NetworkName'] not in rpcLs['names']:
            rpcLs['names'].append(value['NetworkName'])
            rpcLs[value['NetworkName']]= []
        rpcLs[value['NetworkName']].append({'netName':value['NetworkName'],'chainId':value['chainId'],'RPC':value['RPC'],'nativeCurrency':value['nativeCurrency'],'blockExplorer':value['blockExplorer']})
        f.pen(rpcLs,'RPCList.json')
    if event == 'Exit':
        close.window()
chooseDefaultRPC()
