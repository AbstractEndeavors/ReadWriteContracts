from web3 import Web3
import sys
import os
home = os.getcwd()
import json
sys.path.insert(0, "/home/bigrugz/Desktop/New Folder 2/walls")
import priv_key as priv
import PySimpleGUI as sg
import codecs
import requests
from hexbytes import HexBytes
from web3 import Web3, HTTPProvider
def avgGasPriceEstd():
    pending_transactions = web3.provider.make_request("parity_pendingTransactions", [])
    gas_prices,gases = [],[]
    for tx in pending_transactions["result"[:10]]:
        gas_prices.append(int((tx["gasPrice"]),16))
        gases.append(int((tx["gas"])))
    return statistics.median(gas_prices)
def avgGasPriceEst():
    req = requests.get('https://ethgasstation.info/json/ethgasAPI.json')
    t = json.loads(req.content)
    print('safeLow', t['safeLow'])
    print('average', t['average'])
    print('fast', t['fast'])
    print('fastest', t['fastest'])
    #web3.eth.Eth.generateGasPrice`
    gas_price1 = web3.eth.gasPrice
    return t['fast']/(10**8)
def specificverifyInput(inType,inVar,outType,outVar,fun,ask):
    asky = ''
    layout = [[sg.Text(ask), sg.Yes()],
            [sg.Text('choose anther '+str(outVar)+' input:'), sg.No()],
            [sg.Yes(), sg.No()]]
    window = sg.Window('Window Title', layout)
    while asky == '':             
        event, values = window.read()
        window
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
    windowDesk['getCol'].update(value=layout)
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
def askList(nets):
    y = []
    sg.set_options(suppress_raise_key_errors=False, suppress_error_popups=False, suppress_key_guessing=False)
    layout = [[sg.Text('functions:'),sg.Combo(nets, key='functions',default_value=nets[0]), sg.Push()],
    [sg.OK('OK'),sg.Button('Show'),sg.Button('Exit')]]
    windowDesk
    window = sg.Window('Window Title', layout, finalize=True)
    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.OK() or event == 'OK':
            return values['functions']
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
    window.close()
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
def ifInput(js):
    lsType = ['address','uint','bool','bytes','string']
    if 'inputs' in js:

        inps = js['inputs']
        for i in range(0,len(inps)):
            if ' ' in inps[i]:
                askAll(inps[i].split(' ')[0],inps[i].split(' ')[-1],js['name'])
            else:
                 askAll(inps[i],inps[i],js['name'])
def homeIt():
	changeGlob("home",os.getcwd())
	slash = "//"
	if "//" not in str(home):
		slash = "/"
		changeGlob("slash",slash)
	return home,slash
def pen(paper, place):
	with open(place, "w") as f:
		f.write(str(paper))
		f.close()
		return
def isHex(x):
	try:
		z = x.hex()
		return True
	except:
		return False
def printHex(x):
	if isHex(x):
		return x.hex()
	return text
def changeGlob(x,v):
	globals()[x] = v
def readerC(file):
	with open(file,"r" ,encoding="utf-8-sig") as f:
		text = f.read()
		return text
def mkLs(ls):
  if type(ls) is not list:
    ls = [ls]
  return ls
def getCodex(x):
    b = get_hex_data(x)
    return codecs.decode(b, 'UTF-8')
def kek(x):
    st = '"'+str(x)+'"'
    return w3.keccak(text=str(x)).hex()
def read_hex(hb):
    h = "".join(["{:02X}".format(b) for b in hb])
    return h
def get_hex_data(x):
    n = len(x)
    hex = x
    return int(hex, n)
def NFTids(ls):
	uint256=ls[0]
	tx = cont.functions.NFTids(int(uint256)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def Pmint(ls):
	address__account,uint256__id,uint256__amount,bytes_data=ls
	tx = cont.functions.Pmint(str(address__account),int(uint256__id),int(uint256__amount),kek(bytes_data)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def PsetURI(ls):
	uint256_k=ls[0]
	tx = cont.functions.PsetURI(int(uint256_k)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def RedGiant():
	tx = cont.functions.RedGiant().call()
	print("RedGiant ="+str(tx))
	return tx
def SuperNova():
	tx = cont.functions.SuperNova().call()
	print("SuperNova ="+str(tx))
	return tx
def WhiteDwarf():
	tx = cont.functions.WhiteDwarf().call()
	print("WhiteDwarf ="+str(tx))
	return tx
def Zero():
	tx = cont.functions.Zero().call()
	print("Zero ="+str(tx))
	return tx
def balanceOf(ls):
	address_account,uint256_id=ls
	tx = cont.functions.balanceOf(str(address_account),int(uint256_id)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def balanceOfBatch(ls):
	addressls_accounts,uint256ls_ids=ls
	tx = cont.functions.balanceOfBatch(str(addressls_accounts),int(uint256ls_ids)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def burn(ls):
	address_account,uint256_id,uint256_value=ls
	tx = cont.functions.burn(str(address_account),int(uint256_id),int(uint256_value)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def burnBatch(ls):
	address_account,uint256ls_ids,uint256ls_values=ls
	tx = cont.functions.burnBatch(str(address_account),int(uint256ls_ids),int(uint256ls_values)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def checkTots():
	tx = cont.functions.checkTots().call()
	print("checkTots ="+str(tx))
	return tx
def exists(ls):
	uint256_id=ls[0]
	tx = cont.functions.exists(int(uint256_id)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def getBalance():
	tx = cont.functions.getBalance().call()
	print("getBalance ="+str(tx))
	return tx
def isApprovedForAll(ls):
	address_account,address_operator=ls
	tx = cont.functions.isApprovedForAll(str(address_account),str(address_operator)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def mint(ls):
	address__account,uint256__id,uint256__amount,bytes_data=ls
	tx = cont.functions.mint(str(address__account),int(uint256__id),int(uint256__amount),kek(bytes_data)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def mintBatch(ls):
	address__to,uint256ls__ids,uint256ls__amounts,bytes_data=ls
	tx = cont.functions.mintBatch(str(address__to),int(uint256ls__ids),int(uint256ls__amounts),kek(bytes_data)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def name():
	tx = cont.functions.name().call()
	print("name ="+str(tx))
	return tx
def owner():
	tx = cont.functions.owner().call()
	print("owner ="+str(tx))
	return tx
def redgiant():
	tx = cont.functions.redgiant().call()
	print("redgiant ="+str(tx))
	return tx
def renounceOwnership(ls):
	tx = cont.functions.renounceOwnership(str()).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def safeBatchTransferFrom(ls):
	address_from,address_to,uint256ls_ids,uint256ls_amounts,bytes_data=ls
	tx = cont.functions.safeBatchTransferFrom(str(address_from),str(address_to),int(uint256ls_ids),int(uint256ls_amounts),kek(bytes_data)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def safeTransferFrom(ls):
	address_from,address_to,uint256_id,uint256_amount,bytes_data=ls
	tx = cont.functions.safeTransferFrom(str(address_from),str(address_to),int(uint256_id),int(uint256_amount),kek(bytes_data)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def setApprovalForAll(ls):
	address_operator,bool_approved=ls
	tx = cont.functions.setApprovalForAll(str(address_operator),str(bool_approved)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def setURI(ls):
	uint256_k=ls[0]
	tx = cont.functions.setURI(int(uint256_k)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def strange():
	tx = cont.functions.strange().call()
	print("strange ="+str(tx))
	return tx
def supernova():
	tx = cont.functions.supernova().call()
	print("supernova ="+str(tx))
	return tx
def supportsInterface(ls):
	bytes4_interfaceId=ls[0]
	tx = cont.functions.supportsInterface(int(bytes4_interfaceId)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def symbol():
	tx = cont.functions.symbol().call()
	print("symbol ="+str(tx))
	return tx
def token():
	tx = cont.functions.token().call()
	print("token ="+str(tx))
	return tx
def totalSupply(ls):
	uint256_id=ls[0]
	tx = cont.functions.totalSupply(int(uint256_id)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def transferOwnership(ls):
	address_newOwner=ls[0]
	tx = cont.functions.transferOwnership(str(address_newOwner)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def updateManager(ls):
	address_man=ls[0]
	tx = cont.functions.updateManager(str(address_man)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def updateToken(ls):
	address_newToken=ls[0]
	tx = cont.functions.updateToken(str(address_newToken)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def uri(ls):
	uint256=ls[0]
	tx = cont.functions.uri(int(uint256)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def uri_RedGiant():
	tx = cont.functions.uri_RedGiant().call()
	print("uri_RedGiant ="+str(tx))
	return tx
def uri_SuperNova():
	tx = cont.functions.uri_SuperNova().call()
	print("uri_SuperNova ="+str(tx))
	return tx
def uri_WhiteDwarf():
	tx = cont.functions.uri_WhiteDwarf().call()
	print("uri_WhiteDwarf ="+str(tx))
	return tx
def uri_ls(ls):
	uint256=ls[0]
	tx = cont.functions.uri_ls(int(uint256)).buildTransaction({'gasPrice': avgGasPriceEst(),'gas':web3.eth.estimateGas({'to': w3.toChecksumAddress(add), 'from': w3.toChecksumAddress(account_1.address), 'value': 0}),'from': account_1.address,'nonce': nonce,'chainId': int(chainId)})
	print(tx)
	return tx
def whitedwarf():
	tx = cont.functions.whitedwarf().call()
	print("whitedwarf ="+str(tx))
	return tx

def getDefVaris(na):
	js = {'NFTids': 'uint256', 'Pmint': 'address__account,uint256__id,uint256__amount,bytes_data', 'PsetURI': 'uint256_k', 'RedGiant': '', 'SuperNova': '', 'WhiteDwarf': '', 'Zero': '', 'balanceOf': 'address_account,uint256_id', 'balanceOfBatch': 'addressls_accounts,uint256ls_ids', 'burn': 'address_account,uint256_id,uint256_value', 'burnBatch': 'address_account,uint256ls_ids,uint256ls_values', 'checkTots': '', 'exists': 'uint256_id', 'getBalance': '', 'isApprovedForAll': 'address_account,address_operator', 'mint': 'address__account,uint256__id,uint256__amount,bytes_data', 'mintBatch': 'address__to,uint256ls__ids,uint256ls__amounts,bytes_data', 'name': '', 'owner': '', 'redgiant': '', 'renounceOwnership': '', 'safeBatchTransferFrom': 'address_from,address_to,uint256ls_ids,uint256ls_amounts,bytes_data', 'safeTransferFrom': 'address_from,address_to,uint256_id,uint256_amount,bytes_data', 'setApprovalForAll': 'address_operator,bool_approved', 'setURI': 'uint256_k', 'strange': '', 'supernova': '', 'supportsInterface': 'bytes4_interfaceId', 'symbol': '', 'token': '', 'totalSupply': 'uint256_id', 'transferOwnership': 'address_newOwner', 'updateManager': 'address_man', 'updateToken': 'address_newToken', 'uri': 'uint256', 'uri_RedGiant': '', 'uri_SuperNova': '', 'uri_WhiteDwarf': '', 'uri_ls': 'uint256', 'whitedwarf': ''}
	return js[na].split(",")
def view_all():
	print("RedGiant",":",(cont.functions.RedGiant().call()))
	print("SuperNova",":",(cont.functions.SuperNova().call()))
	print("WhiteDwarf",":",(cont.functions.WhiteDwarf().call()))
	print("Zero",":",(cont.functions.Zero().call()))
	print("checkTots",":",(cont.functions.checkTots().call()))
	print("getBalance",":",(cont.functions.getBalance().call()))
	print("name",":",(cont.functions.name().call()))
	print("owner",":",(cont.functions.owner().call()))
	print("redgiant",":",(cont.functions.redgiant().call()))
	print("strange",":",(cont.functions.strange().call()))
	print("supernova",":",(cont.functions.supernova().call()))
	print("symbol",":",(cont.functions.symbol().call()))
	print("token",":",(cont.functions.token().call()))
	print("uri_RedGiant",":",(cont.functions.uri_RedGiant().call()))
	print("uri_SuperNova",":",(cont.functions.uri_SuperNova().call()))
	print("uri_WhiteDwarf",":",(cont.functions.uri_WhiteDwarf().call()))
	print("whitedwarf",":",(cont.functions.whitedwarf().call()))
	
def getDeffs(x,y):
  if y == None:
    return globals()[x]()
  return globals()[x](y)
def send_it(ans):
    tx = json.loads(str(ans).replace("'",'"'))
    tx["nonce"] = w3.eth.getTransactionCount(w3.toChecksumAddress(tx['from']))
    tx["gas"] = web3.eth.estimateGas({'to': w3.toChecksumAddress(tx['to']), 'from': w3.toChecksumAddress(tx['from']), 'value': tx['value']})
    signed_tx = w3.eth.account.sign_transaction(tx, priv.p)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
def hubbub():
  print('\n\n')
  view_all()
  function = askList(['view_all()', 'NFTids(uint256)', 'Pmint(address__account,uint256__id,uint256__amount,bytes_data)', 'PsetURI(uint256_k)', 'RedGiant()', 'SuperNova()', 'WhiteDwarf()', 'Zero()', 'balanceOf(address_account,uint256_id)', 'balanceOfBatch(addressls_accounts,uint256ls_ids)', 'burn(address_account,uint256_id,uint256_value)', 'burnBatch(address_account,uint256ls_ids,uint256ls_values)', 'checkTots()', 'exists(uint256_id)', 'getBalance()', 'isApprovedForAll(address_account,address_operator)', 'mint(address__account,uint256__id,uint256__amount,bytes_data)', 'mintBatch(address__to,uint256ls__ids,uint256ls__amounts,bytes_data)', 'name()', 'owner()', 'redgiant()', 'renounceOwnership()', 'safeBatchTransferFrom(address_from,address_to,uint256ls_ids,uint256ls_amounts,bytes_data)', 'safeTransferFrom(address_from,address_to,uint256_id,uint256_amount,bytes_data)', 'setApprovalForAll(address_operator,bool_approved)', 'setURI(uint256_k)', 'strange()', 'supernova()', 'supportsInterface(bytes4_interfaceId)', 'symbol()', 'token()', 'totalSupply(uint256_id)', 'transferOwnership(address_newOwner)', 'updateManager(address_man)', 'updateToken(address_newToken)', 'uri(uint256)', 'uri_RedGiant()', 'uri_SuperNova()', 'uri_WhiteDwarf()', 'uri_ls(uint256)', 'whitedwarf()'])
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
global netName,chainId,rpc,nativeCurrency,explorer,scanner,w3,nonce,varis,web3,windowDesk
windowDesk = ''
varis = {'inputs':{'inpCurr':[],'typeCurr':[]}}
ABI = json.loads('[{"inputs": [], "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "account", "type": "address"}, {"indexed": true, "internalType": "address", "name": "operator", "type": "address"}, {"indexed": false, "internalType": "bool", "name": "approved", "type": "bool"}], "name": "ApprovalForAll", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "previousOwner", "type": "address"}, {"indexed": true, "internalType": "address", "name": "newOwner", "type": "address"}], "name": "OwnershipTransferred", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "operator", "type": "address"}, {"indexed": true, "internalType": "address", "name": "from", "type": "address"}, {"indexed": true, "internalType": "address", "name": "to", "type": "address"}, {"indexed": false, "internalType": "uint256[]", "name": "ids", "type": "uint256[]"}, {"indexed": false, "internalType": "uint256[]", "name": "values", "type": "uint256[]"}], "name": "TransferBatch", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "operator", "type": "address"}, {"indexed": true, "internalType": "address", "name": "from", "type": "address"}, {"indexed": true, "internalType": "address", "name": "to", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "id", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "value", "type": "uint256"}], "name": "TransferSingle", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": false, "internalType": "string", "name": "value", "type": "string"}, {"indexed": true, "internalType": "uint256", "name": "id", "type": "uint256"}], "name": "URI", "type": "event"}, {"stateMutability": "payable", "type": "fallback"}, {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "NFTids", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "_account", "type": "address"}, {"internalType": "uint256", "name": "_id", "type": "uint256"}, {"internalType": "uint256", "name": "_amount", "type": "uint256"}, {"internalType": "bytes", "name": "data", "type": "bytes"}], "name": "Pmint", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "k", "type": "uint256"}], "name": "PsetURI", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "RedGiant", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "SuperNova", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "WhiteDwarf", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "Zero", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "account", "type": "address"}, {"internalType": "uint256", "name": "id", "type": "uint256"}], "name": "balanceOf", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address[]", "name": "accounts", "type": "address[]"}, {"internalType": "uint256[]", "name": "ids", "type": "uint256[]"}], "name": "balanceOfBatch", "outputs": [{"internalType": "uint256[]", "name": "", "type": "uint256[]"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "account", "type": "address"}, {"internalType": "uint256", "name": "id", "type": "uint256"}, {"internalType": "uint256", "name": "value", "type": "uint256"}], "name": "burn", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "account", "type": "address"}, {"internalType": "uint256[]", "name": "ids", "type": "uint256[]"}, {"internalType": "uint256[]", "name": "values", "type": "uint256[]"}], "name": "burnBatch", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "checkTots", "outputs": [{"internalType": "uint256[3]", "name": "", "type": "uint256[3]"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "id", "type": "uint256"}], "name": "exists", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "getBalance", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "account", "type": "address"}, {"internalType": "address", "name": "operator", "type": "address"}], "name": "isApprovedForAll", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "_account", "type": "address"}, {"internalType": "uint256", "name": "_id", "type": "uint256"}, {"internalType": "uint256", "name": "_amount", "type": "uint256"}, {"internalType": "bytes", "name": "data", "type": "bytes"}], "name": "mint", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "_to", "type": "address"}, {"internalType": "uint256[]", "name": "_ids", "type": "uint256[]"}, {"internalType": "uint256[]", "name": "_amounts", "type": "uint256[]"}, {"internalType": "bytes", "name": "data", "type": "bytes"}], "name": "mintBatch", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "name", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "owner", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "redgiant", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "renounceOwnership", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "from", "type": "address"}, {"internalType": "address", "name": "to", "type": "address"}, {"internalType": "uint256[]", "name": "ids", "type": "uint256[]"}, {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}, {"internalType": "bytes", "name": "data", "type": "bytes"}], "name": "safeBatchTransferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "from", "type": "address"}, {"internalType": "address", "name": "to", "type": "address"}, {"internalType": "uint256", "name": "id", "type": "uint256"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}, {"internalType": "bytes", "name": "data", "type": "bytes"}], "name": "safeTransferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "operator", "type": "address"}, {"internalType": "bool", "name": "approved", "type": "bool"}], "name": "setApprovalForAll", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "k", "type": "uint256"}], "name": "setURI", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "strange", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "supernova", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "bytes4", "name": "interfaceId", "type": "bytes4"}], "name": "supportsInterface", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "symbol", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "token", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "id", "type": "uint256"}], "name": "totalSupply", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}], "name": "transferOwnership", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "man", "type": "address"}], "name": "updateManager", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "newToken", "type": "address"}], "name": "updateToken", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "uri", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "uri_RedGiant", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "uri_SuperNova", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "uri_WhiteDwarf", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "uri_ls", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "whitedwarf", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"stateMutability": "payable", "type": "receive"}]')
changeGlob("jsInfo",{'nativeCurrency': "AVAX", 'network': "Testnet", 'RPC': "https://api.avax-test.network/ext/bc/C/rpc", 'chainId': 43113, 'blockExplorer': "https://testnet.snowtrace.io", 'networkName': "AVAX"})
changeGlob('chainId',jsInfo['chainId'])
changeGlob('scanner',jsInfo['blockExplorer'])
changeGlob('w3',Web3(Web3.HTTPProvider(jsInfo['RPC'])))
changeGlob('web3',w3)
add = w3.toChecksumAddress("0x710823129ae7ED40a171E922b3928D4A04F30ce9")
cont = w3.eth.contract(add,abi = ABI)
account_1 = w3.eth.account.privateKeyToAccount(priv.p)
changeGlob('account_1',account_1)
nonce = w3.eth.getTransactionCount(account_1.address)
changeGlob('nonce',w3.eth.getTransactionCount(account_1.address))
  
