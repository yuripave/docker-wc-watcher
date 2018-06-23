FROM python:3

RUN git clone git://github.com/ImDevinC/wc-watcher src \
    && cd src \
    && pip install -r requirements.txt \
    && rm -rf /root/.cache

COPY private.py /src

CMD ["python", "/src/soccerbot.py"]
