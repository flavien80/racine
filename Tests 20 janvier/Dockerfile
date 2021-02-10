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
COPY jobber.txt /home/root/
RUN cat /home/root/jobber.txt > /home/jobberuser/.jobber
USER jobberuser
COPY ipfsbackup.sh .
COPY ipfsbackuperror.sh .
COPY cassandrabackup.sh .
COPY cassandrabackuperror.sh .
COPY ipfsbackup.py .
