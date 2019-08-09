# Voyager Blog Samples

git clone https://github.com/shantanuo/voyager-samples.git

cd voyager-samples

cd aws-batch-naip-thumbs/

docker build -t vg-gdal .

docker run -e "AWS_ACCESS_KEY_ID=xxx" -e "AWS_SECRET_ACCESS_KEY=xxx" -it vg-gdal /usr/bin/python build-thumbnails.py aws-naip-voyager al/2019/ voyager-aws-naip2
_____

docker login

docker tag vg-gdal shantanuo/vg-gdal:latest

docker push shantanuo/vg-gdal
