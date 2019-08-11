FROM ubuntu

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
 && pip install boto3
 
# Copy Build Thumbnail script to Docker image and add execute permissions
COPY build-thumbnails.py build-thumbnails.py

RUN chmod +x build-thumbnails.py
  
