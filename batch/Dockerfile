FROM ubuntu
ARG DEBIAN_FRONTEND=noninteractive

# Install required software via apt and pip
RUN apt-get -y update && \
	apt-get install -y \
    awscli \
    python \
    python-pip \
    software-properties-common \
 && add-apt-repository ppa:ubuntugis/ppa \
 && apt-get -y update \
 && apt-get install -y \
 	gdal-bin \
 && pip install boto3 feedparser bs4 requests

# Copy Build Thumbnail script to Docker image and add execute permissions
ADD ./build-thumbnails.py build-thumbnails.py
ADD ./git-urls.py git-urls.py

RUN chmod +x *.py 
  
