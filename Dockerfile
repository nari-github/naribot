FROM python:3.11
WORKDIR /bot
COPY requirements.txt /bot/
RUN pip install -r requirements.txt
RUN pip install requests
COPY . /bot
CMD python main.py

