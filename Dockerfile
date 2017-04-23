FROM resin/raspberry-pi3-python

# Enable systemd
ENV INITSYSTEM on

# RUN apt update \
#   && apt install -yq --no-install-recommends dropbear \
#   && apt-get clean && rm -rf /var/lib/apt/lists/*

# Change root password
# Insecure default password
# RUN echo "root:resin" | chpasswd
# RUN export PASSWD=${PASSWD:=root} \
#   # && openssl rand -base64 6 \
#   && echo "root:$PASSWD" | chpasswd

RUN mkdir /app \
  && git clone https://github.com/scanlime/fadecandy.git /opt/fadecandy

COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["supervisord", "-c", "/app/supervisord.conf"]
