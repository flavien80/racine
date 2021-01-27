FROM jobber:latest
USER root
ENV RESTIC_PASSWORD="root"
RUN apk update
RUN apk add restic
RUN apk add python3
RUN cd / && mkdir backups
RUN restic init --repo /backups
RUN pip3 install --upgrade ipfshttpclient
RUN cd /home/jobberuser && mkdir jobber && cd jobber && touch runlog.txt && touch jobber.log
RUN cd /backups/ && touch config.txt && touch repolist.txt && touch node-001.txt && touch cconf.txt && touch node-002.txt && touch keyrepolist.txt
COPY jobber.txt /home/root/
RUN cat /home/root/jobber.txt > /home/jobberuser/.jobber
COPY ipfsbackup.sh /home/jobberuser
COPY ipfsbackuperror.sh /home/jobberuser
RUN (ls /home/jobberuser/ipfsbackup.sh && echo "Mon fichier existe") || echo "Mon fichier n'existe pas"
COPY cassandrabackup.sh /home/jobberuser
COPY cassandrabackuperror.sh /home/jobberuser
COPY ipfsbackup.py /home/jobberuser
USER jobberuser
