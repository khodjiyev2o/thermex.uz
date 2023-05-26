#!/bin/sh
echo "restarting gunicorn..."
sudo systemctl restart allinsan-backend.service
echo "gunicorn restarted"
