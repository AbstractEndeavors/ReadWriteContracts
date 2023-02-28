import PySimpleGUI as sg
import windowRuns
import sys
import grabApi
import functions as fun
import guiFunctions as guiFun
import json
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
                input(path)
    return ls
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
def startCont(path):
    sys.path.insert(0, path)
    import dothefunx
    dotheFunx.startIt()
    sys.path.insert(0, home)
def blockDefaults():
    block_3 = [[sg.Text('derive Source From Address', font='Any 20')],[sg.Input('',key='runAdd'), sg.Text('input contract address')],[sg.T('This frame has element_justification="c"')],[sg.Button('RUN'), sg.Button('checkSum')],[sg.Text('searches All Networks',)]]
    block_4 = [[sg.Text('Block 4', font='Any 20')],[sg.T('This is some random text',key='inputs')],[sg.Image(data=sg.DEFAULT_BASE64_ICON, enable_events=True)]  ]
    block_2 = [
               [sg.T('existing address: '),guiFun.dropDown({"ls":getAllSt(getInfos(),'add'),"key":'addressChooseLs',"size":(len(getAllSt(getInfos(),'add')[0])+5,15),"default_value":getAllSt(getInfos(),'add')[0],"visible":True,"enable_events":True})],
               [sg.T('network: '),guiFun.dropDown({"ls":findLsJsSpec(getInfos(),'add',getAllSt(getInfos(),'add')[0],'network'),"key":'networkChooseLs',"size":(len(findLsJsSpec(getInfos(),'add',getAllSt(getInfos(),'add')[0],'network'))+5,15),"default_value":findLsJsSpec(getInfos(),'add',getAllSt(getInfos(),'add')[0],'network'),"visible":True,"enable_events":True})],
               [sg.T('network Name: '),guiFun.dropDown({"ls":findLsJsSpec(getInfos(),'add',getAllSt(getInfos(),'add')[0],'net'),"key":'netNameChooseLs',"size":(len(findLsJsSpec(getInfos(),'add',getAllSt(getInfos(),'add')[0],'net'))+5,15),"default_value":findLsJsSpec(getInfos(),'add',getAllSt(getInfos(),'add')[0],'net'),"visible":True,"enable_events":True})],
               [sg.T('contract Name: '),guiFun.dropDown({"ls":findLsJsSpec(getInfos(),'add',getAllSt(getInfos(),'add')[0],'ContractName'),"key":'nameChooseLs',"size":(len(findLsJsSpec(getInfos(),'add',getAllSt(getInfos(),'add')[0],'ContractName'))+5,15),"default_value":findLsJsSpec(getInfos(),'add',getAllSt(getInfos(),'add')[0],'ContractName'),"visible":True,"enable_events":True})],
               [sg.T('path: '),guiFun.dropDown({"ls":findLsJsSpec(getInfos(),'add',getAllSt(getInfos(),'add')[0],'path'),"key":'pathChooseLs',"size":(len(findLsJsSpec(getInfos(),'add',getAllSt(getInfos(),'add')[0],'path'))+5,15),"default_value":findLsJsSpec(getInfos(),'add',getAllSt(getInfos(),'add')[0],'path'),"visible":True,"enable_events":True})],
               [sg.Button('getABI',key='getABI',enable_events=True)]
                ]
    return block_2,block_3,block_4
def chatBotWindow():
  return [[sg.Text('Your output will go here', size=(40, 1))],[sg.Output(size=(127, 30), font=('Helvetica 10'))],[sg.Text('Command History'),sg.Text('', size=(20, 3), key='history')],[sg.ML(size=(85, 5), enter_submits=True, key='query', do_not_clear=False),sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]
def chatBotLayout():
  return [[sg.Menu(menu_def, tearoff=True, font='_ 12', key='-MENUBAR-')],[sg.Text('Right click me for a right click menu example')],[sg.Output(size=(60, 20))],[sg.ButtonMenu('ButtonMenu',  right_click_menu, key='-BMENU-', text_color='red', disabled_text_color='green'), sg.Button('Plain Button')],[sg.Button('Run'), sg.Button('Shortcut 1'), sg.Button('Fav Program'), sg.Button('EXIT')],[sg.Text('Your output will go here', size=(40, 1))],[sg.Output(size=(127, 30), font=('Helvetica 10'))],[sg.Text('Command History'),sg.Text('', size=(20, 3), key='history')],[sg.ML(size=(85, 5), enter_submits=True, key='query', do_not_clear=False),sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))],]
def fileMenu():
  return [['&File', ['&Open     Ctrl-O', '&Save       Ctrl-S', '&Properties', 'E&xit']],['&Edit', ['&Paste', ['Special', 'Normal', ], 'Undo', 'Options::this_is_a_menu_key'], ],['&Toolbar', ['---', 'Command &1', 'Command &2','---', 'Command &3', 'Command &4']],['&Help', ['&About...']]]
def rightClickMenu():
  return ['Unused', ['Right', '!&Click', '&Menu', 'E&xit', 'Properties']]
def desktopTheme(ls):
  theme_dict = {'BACKGROUND': '#2B475D','TEXT': '#FFFFFF','INPUT': '#F2EFE8','TEXT_INPUT': '#000000','SCROLL': '#F2EFE8','BUTTON': ('#000000', '#C2D4D8'),'PROGRESS': ('#FFFFFF', '#C7D5E0'),'BORDER': 0,'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}
  sg.theme_add_new('Dashboard', theme_dict)
  sg.theme('Dashboard')
  BORDER_COLOR = '#C7D5E0'
  DARK_HEADER_COLOR = '#1B2838'
  BPAD_TOP = ((20,20), (20, 10))
  BPAD_LEFT = ((20,10), (0, 0))
  BPAD_LEFT_INSIDE = (0, (10, 0))
  BPAD_RIGHT = ((10,20), (10, 0))
  #fileMenu =  test_menus()
  top_banner = [[sg.Text('Dashboard', font='Any 20', background_color=DARK_HEADER_COLOR, enable_events=True, grab=False), sg.Push(background_color=DARK_HEADER_COLOR),sg.Text('Wednesday 27 Oct 2021', font='Any 20', background_color=DARK_HEADER_COLOR)],]
  top  = [[sg.Push(), sg.Text('Weather Could Go Here', font='Any 20'), sg.Push()],[sg.T('This Frame has a relief while the others do not')],[sg.T('This window is resizable (see that sizegrip in the bottom right?)')]]
  block_2 = ls[0]
  block_3 = ls[1]
  block_4 = ls[2]
  layout = [ProgressBar(),[sg.Frame('', [[sg.Frame('', block_2,size=(450,150), pad=BPAD_LEFT_INSIDE, border_width=0, expand_x=True, expand_y=True, )],[sg.Frame('', block_3, size=(450,150),  pad=BPAD_LEFT_INSIDE, border_width=0, expand_x=True, expand_y=True, element_justification='l')]],pad=BPAD_LEFT, background_color=BORDER_COLOR, border_width=0, expand_x=True, expand_y=True),
                           sg.Column(block_4,key='getCol', size=(450, 320), pad=BPAD_RIGHT,  expand_x=True, expand_y=True, grab=True),],[sg.Sizegrip(background_color=BORDER_COLOR)]]
  windowRuns.widowMain(sg.Window('Dashboard PySimpleGUI-Style', layout, margins=(0,0), background_color=BORDER_COLOR,keep_on_top=False, no_titlebar=False, resizable=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_LOC_EXIT)),

def ChatBotWithHistory():
  sg.theme('GreenTan')
  layout = chatBotWindow()
  windowRuns.windowChat(sg.Window('Chat window with history', layout,default_element_size=(30, 2),font=('Helvetica', ' 13'),default_button_element_size=(8, 2),return_keyboard_events=True))
  command_history = []
  history_offset = 0

def second_window():
    layout = [[sg.Text('The second form is small \nHere to show that opening a window using a window works')],[sg.OK()]]
    window = sg.Window('Second Form', layout)
    event, values = window.read()
    window.close()
def test_menus():
    sg.theme('LightGreen')
    sg.set_options(element_padding=(0, 0))
    menu_def = fileMenu()
    right_click_menu = rightClickMenu()
    layout = [[sg.Menu(menu_def, tearoff=True, font='_ 12', key='-MENUBAR-')],[sg.Text('Right click me for a right click menu example')],[sg.Output(size=(60, 20))],[sg.ButtonMenu('ButtonMenu',  right_click_menu, key='-BMENU-', text_color='red', disabled_text_color='green'), sg.Button('Plain Button')],[sg.Button('Run'), sg.Button('Shortcut 1'), sg.Button('Fav Program'), sg.Button('EXIT')],[sg.Text('Your output will go here', size=(40, 1))],[sg.Output(size=(127, 30), font=('Helvetica 10'))],[sg.Text('Command History'),sg.Text('', size=(20, 3), key='history')],[sg.ML(size=(85, 5), enter_submits=True, key='query', do_not_clear=False),sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))],]
    windowRuns.menuWindow(sg.Window("Windows-like program",layout,default_element_size=(12, 1),default_button_element_size=(12, 1)))
    test_menus()
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
desktopTheme(blockDefaults())
