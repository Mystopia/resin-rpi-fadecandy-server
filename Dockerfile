FROM resin/raspberry-pi3-python

# Enable systemd
ENV INITSYSTEM on

RUN mkdir /app
COPY . /app/

RUN pip install -r /app/requirements.txt
RUN git clone https://github.com/scanlime/fadecandy.git /opt/fadecandy

WORKDIR /app

CMD ["supervisord", "-c", "/app/supervisord.conf"]
