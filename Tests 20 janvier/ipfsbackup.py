import ipfshttpclient
config="/ipfs/QmQU9bpGsg6G1C9knbXK7ztzVvjjDTYhsFfE3f55CT31MK"
repolist="/ipfs/QmR8KEqwEhjwEzYefHub9hjfFTwpYSn9tLsfFv4anbHCCi"
node001="/ipns/Qmcir6CzDtTZvywPt9N4uXbEjp3CJeVpW6CetMG6f93QNt"
cconf="/ipns/QmaAAZor2uLKnrzGCwyXTSwogJqmPjJgvpYgpmtz5XcSmR"
node002="/ipns/Qmb2paHChFzvU9fnDtAvmpbEcwyKfpKjaHc67j4GCmWLZv"
keyrepolist="/ipns/QmcRWARTpuEf9E87cdA4FfjBkv7rKTJyfvsLFTzXsGATbL"
client = ipfshttpclient.connect(addr="/dns/ipfs/tcp/5001")

client.get(config,"/backups")
client.get(repolist,"/backups")
node001txt = client.get(node001,"/backups")
cconftxt = client.get(cconf,"/backups")
node002txt = client.get(node002,"/backups")
keyrepolisttxt = client.get(keyrepolist,"/backups")
