FROM python:3.7-slim

COPY . /opt/code_predict

WORKDIR /opt/code_predict

ENV PYTHONPATH /opt:$PYTHONPATH
ENV HTTP "http://"
ENV HTTPS "https://"
ENV OSM_SERVER_IP "35.228.24.23"
ENV NBI_PORT "9999"
ENV NBI_SERVER_PORT $OSM_SERVER_IP:$NBI_PORT
ENV OSM_SOCKET_ADDR $HTTP$OSM_SERVER_IP
ENV NBI_SOCKET_ADDR $HTTPS$NBI_SERVER_PORT
ENV NBI_AUTHENTICATION_URL $NBI_SOCKET_ADDR"/osm/admin/v1/tokens"
ENV PREDICTOR_MODEL ARIMA

RUN pip install -U pip
RUN pip install -r requirements.txt

ENTRYPOINT [ "/opt/code_predict/docker-entrypoint-controller.sh" ]
