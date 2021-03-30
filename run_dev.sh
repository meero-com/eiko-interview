#!/bin/sh

export PYTHONPATH=src
exec uvicorn mini_eiko.app:app --reload --reload-dir ./src --log-config logging.conf.json
