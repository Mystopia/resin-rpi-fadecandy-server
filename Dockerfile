FROM resin/raspberry-pi3-python

# Enable systemd
ENV INITSYSTEM on

RUN apt update \
  && apt install -yq --no-install-recommends dropbear \
  && apt clean
  && rm -rf /var/lib/apt/lists/*

RUN mkdir /app
COPY . /app/

RUN pip install -r /app/requirements.txt
RUN git clone https://github.com/scanlime/fadecandy.git /opt/fadecandy

WORKDIR /app

CMD ["supervisord", "-c", "/app/supervisord.conf"]
