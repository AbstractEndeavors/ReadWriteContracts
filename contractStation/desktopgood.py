import PySimpleGUI as sg
import windowRuns
import sys
import grabApi
import functions as fun
import guiFunctions as guiFun
import json
import os
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
def tryCheckSum(x):
    try:
        y = checkSum(x)
        return y
    except:
        return False
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
def isLs(ls):
    if type(ls) is list:
        return True
    return False
def isList(x):
    if x[-1] == ']':
        if x[:-1].split('[')[-1] == '':
            return [x],'*',0
        lsN = []
        for i in range(0,int(x[:-1].split('[')[-1])):
            lsN.append(x)    
        return lsN,i,0
    return x,1,0
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
def lsNum():
    return str('1,2,3,4,5,6,7,8,9,0').split(',')
def isNum(x):
    if isInt(x):
        return True
    for k in range(0,len(str(x))):
        if str(x)[k] not in lsNum():
            return False
    return True
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
    return specificverifyInput(ty,va,ty,ans,fun,'your '+str(ty)+' input for '+str(va)+' in functin '+str(fun)+' is '+str(ans)+' that ok?')
def askInput(ty,va,fun):
    return specificAskInput(ty,va,fun,'please input '+str(ty)+' for variable '+str(va)+' in function'+str(fun)+':')
def askBool(ty,va,fun):
    return specificAskInput(ty,va,fun,'please input '+str(ty)+' for variable '+str(va)+' in function'+str(fun)+':')
def inputUint(ty,va,fun):
    while isUintSt(ty):
        ast = False
        print('input will be multiplied by 10^'+str(int(18))+' if * is added to the end of the input)')
        ans = askInput(ty,va,fun)
        if ans[-1] == '*':
            ast,ans = True,ans[:-1]
        if isNum(ans):
            if ast == True:
                ans = int(float(int(ans))*float(str('1e'+str(int(18)))))
            if verify(ty,va,fun,ans):
                ifVarisLsApp(str(ans))
                return
def inputInt(ty,va,fun):
    while isIntSt(ty):
        ast = False
        print('input will be multiplied by 10^'+str(int(8))+' if * is added to the end of the input)')
        ans = askInput(ty,va,fun)
        if ans[-1] == '*':
            ast,ans = True,ans[:-1]
        if isNum(ans):
            if ast == True:
                ans = int(float(int(ans))*float(str('1e'+str(int(8)))))
            if verify(ty,va,fun,ans):
                ifVarisLsApp(str(ans))
                return
def ifVarisLsApp(x):
    if type(varis['inputs']['inpCurr'][-1]) is list:
        varis['inputs']['inpCurr'][-1].append(x)
    else:
        varis['inputs']['inpCurr'][-1] = x
def inputAddress(ty,va,fun):
    while isAddress(ty):
        ans = tryCheckSum(str(askInput(ty,va,fun)))
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
        inputUint(ty,va,fun)
        inputInt(ty,va,fun)
        cou += 1
        listLoop(cou,tot)
        if deff == False:
            tot = indetLoop(ty,cou)
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
          spl = inps[i].split('_')
          js['inputs'].append(spl[0])
          if isLs(spl):
            if len(spl)>1:
              js['name'].append(spl[1])
  ifInput(js)
  send_it(getDeffs(funName,varis['inputs']['inpCurr']))
  return 
def getDefaultOptions():
    return sg.set_options(suppress_raise_key_errors=True, suppress_error_popups=True, suppress_key_guessing=True)
def getVerifyInput(inType,inVar,outType,outVar,fun,ask):
    return [[sg.Text(ask), sg.Yes()],[sg.Text('choose anther '+str(outVar)+' input:'), sg.No()],[sg.Yes(), sg.No()]]
def getAskInput(inType,inVar,fun,ask):
    return [sg.Text(inType + ' '+ inVar), sg.Input('', key=inType),sg.Text('verify:'), sg.Input('', disabled=True, key='verify')]
def getAskInput(inType,inVar,fun,ask):
    return [sg.Text(inType,key='inType'),sg.Text(' ',key='space'),sg.Text('',key='inVar'),sg.Text(inType,key='inType'),sg.Text('verify:'), sg.Input('', disabled=True, key='verify')]
def getAskList(nets):
    return [[sg.Text('functions:'),sg.Text(nets, key='functions',default_value=nets[0]), sg.Push()],[sg.OK('OK'),sg.Button('Show'),sg.Button('Exit')]]
def getTextInput(inType,inVar,qu,outType,outVar,fun,ask):
    return [[sg.Text(inType + ' '+ inVar), sg.Push(), sg.Input('', key='x')],[sg.Text(outType+' '+outVar), sg.Push(), sg.Input('', disabled=True, key='x+2')],[sg.Button('Show'), sg.Button('Exit')]]
def getSimpleBool(ask):
    return [[sg.Text(ask),sg.Button('True'), sg.Button('False')]]
def specificverifyInput(inType,inVar,outType,outVar,fun,ask):
    asky = ''
    layout = getVerifyInput(inType,inVar,outType,outVar,fun,ask)
    boolWindow(sg.Window('inType', layout),asky)
def askList(nets):
    y = []
    layout = getAskList(nets)
    boolWindow(sg.Window('Window Title', layout, finalize=True),'')
def specificAskInput(inType,inVar,fun,ask):
    asky = ''
    y = asky
    layout = getAskInput(inType,inVar,fun,ask)
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
def specificTextInput(inType,inVar,qu,outType,outVar,fun,ask):
    layout = getTextInput(inType,inVar,qu,outType,outVar,fun,ask)
    window = sg.Window(fun, layout)
    while True:  # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Show':
            x_string = values['x']
            try:
               y = ans = grab.tryCheckSum(x_string)
            except ValueError:
                y = "Wrong number !!!"
            window['x+2'].update(value=y)
    window.close()
def simpleBool(ask):
    asky = ''
    layout = getSimpleBool(ask)
    boolWindow(sg.Window(ask,layout),asky)
def boolWindow(window,asky):
    while asky == '':             
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            asky = False
        if event == sg.OK() or event == 'OK':
            return values['functions']
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        window.close()
        asky = True
    window.close()  
    return asky
def ProgressBar():
    from rpcListNew import rpcs as rpcLs
    return [[sg.Frame('rpc Scan Progress',[[sg.Text('',key='progTitle')],[guiFun.ProgressBar({'val':0, "orientation":'h', "size":(len(rpcLs),20), "key":'progressbar',"enable_events":True})],[sg.Cancel()]], size=(920, 100), pad=((20,20), (20, 10)),  expand_x=True,  relief=sg.RELIEF_GROOVE, border_width=3)]]
def getInfos():
    path,ls = 'infos',[]
    adds = fun.lsDir(path)
    for k in range(0,len(adds)):
        add = adds[k]
        ls.append({'add':add,'network':'','net':'','name':'','path':'','folders':[]})
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
                ls[-1]['ContractName'] = json.loads(fun.reader(fun.crPa(path,'info.json')))['source']['ContractName']
    return ls
def startCont(path):
    sys.path.insert(0, path)
    print(path)
    import dothefunx
    dothefunx.windowDesk = windowDesk
    dotheFunx.startIt()
    sys.path.insert(0, home)
def widowMain(window):
      while True:
        event, values = window.read()
        lsAskGlob = getAsks(window,values['functions'])
        col = [sg.Column(lsAskGlob,key='getCol', size=(450, 320), pad=(450, 320),  expand_x=True, expand_y=True, grab=True),],[sg.Sizegrip(background_color='blue')]
        'inType','inVar','fun'
        window.Refresh()
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            break
        elif event == 'getABI':
              input(values['pathChooseLs'])
              startCont(values['pathChooseLs'])
        elif event == 'RUN':
              from rpcListNew import rpcs as rpcLs
              add = values['runAdd']
              for k in range(0,len(rpcLs)):
                  progress_bar = window['progressbar']
                  progress_bar.UpdateBar(k)
                  keys = fun.getKeys(rpcLs[k])
                  window['progTitle'].update(value=rpcLs[k])
                  window['progTitle'].update(value=rpcLs[k])
                  grabApi.deriveAnyInfo(add,k)
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
def getSheetPath():
    return findLsJsSpec(getInfos(),'add',getAllSt(getInfos(),'add')[0],'path')
def getFile(st):
    return fun.reader(fun.crPa(findLsJsSpec(getInfos(),'add',getAllSt(getInfos(),'add')[0],'path'),st))
def getFunVars(x):
    sys.path.insert(0, getSheetPath())
    import funcSheet
    funs = funcSheet.getDefVaris(x)
    sys.path.insert(0, home)
    return funs
def getFuncFuns():
    sys.path.insert(0, getSheetPath())
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
    [sg.Text('please input '),sg.Text('',key='inType'),sg.Text(' for variable '),sg.Text('',key='inVar'),sg.Text(' in function'),sg.Text('',key='fun'),sg.Text(': '),sg.Input('', disabled=True, key='verify')]
def askBool(ty,va,fun):
    return specificAskInput(ty,va,fun,'please input '+str(ty)+' for variable '+str(va)+' in function'+str(fun)+':')
def mkVisible(window,st,boolIt):
    window[st].update(visible=boolIt)
def cleanLs(ls):
    lsN = []
    for i in range(0,len(ls)):
        if '' != ls[i]:
            lsN.append(ls[i])
    return lsN
def mkvartQ(js):
    varKey = str(js['fun'])+'__'+str(js['type'])+'__'+str(js['var'])
    inp = sg.Input('', key=varKey)
    if 'bool' in js['type']:
        inp = sg.Combo(['True','False'], key=varKey,enable_events=True)
    return [sg.Frame('',[[sg.Text(str(js['var'])+': ',font='Any 15'),inp,sg.Text(str(js['type']),font='Any 15')]],pad=(0, (10, 0)), border_width=0, expand_x=True, expand_y=True, element_justification='v')]
def getTabs(ls):
    tabs = []
    for k in range(0,len(ls)):
        js = {'fun':ls[k].split('(')[0],'type':'','var':''}
        vars = getFunVars(ls[k].split('(')[0])
        print(ls[k].split('(')[0],vars)
        if len(vars[0]) != 0:
            tabs.append([[sg.T(str(ls[k]))]])
            for i in range(0,len(vars)):
                spl = cleanLs(fun.mkLs(vars[i].split('_')))
                print(spl)
                js['type'] = spl[0]
                if len(spl)>1:
                    js['var'] = spl[1]
                tabs[-1].append(mkvartQ(js))
            tabs[-1] = sg.Tab(str(js['fun']),[[sg.Column(tabs[-1],key='getCol', pad=(0, (10, 0)),  expand_x=True, expand_y=True, grab=True)]],key ='tab_'+str(js['fun']))
    return sg.TabGroup([tabs],key="group_functions")
def getNetDrops(titleLs,stLs):
    lsAdd = getAllSt(getInfos(),'add')
    layout = [[sg.T('existing address: '),guiFun.dropDown({"ls":lsAdd,"key":'addressChooseLs',"size":(len(lsAdd[0])+5,15),"default_value":lsAdd[0],"visible":True,"enable_events":True})]] 
    for k in range(0,len(titleLs)):
        ls = findLsJsSpec(getInfos(),'add',lsAdd[0],stLs[k])
        layout.append([sg.T(titleLs[k]+': '),guiFun.dropDown({"ls":ls,"key":stLs[k]+'ChooseLs',"size":(len(ls)+5,15),"default_value":ls,"visible":True,"enable_events":True})])
    lsButtons = [[sg.Button('getABI',key='getABI',enable_events=True)],[sg.Text('derive Source From Address', font='Any 20')],[sg.Input('',key='runAdd'), sg.Text('input contract address')],[sg.T('searches All Networks')],[sg.Button('RUN'), sg.Button('checkSum')]]
    for k in range(0,len(lsButtons)):
        layout.append(lsButtons[k])
    return layout
def blockDefaults():
    top_banner = [[sg.Text('Dashboard', font='Any 20', background_color=jsFormat["DARK_HEADER_COLOR"], enable_events=True, grab=False),sg.Push(background_color=jsFormat["DARK_HEADER_COLOR"]),sg.Text('Wednesday 27 Oct 2021', font='Any 20', background_color=jsFormat["DARK_HEADER_COLOR"])],]
    top  = [[sg.Push(), sg.Text('Weather Could Go Here', font='Any 20'), sg.Push()],[sg.T('This Frame has a relief while the others do not')],[sg.T('This window is resizable (see that sizegrip in the bottom right?)')]]
    block_1 = [sg.Frame('', [[getTabs(getFuncFuns())],[sg.Button('Submit',key='Submit',visible=True,enable_events=True),sg.Button('verify',key='verify',visible=True,enable_events=True)]], pad=((20,20), (20, 10)),  expand_x=True,  relief=sg.RELIEF_GROOVE, border_width=3)]
    block_2 = [sg.Frame('',getNetDrops(['network','network Name','contract Name','path'],['network','net','ContractName','path']), pad=((20,20), (20, 10)),  expand_x=True,  relief=sg.RELIEF_GROOVE, border_width=3)]
    blockFrame = [sg.Frame('',[block_1,block_2],pad=jsFormat["BPAD_LEFT"], background_color=jsFormat["BORDER_COLOR"], border_width=0, expand_x=True, expand_y=True),]
    return [top_banner,top,ProgressBar(),blockFrame]
def chatBotWindow():
  return [[sg.Text('Your output will go here', size=(40, 1))],[sg.Output(size=(127, 30), font=('Helvetica 10'))],[sg.Text('Command History'),sg.Text('', size=(20, 3), key='history')],[sg.ML(size=(85, 5), enter_submits=True, key='query', do_not_clear=False),sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]
def chatBotLayout():
  return [[sg.Menu(menu_def, tearoff=True, font='_ 12', key='-MENUBAR-')],[sg.Text('Right click me for a right click menu example')],[sg.Output(size=(60, 20))],[sg.ButtonMenu('ButtonMenu',  right_click_menu, key='-BMENU-', text_color='red', disabled_text_color='green'), sg.Button('Plain Button')],[sg.Button('Run'), sg.Button('Shortcut 1'), sg.Button('Fav Program'), sg.Button('EXIT')],[sg.Text('Your output will go here', size=(40, 1))],[sg.Output(size=(127, 30), font=('Helvetica 10'))],[sg.Text('Command History'),sg.Text('', size=(20, 3), key='history')],[sg.ML(size=(85, 5), enter_submits=True, key='query', do_not_clear=False),sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))],]
def fileMenu():
  return [['&File', ['&Open     Ctrl-O', '&Save       Ctrl-S', '&Properties', 'E&xit']],['&Edit', ['&Paste', ['Special', 'Normal', ], 'Undo', 'Options::this_is_a_menu_key'], ],['&Toolbar', ['---', 'Command &1', 'Command &2','---', 'Command &3', 'Command &4']],['&Help', ['&About...']]]
def rightClickMenu():
  return ['Unused', ['Right', '!&Click', '&Menu', 'E&xit', 'Properties']]
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
global lsAskGlob,jsFormat,theme_dict
theme_dict = {'BACKGROUND': '#2B475D','TEXT': '#FFFFFF','INPUT': '#F2EFE8','TEXT_INPUT': '#000000','SCROLL': '#F2EFE8','BUTTON': ('#000000', '#C2D4D8'),'PROGRESS': ('#FFFFFF', '#C7D5E0'),'BORDER': 0,'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}
jsFormat = {"BORDER_COLOR":'#C7D5E0',"DARK_HEADER_COLOR":'#1B2838',"BPAD_TOP":((20,20), (20, 10)),"BPAD_LEFT":((20,10), (0, 0)),"BPAD_LEFT_INSIDE":(0, (10, 0)),"BPAD_RIGHT":((10,20), (10, 0))}
lsAskGlob = ''
homeIt()
desktopTheme(blockDefaults())
