# moonaudit
#
# install deps using pip:
# python-bitcoinrpc, json

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import json
import time
import os

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

# user-config section
rpchost = '127.0.0.1'
rpcuser = 'rpcuser'
rpcpass = 'rpcpass'
txnconf = 6

if os.path.isfile('progress.dat'):
   with open('progress.dat', 'r') as progress:
      curblock=int(progress.read())
      progress.closed
else:
   curblock=0
rpcpipe = AuthServiceProxy('http://' + rpcuser + ':' + rpcpass + '@' + rpchost + ':44663')
while(1!=2):
   curblock=curblock+1
   totalblk=rpcpipe.getblockcount()
   if (curblock>totalblk-txnconf):
      with open('/root/moonaudit/progress.dat','w') as progress:
         progress.write(str(curblock-1))
         progress.closed
         exit()
   rawblockhash=rpcpipe.getblockhash(curblock)
   rawblockdata=rpcpipe.getblock(rawblockhash)
   print 'checking block %08d' % (curblock)
   timestamp=find_between(str(rawblockdata),'time\': ',', u\'bits')
   sendnum=0
   for txhash in rawblockdata['tx']:
       sendnum=sendnum+1
       txraw=rpcpipe.getrawtransaction(txhash)
       txdata=rpcpipe.decoderawtransaction(txraw)
       curvout=-1
       for outputs in txdata['vout']:
            curvout=curvout+1
            address = ''
            value = 0
            address = find_between(str(outputs), '[u\'', '\']')
            value = find_between(str(outputs), 'Decimal(\'', '\')')
            if (float(str(value))>28999999.99999999):
               print 'block number: %08d;' % (curblock,) + ' unixtime: ' + timestamp + '; address: ' + address + '; coins sent in one operation: ' + str(value                                                  ) + '; txid of transaction: ' + txhash
               with open('/var/www/moonsend_working.log', 'a') as moonaudit:
                   moonaudit.write('block number: %08d;' % (curblock,) + ' unixtime: ' + timestamp + '; address: ' + address + '; coins sent in one operation:                                                   ' + str(value) + '; txid of transaction: ' + txhash + '\n')
               moonaudit.closed
