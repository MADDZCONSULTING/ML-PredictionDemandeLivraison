FROM tiangolo/uwsgi-nginx-flask:python3.7

# Update to the latest PIP
RUN pip3 install --upgrade pip

RUN pip3 install Flask==1.0.2 \
                flask-inputs==0.3.0 \
                jsonschema==3.0.1 \
                pytest==4.6.2

# Our application code will exist in the /app2 directory,
# so set the current working directory to that
WORKDIR /app

# Backup the default app2 files.  You could also delete these
RUN mkdir bak && \
    mv main.py uwsgi.ini bak


# Copy our files into the current working directory WORKDIR
COPY ./ ./

# install our dependencies
RUN  pip3 install -r requirements.txt