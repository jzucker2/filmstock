# Examples

A sample `Dockerfile` below:

```
ARG FILMSTOCK_VERSION=0.2.0
FROM ghcr.io/jzucker2/filmstock:${FILMSTOCK_VERSION} AS linux_base

FROM linux_base AS pip_setup
ARG PIP_VERSION=22.1.2
RUN pip install pip==${PIP_VERSION}

FROM pip_setup AS python_dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM python_dependencies AS source_code
COPY /demo /demo
WORKDIR /demo

ENV FLASK_APP=app

FROM source_code AS db_setup
RUN ["flask", "db", "upgrade"]

FROM db_setup AS seed_initial_data
RUN ["python", "seed_initial_data.py"]

FROM seed_initial_data AS run_server
# can use `run_dev.sh` or `run_prod.sh`
CMD ["sh", "run_dev.sh"]
```
