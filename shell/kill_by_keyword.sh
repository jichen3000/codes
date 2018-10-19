## declare an array variable
declare -a arr=("ruby app" "ruby verify")

## now loop through the above array
for i in "${arr[@]}"
do
   echo "handle $i"
   pid=`ps aux|grep '$i'| grep -v grep | awk '{print $2}'`
   # or do whatever with individual element of the array
done