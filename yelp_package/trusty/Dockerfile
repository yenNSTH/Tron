FROM ubuntu:trusty

RUN apt-get update > /dev/null && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        debhelper \
        dpkg-dev \
        devscripts \
        python-pip \
        wget \
        gdebi-core \
        gcc \
        python-dev \
        coffeescript \
        libyaml-dev \
        libssl-dev \
        libffi-dev \
        && apt-get clean > /dev/null

RUN cd /tmp && \
    wget http://mirrors.kernel.org/ubuntu/pool/universe/d/dh-virtualenv/dh-virtualenv_1.0-1_all.deb && \
    gdebi -n dh-virtualenv*.deb && \
    rm dh-virtualenv_*.deb

WORKDIR /work
