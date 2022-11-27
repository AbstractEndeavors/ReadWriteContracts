import functions as ff
import json
def createInps(ls):
    n = '('
    for i in range(0,len(ls)):
        n = n + ls[i]+ ','
    n = n.replace(' ','_').replace('[]','ls') + ')'
    return n.replace(',)',')')
def parse_it(add,path):
    abiPath = ff.crPa([path,'ABI.json'])
    info = json.loads(ff.reader(ff.crPa([path,'info.json'])).replace("'",'"'))
    path,network,chainId,RPC,explorer,scanner = info['path'],info["network"],info["chainId"],info["RPC"],info["explorer"],info["scanner"],
    ff.pen(add,'currInfo.txt')
    import fun_get as fun
    js,funs = fun.getFuns(abiPath)
    beg = "from web3 import Web3\nimport sys\nimport os\nhome = os.getcwd()\nsys.path.insert(0, '"+home+"')\nimport pK as key\nimport networkChoose as choose\nimport json\nimport functions as f\nsys.path.insert(0, str(home))\nhome,slash = f.homeIt()\n"
    end = '\nglobal network,chainId,rpc,explorer,scanner,w3,nonce\nadd = "'+str(add)+'"\nabi = f.readerC(f.crPa(["'+path+'","ABI.json"]))\nnetwork,chainId,rpc,explorer,scanner,w3 = "'+network+'","'+chainId+'","'+RPC+'","'+explorer+'","'+scanner+'",Web3(Web3.HTTPProvider("'+RPC+'"))\n\ncont = w3.eth.contract(add,abi = abi)\naccount_1 = w3.eth.account.privateKeyToAccount(key.p)\nnonce = w3.eth.getTransactionCount(account_1.address)'
    symbol = 'cont'
    call = []
    asks = []
    fun_sheet = beg.replace("'",'"')
    view_sheet = 'def view_all():\n\t'
    funsWhole =  js['function']
    funnames = funsWhole['names']
    
    for i in range(0,len(funnames)):
        name = str(funnames[i])
        varis = str(createInps(funsWhole[name]['inputs']))
        wholeFun = str(name + varis)
        if funsWhole[name]['stateMutability'] not in ['internal','private','external']:
            asks.append(wholeFun)
            fun_sheet = fun_sheet + 'def '+name+varis+':\n\tx = cont.functions.'+wholeFun+'.call()\n\tf.pen(x,"ask.txt")\n\tprint("'+name+'"," is ",x)\n\treturn x\n'
            if varis == '()':
                view_sheet = view_sheet +  'print("'+name+'",":",f.printHex(cont.functions.'+wholeFun+'.call()))\n\t'
        else:
            call.append(wholeFun)
            fun_sheet = fun_sheet + 'def '+wholeFun+':\n\treturn cont.functions.'+name+".buildTransaction({'gasPrice': 60000000000,'gas':402640,'from': account_1.address,'nonce': nonce,'chainId': int(ch_id)})\n"
    fun_sheet = fun_sheet +view_sheet+ end
    get_em = [asks,call]
    fun_all = []
    for k in range(0,len(get_em)):
        for i in range(0,len(get_em[k])):
            n = 'funs.'+get_em[k][i].replace('[]','ls').replace(' ,',',').replace(', ',',').replace(' ','_')
            fun_all.append(n)
    return funs,asks,call,fun_all,fun_sheet
home,slash = ff.homeIt()
