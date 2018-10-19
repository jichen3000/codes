/home/ubuntu/caffe/build/tools/caffe train --solver /home/ubuntu/work/caffe_examples/dog_cat/solver_1.prototxt
# echo -n "Enter any key to stop shutdown in 20 seconds > "
# if read -n 1 -t 20 response; then
#     echo; echo "Shutdown stops!"
# else
# fi

echo; echo "Shutdown now..."
python send_mail.py "Test finised!" ./result_01.log
sudo shutdown -h now

# nohup ./train.sh >result_01.log 2>&1 &