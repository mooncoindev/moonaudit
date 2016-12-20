# moonaudit
creates a list of transactions which are equal to or greater than 29,000,000 MOON.  
  
once the script is within 5 blocks (this value is configurable) from the last block in the chain, it will pause for a few seconds and check again; enabling a realtime continually updating list to be created.  
  
# how to use
the following variables in moonaudit.py need to be set:  
  
*rpchost = '127.0.0.1'*  
*rpcuser = 'rpcuser'*  
*rpcpass = 'rpcpass'*  
*txnconf = 5*  
  
once set correctly, launch the script:  
  
*python moonaudit.py > all_moon_spends.log*  

to leave running permanently:  
  
*echo "python moonaudit.py > all_moon_spends.log" > moonaudit.sh*  
*chmod +x moonaudit.sh*  
*screen ./moonaudit.sh*
