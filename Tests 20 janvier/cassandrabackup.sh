#!/bin/sh
cd /backups/
mkdir cassandra
cqlsh root
nodetool snapshot
for dossier in 'find -name snapshots'
do
  cp -r dossier /backups/cassandra
done
EXIT
restic -r /backups/cassandra --verbose backup ~/work
