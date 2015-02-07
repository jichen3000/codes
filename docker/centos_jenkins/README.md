# docker-centos-jenkins

A Dockerfile that produces a CentOS-based Docker image that will run the latest stable [Jenkins][jenkins].

The build is based on [centos:7].

[Jenkins]: http://jenkins-ci.org/

## Included packages (and their dependencies)

* wget
* Jenkins
* OpenJDK 1.7

## Image Creation


```
$ docker build -t="jichen3000/centos7-jenkins" .
```


## Container Creation / Running


``` shell
$ docker run -d -name="cj" \
             -p 54321:8080 \
	     jichen3000/centos7-jenkins
$ iptables -I INPUT 1 -p tcp --dport 54321 -j ACCEPT
```



