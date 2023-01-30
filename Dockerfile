FROM python:3.9

ENV GOOGLE_API_KEY=$GOOGLE_API_KEY
USER root
ENV PYTHONUNBUFFERED=1
RUN apt-get update
RUN apt-get install -y cron
WORKDIR /root/youtube-crawler

COPY requirements.txt requirements.txt
RUN chmod 666 -R /etc/cron*
RUN chmod 666 -R /root


RUN python -m pip install --upgrade pip


# RUN apt-get install libgflags-dev libgdal-dev libsnappy-dev zlib1g-dev libbz2-dev liblz4-dev libzstd-dev librocksdb-dev poppler-utils dnsutils -y
RUN pip install --upgrade --no-cache-dir 'setuptools<65'
# RUN service cron start
COPY ./  /root/youtube-crawler/



RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py check
RUN python manage.py crontab add || python manage.py crontab add
RUN chown -R root:root /root/youtube-crawler



EXPOSE 8000

CMD gunicorn youtube_crawler.wsgi:application --bind 0.0.0.0:8000 --workers 1
