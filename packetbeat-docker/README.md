## From docker hub

You can also pull the image from Docker Hub and run it like this:

    docker run --cap-add=NET_ADMIN --network=host -e KIBANA="https://6a16d771c4fc3be7f251c7c629a421e2.us-east-1.aws.found.io:9243" -e HOST="https://d322f42d01dc50c50dba0b446e6a1c0a.us-east-1.aws.found.io:9243" -e PASS="pwkbZXIB3VMPtr4wOnpLNi8c"  shantanuo/packetbeat-agent
    

## Thanks

* [@dansowter](https://github.com/dansowter) for providing a starting point in [this ticket](https://github.com/packetbeat/packetbeat/issues/13).
* [Jan Lelis](https://github.com/janlelis) for the help.
