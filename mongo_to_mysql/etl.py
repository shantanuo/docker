from continuumio/miniconda3
ADD etl.py /tmp/

RUN pip install requests pandas boto3 fire