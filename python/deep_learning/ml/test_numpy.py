# 
# https://github.com/pbharrin/machinelearninginaction
from numpy import *

rand_mat = mat(random.rand(4,4))
# rand_mat = mat([[ 0.84619051,  0.44630556,  0.03616869,  0.0597108 ],
#  [ 0.49604674,  0.11992932,  0.5527096 ,  0.65262131],
#  [ 0.54697695,  0.11936534,  0.96405258,  0.23149131],
#  [ 0.83873332,  0.29457607,  0.81256088,  0.05259617]])
print rand_mat
print rand_mat.I

print eye(4)

np.random.randint(5, size=(2, 4))

# get data set
# http://archive.ics.uci.edu/ml/


np.unique(labels[...,0], return_counts=True)