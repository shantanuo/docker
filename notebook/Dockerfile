FROM continuumio/miniconda3
RUN /opt/conda/bin/conda install jupyter -y --quiet
EXPOSE 8888
RUN cd /tmp/
RUN apt-get update
RUN apt-get install --yes python-pydot
RUN conda install --yes -c conda-forge fastparquet pydotplus
RUN pip install -U numpy seaborn sklearn
CMD ["/opt/conda/bin/jupyter", "notebook", "--NotebookApp.token='india'", "--notebook-dir=/tmp/", "--ip='0.0.0.0'", "--port=8888", "--no-browser", "--allow-root"]
