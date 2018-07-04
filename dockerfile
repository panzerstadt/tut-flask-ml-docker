FROM continuumio/anaconda3
MAINTAINER TLQ, https://liquntang.wordpress.com/
COPY ./ml_dockerize /usr/local/python/
EXPOSE 5000
WORKDIR /usr/local/python/
RUN pip install -r requirements.txt
CMD python app.py