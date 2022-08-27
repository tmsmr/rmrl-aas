FROM python:3.10-alpine3.16 as dependency-builder
RUN apk update && apk add --no-cache git build-base freetype-dev jpeg-dev
COPY ./requirements.txt /requirements.txt
RUN pip install --user --no-cache-dir --upgrade -r /requirements.txt

FROM python:3.10-alpine3.16
LABEL org.opencontainers.image.authors="contact@thomas-maier.net"
RUN apk update && apk add --no-cache jpeg
ENV PYTHONUNBUFFERED 1
RUN adduser -S flask \
 && mkdir /app \
 && chown -R flask /app
USER flask
WORKDIR /app
COPY --from=dependency-builder --chown=flask /root/.local /home/flask/.local
ENV PATH=/home/flask/.local/bin:$PATH
COPY rmrl_aas.py /app/rmrl_aas.py
CMD ["waitress-serve", "rmrl_aas:app"]