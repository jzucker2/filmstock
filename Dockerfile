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
# Add .cargo/bin to PATH
ENV PATH="/root/.cargo/bin:${PATH}"

ARG RUST_VERSION=1.61.0
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y --default-toolchain ${RUST_VERSION}

RUN echo "install rust, now source rust"
# rustup says to run this after install!
RUN . $HOME/.cargo/env
RUN echo "done setting cargo env"
# Check cargo is visible
RUN cargo --help

FROM install_rust AS pip_setup
COPY pip-requirements.txt pip-requirements.txt
RUN pip install -r pip-requirements.txt

FROM pip_setup AS python_dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM python_dependencies as clean_up

# remove existing `requirements.txt` to prevent clashes
RUN rm requirements.txt
RUN rm pip-requirements.txt

RUN rustup self uninstall -y \
  && rm -rf /root/.cargo
#  && rm -rf /root/.cache /root/.cargo /tmp/* /var/lib/apt/lists/* \

FROM clean_up AS configure
ENV PROMETHEUS_MULTIPROC_DIR /tmp
ENV prometheus_multiproc_dir /tmp
ENV METRICS_PORT 9200

FROM configure AS test_build
COPY /scripts /filmstock/scripts
CMD ["sh", "filmstock/scripts/test.sh"]
