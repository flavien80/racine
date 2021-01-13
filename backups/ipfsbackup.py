import ipfshttpclient
import sys
#ipadress="/ip4/5.196.67.240/tcp/4001/ipfs/QmTdxazXmX1PUfKWUXGddDW4GeaktwKni8GSjjHhWi2Lgz"
hash="TOBECOMPLETED"
client = ipfshttpclient.connect()
filetobackup = api.get(hash)
f = open(filetobackup, 'r')
f2 = open(path+"/"+sys.argv[1], 'w')
while(line in f):
    f2.write(line)
# https://python-ipfs-api.readthedocs.io/en/latest/api_ref.html