FROM python:3.8

COPY config.json config.json
COPY auction.py auction.py
CMD ["python", "auction.py"]
