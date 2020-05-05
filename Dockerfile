FROM python:3.8

COPY auction.py auction.py
CMD ["python", "auction.py"]
