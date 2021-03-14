FROM python:3.7

# Enable output to console
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /code

RUN pip install gunicorn

# Install Dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /code/

RUN chmod +x ./entry.sh

EXPOSE 8000

CMD ["/code/entry.sh"]

