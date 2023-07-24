FROM python:3
COPY . /USR/SRC/APP
WORKDIR /USR/SRC/APP
RUN pip install -r requirements.txt
CMD python main.py