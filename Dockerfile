FROM alpine:latest
MAINTAINER guokers@vip.qq.com

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
RUN set -x \
    && apk update \
    && apk add python3-dev \
    && apk add bash \
    && apk add libc-dev \
    && apk add libxml2 \
    && apk add libxslt \
    && apk add libxslt-dev \
    && apk add gcc \
    && apk add linux-headers \
    && apk add g++ \
    && mkdir -p /opt/domain_src

COPY . /opt/domain_src/

RUN set -x \
    && pip3 install -i https://mirrors.aliyun.com/pypi/simple/ -r /opt/domain_src/requirements.txt \
    && chmod +x /opt/domain_src/start.sh \
    && rm -f /var/cache/apk/* \
    && rm -rf /root/.cache \
    && rm -rf /tmp/* 

WORKDIR /opt/domain_src
ENTRYPOINT ["/opt/domain_src/start.sh"]

CMD ["/usr/bin/tail", "-f", "nohup.out"]