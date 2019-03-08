FROM python:3.6
WORKDIR /app/
ADD . /app/
RUN pip install -r altikelime/requirements.txt
CMD ["python", "./altikelime/manage.py runserver"]
