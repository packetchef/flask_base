#!/bin/bash
cd /site && /usr/bin/gunicorn --workers 3 --bind 0.0.0.0:7001 wsgi:app
