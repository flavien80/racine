FROM ubuntu
RUN apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install apache2
RUN apt-get -y install libapache2-mod-php
COPY index.html /var/www/html
COPY 01-www.example.com.conf /etc/apache2/sites-available/01-www.example.com.conf
RUN mkdir /var/www/html/www.example.com/
RUN cp /var/www/html/index.html /var/www/html/www.example.com
RUN a2ensite 01-www.example.com
ENTRYPOINT /etc/init.d/apache2 start; /bin/bash
WORKDIR /var/www/html
EXPOSE 80
