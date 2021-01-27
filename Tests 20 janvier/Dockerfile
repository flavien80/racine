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
COPY ipfsbackup.sh /bin/bash
COPY ipfsbackuperror.sh /bin/bash
COPY cassandrabackup.sh /bin/bash
COPY cassandrabackuperror.sh /bin/bash
COPY ipfsbackup.py /bin/bash
ENTRYPOINT /bin/bash
