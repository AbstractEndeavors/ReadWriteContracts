import grabAbi as grab
import PySimpleGUI as sg
def specificTextInput(inType,inVar,qu,outType,outVar,fun,ask):
    layout = [
        [sg.Text(inType + ' '+ inVar), sg.Push(), sg.Input('', key='x')],
        [sg.Text(outType+' '+outVar), sg.Push(), sg.Input('', disabled=True, key='x+2')],
        [sg.Button('Show'), sg.Button('Exit')]]
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
    simpleBool(str(k)+' out of '+str(tot)+' inputs in this list')
def denyInp(ty,va,fun,ans,exp):
    simpleBool('your '+str(ty)+' input for '+str(va)+' in function '+str(fun)+'; '+str(ans)+' was denied for '+exp)
def verify(ty,va,fun,ans):
    return simpleBool(find.boolAsk('your '+str(ty)+' input for '+str(va)+' in functin '+str(fun)+' is '+str(ans)+' that ok?'))
def askInput(ty,va,fun):
    return inputIt('please input '+str(ty)+' for variable '+str(va)+' in function'+str(fun)+':')
def askBool(ty,va,fun):
    return inputIt('please input '+str(ty)+' for variable '+str(va)+' in function'+str(fun)+':')
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
global varis
varis = {'inputs':{'inpCurr':[],'typeCurr':[]}}

