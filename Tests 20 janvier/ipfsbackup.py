import ipfshttpclient
config="/ipfs/QmQU9bpGsg6G1C9knbXK7ztzVvjjDTYhsFfE3f55CT31MK"
repolist="/ipfs/QmR8KEqwEhjwEzYefHub9hjfFTwpYSn9tLsfFv4anbHCCi"
node001="/ipns/Qmcir6CzDtTZvywPt9N4uXbEjp3CJeVpW6CetMG6f93QNt"
cconf="/ipns/QmaAAZor2uLKnrzGCwyXTSwogJqmPjJgvpYgpmtz5XcSmR"
node002="/ipns/Qmb2paHChFzvU9fnDtAvmpbEcwyKfpKjaHc67j4GCmWLZv"
keyrepolist="/ipns/QmcRWARTpuEf9E87cdA4FfjBkv7rKTJyfvsLFTzXsGATbL"
client = ipfshttpclient.connect("/dns/ipfs/tcp/5001")

configtxt = api.get(config)
sourceconfig = open(configtxt, 'r')
destconfig = open("/backups/config.txt", 'w')
while(line in sourceconfig):
    destconfig.write(line)
    
repolisttxt = api.get(repolist)
sourcerepolist = open(repolisttxt, 'r')
destrepolist = open("/backups/repolist.txt", 'w')
while(line in sourcerepolist):
    destrepolist.write(line)

node001txt = api.get(node001)
sourcenode001 = open(node001txt, 'r')
destnode001 = open("/backups/node001.txt", 'w')
while(line in sourcenode001):
    destnode001.write(line)

cconftxt = api.get(cconf)
sourcecconf = open(cconftxt, 'r')
destcconf = open("/backups/cconf.txt", 'w')
while(line in sourcecconf):
    destcconf.write(line)

node002txt = api.get(node002)
sourcenode002 = open(node002txt, 'r')
destnode002 = open("/backups/node002.txt", 'w')
while(line in sourcenode002):
    destnode002.write(line)

keyrepolisttxt = api.get(keyrepolist)
sourcekeyrepolist = open(keyrepolisttxt, 'r')
destkeyrepolist = open("/backups/keyrepolist.txt", 'w')
while(line in sourcekeyrepolist):
    destkeyrepolist.write(line)
# https://python-ipfs-api.readthedocs.io/en/latest/api_ref.html
