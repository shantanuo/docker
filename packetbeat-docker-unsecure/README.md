## From docker hub

You can also pull the image from Docker Hub and run it like this:

    docker run --cap-add=NET_ADMIN --network=host -e KIBANA="http://shantanuoak.com:5601" -e HOST="http://shantanuoak.com:9200" shantanuo/packetbeat-agent-unsecure
    

## Thanks

* [@dansowter](https://github.com/dansowter) for providing a starting point in [this ticket](https://github.com/packetbeat/packetbeat/issues/13).
* [Jan Lelis](https://github.com/janlelis) for the help.
