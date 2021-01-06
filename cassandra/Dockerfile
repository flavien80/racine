FROM jobber
USER root
RUN apk update
RUN apk add restic
RUN apk add python3
RUN restic init --repo /backups
RUN jobber init

ENTRYPOINT /bin/bash
