# python theano_tsne_using_updates.py 1000;
# sleep 2;

# python theano_tsne_using_updates.py 1000;
# sleep 2;

# THEANO_FLAGS=mode=FAST_RUN,device=gpu,lib.cnmem=1 python theano_tsne_using_updates_and_gpu.py 1000;
# sleep 2;

# THEANO_FLAGS=mode=FAST_RUN,device=gpu,lib.cnmem=1,floatX=float32 python theano_tsne_using_updates_and_gpu.py 1000;
# sleep 2;

THEANO_FLAGS=mode=FAST_RUN,device=gpu,lib.cnmem=1,floatX=float32,profile=True python theano_tsne_updates_no_scan.py 1000;
sleep 2;

THEANO_FLAGS=mode=FAST_RUN,device=gpu,lib.cnmem=1,floatX=float32 python theano_tsne_updates_no_scan.py 1000;
sleep 2;

THEANO_FLAGS=mode=FAST_RUN,device=gpu,lib.cnmem=1,floatX=float32 python theano_tsne_no_scan_at_all.py 1000;
sleep 2;

# THEANO_FLAGS=mode=FAST_RUN,device=gpu python theano_tsne_using_updates.py 60;
# sleep 2;

python numpy_tsne.py 1000;
sleep 2;

python numpy_tsne.py 1000;
sleep 2;

# nohup bash run_performance.sh  > output.log 2>&1 &