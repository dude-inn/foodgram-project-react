FROM python:3.7-slim
WORKDIR /app
COPY . .
RUN pip3 install --upgrade pip setuptools --no-cache-dir
RUN pip3 install -r requirements.txt --no-cache-dir
CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]
LABEL author='dude-inn' version=1.0
