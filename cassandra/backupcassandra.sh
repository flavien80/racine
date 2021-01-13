cd /backups/
mkdir cassandra
cqlsh localhost
nodetool snapshot
for dossier in 'find -name snapshots'
  cp -r dossier /backups/cassandra
restic -r /backups/cassandra --verbose backup ~/work
