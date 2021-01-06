FROM jobber:latest
USER root
ENV RESTIC_PASSWORD="root"
RUN apk update
RUN apk add restic
RUN apk add python3
RUN restic init --repo /backups
RUN jobber init
RUN cat jobber.txt > /home/rec/.jobber
RUN pip3 install --upgrade runrestic
RUN pip3 install --upgrade ipfsApi
ENTRYPOINT /bin/bash
