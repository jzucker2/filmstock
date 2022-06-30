FROM python:3.10 AS linux_base

# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=998232
ENV CARGO_NET_GIT_FETCH_WITH_CLI=true

FROM linux_base AS debian_base

# install deps
RUN apt-get update -y && apt-get install -y \
        xz-utils \
        libffi-dev \
        libssl-dev \
        gcc \
        git \
        build-essential \
        python3-dev \
    && apt-get clean

FROM debian_base as install_rust

RUN echo "Print HOME ..."
RUN echo "$HOME"

## Add .cargo/bin to PATH
ENV PATH="/root/.cargo/bin:${PATH}"

RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

RUN echo "install rust, now source rust"
# rustup says to run this!
RUN . $HOME/.cargo/env

RUN echo "done setting cargo env"

# Check cargo is visible
RUN cargo --help

FROM install_rust AS pip_setup

ARG PIP_VERSION=22.1.2
RUN pip install pip==${PIP_VERSION}

FROM pip_setup AS python_dependencies
COPY requirements.txt requirements.txt


RUN pip install -r requirements.txt

FROM python_dependencies as clean_up

RUN rustup self uninstall -y \
  && rm -rf /root/.cache /root/.cargo /tmp/* /var/lib/apt/lists/*

FROM clean_up AS test_build

COPY /test.sh /test.sh

# can use `run_dev.sh` or `run_prod.sh`
CMD ["sh", "test.sh"]
