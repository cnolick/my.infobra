FROM python:3.6
ADD . /
WORKDIR /site
RUN pip install -r requirements.txt
CMD ["python", "app.py"]