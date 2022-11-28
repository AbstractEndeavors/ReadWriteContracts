import functions as f
import currFun.do_it as do
import currFun.funcSheet as funs
import subprocess
import clipboard
import json
def print_scan():
    spl = 'api.'
    if 'api-' in scanners:
        li = scanners.split(spl.replace('.','-'))[1]
    print('https://'+li+'/address/'+str(add))
    clipboard.copy('https://'+li+'/address/'+str(add))
    return 'https://'+li
def sendIt():
    tx = json.loads(str(do.txt).replace("'",'"'))
    tx["nonce"] = w3.eth.getTransactionCount(f.check_sum(tx['from']))
    tx["gas"] = int(tx["gas"]+(tx["gas"]/2))
    tx["gasPrice"] = int(tx["gasPrice"]+(tx["gasPrice"]/2))
    signed_tx = w3.eth.account.sign_transaction(tx, priv)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    p = subprocess.Popen(["firefox", str(print_scan())+'/tx/'+str(tx_hash.hex())])
global scanners,net,ch_id,main_tok,file,w3,network,priv,add
w3 = funs.w3
