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
    return specificverifyInput(ty,va,ty,ans,fun,'your '+str(ty)+' input for '+str(va)+' in functin '+str(fun)+' is '+str(ans)+' that ok?')
def askInput(ty,va,fun):
    return specificAskInput(ty,va,fun,'please input '+str(ty)+' for variable '+str(va)+' in function'+str(fun)+':')
def askBool(ty,va,fun):
    return specificAskInput(ty,va,fun,'please input '+str(ty)+' for variable '+str(va)+' in function'+str(fun)+':')
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
        if ans == 'exit':
            return 'exit'
        else:
            denyInp(ty,va,fun,ans,' bad checksum address')
def inputBool(ty,va,fun):
    while isBool(ty):
        ans = askBool(ty,va,fun)
        if verify(ty,va,fun,ans):
            if ans == True:
                ifVarisLsApp(bool(ans))
            else:
                ifVarisLsApp(bool(ans))
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
        inps = js['inputs']
        for i in range(0,len(inps)):
            if ' ' in inps[i]:
                askAll(inps[i].split(' ')[0],inps[i].split(' ')[-1],js['name'])
            else:
                 askAll(inps[i],inps[i],js['name']) 
def createInp(x):
    #scanner_url = print_scan()
    ask = askList(x)
    varis['inputs'] = {'typeCurr':[],'inpCurr':[],'funJS':[]}
    varis['inputs']['funJS'].append(f.jsIt(f.reader(f.createPath('currFun','allWallVar.json')))['function'][ask.split('(')[0]])
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
