FROM continuumio/anaconda3
MAINTAINER TLQ, https://liquntang.wordpress.com/
EXPOSE 8000
RUN apt-get update && apt-get install -y apache2 apache2-dev vim \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*
WORKDIR /var/www/ml_dockerize/
COPY ./ml_dockerize.wsgi /var/www/ml_dockerize/ml_dockerize.wsgi
COPY ./ml_dockerize /var/www/ml_dockerize
RUN pip install -r requirements.txt
RUN /opt/conda/bin/mod_wsgi-express install-module
RUN mod_wsgi-express setup-server ml_dockerize.wsgi \
    --port=8000 --user www-data \--group www-data \
    --server-root=/etc/mod_wsgi-express-80
CMD /etc/mod_wsgi-express-80/apachectl start -D FOREGROUND
