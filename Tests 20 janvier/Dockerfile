FROM jobber:latest
USER root
ENV RESTIC_PASSWORD="root"
RUN apk update
RUN apk add restic
RUN apk add python3
RUN restic init --repo /backups
RUN pip3 install --upgrade ipfshttpclient
RUN cd /home/jobberuser
RUN mkdir jobber
RUN cd jobber
RUN touch runlog.txt
RUN touch jobber.log
RUN cd /backups/
RUN touch config.txt
RUN touch repolist.txt
RUN touch node-001.txt
RUN touch cconf.txt
RUN touch node-002.txt
RUN touch keyrepolist.txt
COPY jobber.txt /home/root/
RUN cat /home/root/jobber.txt > /home/jobberuser/.jobber
COPY ipfsbackup.sh /home/jobberuser
COPY ipfsbackuperror.sh /home/jobberuser
COPY cassandrabackup.sh /home/jobberuser
COPY cassandrabackuperror.sh /home/jobberuser
COPY ipfsbackup.py /home/jobberuser
USER jobberuser
