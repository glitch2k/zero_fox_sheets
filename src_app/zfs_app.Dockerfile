FROM python

WORKDIR /usr/app/src

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 2584

COPY . .

CMD [ "python", "main.py"]

