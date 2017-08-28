FROM willfarrell/filebeat:5

# Install deps
RUN apk add --no-cache --virtual .run-deps curl jq python

COPY filebeat.yml /etc/filebeat/filebeat.yml
COPY strip.py /strip.py
COPY tag.py /tag.py

COPY docker-entrypoint.sh  /
ENTRYPOINT ["/docker-entrypoint.sh"]

CMD [ "filebeat", "-e", "-c", "/etc/filebeat/filebeat.yml"]