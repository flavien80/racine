import ipfsApi
ipadress=0
ipfshash="blabla"
api = ipfsApi.Client(host='http://'.ipadress, port=5001)
api.get(ipfshash)
# https://python-ipfs-api.readthedocs.io/en/latest/api_ref.html