### test on colin-d



run two times, get the second time

| iteration | theano updates | theano | numpy   | t updates GPU | t min for GPU
| --------- | -------------- | ------ | ------- | ------------- |
| 60        | 8              | 4      | 18      | 54,7          |
| 80        | 13,10          | 21,22  | 24,24   |               |
| 100       | 13,13          | 243    | 30,30   | 21,12         |
| 1000      | 116,116        |        | 304,303 | 119,118       | 105,106
|           |                |        |         |               |
|           |                |        |         |               |
|           |                |        |         |               |
|           |                |        |         |               |
|           |                |        |         |               |

1000 times
numpy: 304,303
numpy, change dy: 162
theano: too long
theano updates: 116,116
t updates GPU: 119,118
t min for GPU, all float32: 105,106
t no scan at all no gpu, change dy: 72, 70
t no scan at all gpu, change dy: 29, 25


Description:    Ubuntu 14.04.4 LTS

Using gpu device 0: GeForce GTX 660 (CNMeM is enabled with initial size: 95.0% of memory, cuDNN 4007)
Memory 2GB
GDDR5
CUDA Cores 960

cpuinfo
model name  : Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz
8 core, 
cpu MHz     : 3958.875
cache size  : 8192 KB

meminfo 
MemTotal:        8116508 kB
