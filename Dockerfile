FROM python

WORKDIR /usr/src/app

COPY ./todopy .

CMD ["python", "./runapp.py"]
