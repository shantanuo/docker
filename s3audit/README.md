Based on this medium article:

https://medium.com/the-scale-factory/securing-s3-buckets-with-s3audit-a8cb989cb861

Help from stack overflow:

https://stackoverflow.com/questions/58282220/can-not-create-an-image-because-of-failing-go-command

How to use this image?

docker build -t shantanuo/pm .

docker run --disable-content-trust  -it  shantanuo/pm sh

/ # ./aws-vault add home

Enter Access Key ID:

/ # ./aws-vault exec home -- s3audit

