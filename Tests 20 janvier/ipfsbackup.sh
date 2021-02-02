#!/bin/sh
echo "IPFS Backup in progress"
cd /backups
python3 /ipfsbackup.py
restic -r /backups/ --verbose backup ~/work
