# AWS Tutorial

http://cs231n.github.io/aws-tutorial/

## build Amazon Machine Image

### choose location to N.California

### Create Instance

launch an instance

steps:

1. 

Udacity Tensorflow - ami-e6ade686
it based on cs231n_caffe_torch7_keras_lasagne_v2


## ssh
\# notice, the username will dependen on os, this is for ubuntu
\# http://stackoverflow.com/questions/18551556/permission-denied-publickey-when-ssh-access-to-amazon-ec2-instance
chmod 400 ~/.ssh/ec2_private_key.pem

ssh -i ~/.ssh/ec2_private_key.pem ubuntu@54.183.85.174

## aws-cli
sudo pip install awscli

\# create keys
https://console.aws.amazon.com/iam/home?#/security_credential

aws configure


json, text, or table

aws ec2 help

aws ec2 describe-instances --instance-ids i-0c7fa3add1ccc7df7 | grep PublicIpAddress
--filters

elastic ip: 52.52.204.109
instances:
ec2-gpu     i-0e3f3f00a86d384cd g2.2xlarge  us-west-1c  52.8.188.18
ec2-test    i-0c7fa3add1ccc7df7 t2.micro    us-west-1c  52.52.204.190

## install opencv
sudo apt-get update
sudo apt-get install graphviz
sudo apt-get install python-opencv
conda install opencv

## copy
scp ec2-gpu:/home/ubuntu/work/caffe_examples/dog_cat/result.log result.log
scp ec2-gpu:/home/ubuntu/work/caffe_examples/dog_cat/solver.prototxt  solver.prototxt  
scp ec2-gpu:/home/ubuntu/work/caffe_examples/dog_cat/train.prototxt  train.prototxt  
scp ec2-gpu:/home/ubuntu/work/caffe_examples/dog_cat/validation.prototxt  validation.prototxt
scp ec2-gpu:/home/ubuntu/work/caffe_examples/dog_cat/snapshots_iter_10000.caffemodel  snapshots_iter_10000.caffemodel
scp ec2-gpu:/home/ubuntu/work/caffe_examples/dog_cat/snapshots_iter_10000.solverstate  snapshots_iter_10000.solverstate

## 
ec2_ins.py

## timezone on ubuntu
sudo timedatectl set-timezone America/Los_Angeles

http://askubuntu.com/questions/323131/setting-timezone-from-terminal

