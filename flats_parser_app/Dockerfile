FROM ubuntu:20.04
RUN mkdir /src
COPY ./ /src/
WORKDIR /src
RUN apt-get update \
    && apt-get -y install libpq-dev gcc python3.8 python3-pip \
    && pip install psycopg2

# You should install the dependencies required to run the browsers.
# There's no need to install chromium separately
RUN apt-get install -y libnss3 libasound2 libgbm-dev

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
# python3 -m
# Install playwright and then its dependencies (the browsers)
RUN pip3 install playwright
RUN playwright install
RUN playwright install-deps

CMD ["python3","app.py"]
