echo "IPFS Backup in progress"
python3 ipfsbackup.py
restic -r /backups/ --verbose backup ~/work