FROM centos/python-38-centos7
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN python manage.py makemigrations && python manage.py migrate
RUN python manage.py migrate