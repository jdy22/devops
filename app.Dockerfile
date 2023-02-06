# to build this image, you want to start with the base image (googled for python base image)
# /app is the base working directory. any commands and paths will be relative to /app. if you want an absolute path then put a "\" first
FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential python3.10-venv

# FROM python:3.10.0-alpine (cannot have 2 FROMs)
# WORKDIR /app

# Enable venv
# read this https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install PANDOC (need texlive)
RUN apt-get install -y pandoc
RUN apt-get install -y texlive

# copy everything from root folder, to /app folder inside the image
# cmd & entrypoint https://devtron.ai/blog/cmd-and-entrypoint-differences/#:~:text=CMD%3A%20Sets%20default%20parameters%20that,Docker%20containers%20with%20CLI%20parameters.
COPY . .
RUN pip install -r requirements.txt
ENV PORT=8080
CMD ["gunicorn", "--config", "gunicorn_config.py", "wsgi:app"]
EXPOSE 8080

# dockerbuild command picks up this file, and runs the commands in this file to build a docker image
# with the docker image, you can deploy it directly in a container to run your programme
# traditionally you have a server and you package your program in to an .exe file --> but now you can build the
# docker image and deploy it on any container with the docker app and run it.