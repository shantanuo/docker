FROM 763104351884.dkr.ecr.us-east-1.amazonaws.com/tensorflow-training:1.13-cpu-py36-ubuntu16.04 
RUN pip install jupyter
EXPOSE 8888
RUN cd /tmp/
CMD ["/opt/conda/bin/jupyter", "notebook", "--NotebookApp.token='india'", "--notebook-dir=/tmp/", "--ip='0.0.0.0'", "--port=8888", "--no-browser", "--allow-root"]
