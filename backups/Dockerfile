FROM jobber:latest
USER root
ENV RESTIC_PASSWORD="root"
RUN apk update
RUN apk add restic
RUN apk add python3
RUN restic init --repo /backups
RUN pip3 install --upgrade ipfshttpclient
COPY init.sh /bin/bash/
ENTRYPOINT /bin/bash/init.sh
