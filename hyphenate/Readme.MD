docker run --disable-content-trust -it shantanuo/hyphenate ./example ../dicts/hyph_mr_IN.dic /hi_sample.text

```
वि=त्त
वि=त्‍त
वि=त्‌त
उप=क्र=मा=वर=च्या=ही=च
उप=क्र=मा=वर=च्या=ही=बद्दल=चा
वि=त्‌=त=वान
वि=त्‍त=वान
```
Or you can mount /tmp/ folder inside the container and run the commands on text files saved on host server within /tmp/ folder.

docker run --disable-content-trust -v /tmp/:/tmp/ -it shantanuo/hyphenate ./example /tmp/hyph_mr_IN.dic /tmp/hi_sample.text
