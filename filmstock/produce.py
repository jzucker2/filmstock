#!/usr/bin/env python3
from app.version import version
from producer.producer import run_cli


if __name__ == "__main__":
    run_cli(version=version)
