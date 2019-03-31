1) Download data:

pip install kaggle

echo '{"username":"shantanuo","key":"c90c207ab8d6c445c54f77c5d5dcdedbx"}' > /root/.kaggle/kaggle.json

cd /tmp/

kaggle competitions download -c jigsaw-toxic-comment-classification-challenge

wget https://raw.githubusercontent.com/shantanuo/docker/master/dlami/tensorflow-vgg-like-charcnn.py

2) Start tensorflow container

docker run -p 8881:8888 -v /tmp/:/tmp/ -d shantanuo/dlami

3) Enter into the container and run the script:

docker exec -it XXXX bash
python /tmp/tensorflow-vgg-like-charcnn.py
