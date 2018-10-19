# install

on colin-d

## source
https://github.com/NervanaSystems/neon
http://neon.nervanasys.com/docs/latest/installation.html


## prerequisite

```bash
sudo apt-get update

sudo apt-get install clang-3.5
sudo ln -s /usr/bin/clang-3.5 /usr/bin/clang
sudo ln -s /usr/bin/clang++-3.5 /usr/bin/clang++

clang++ -v

sudo apt-get install libsox-fmt-all libsox-dev sox
sudo apt-get install libcurl4-openssl-dev

export LIBRARY_PATH="/usr/local/cuda/lib64:/usr/local/cuda/lib:/usr/local/lib:/usr/local/cuda-7.5/targets/x86_64-linux/lib"
echo $LIBRARY_PATH

# the above just for aeon

export PATH="/usr/local/cuda/bin:"$PATH
export LD_LIBRARY_PATH="/usr/local/cuda/lib64:/usr/local/cuda/lib:/usr/local/lib:"$LD_LIBRARY_PATH

pip install virtualenv
pip install h5py
pip install pyaml
pip install pkgconfig
```

Additionally

To enable multi-threading operations on a CPU, install OpenBLAS
Enabling Neon to use GPUs requires installation of CUDA SDK and drivers

## install steps:

```bash
git clone https://github.com/NervanaSystems/neon.git
cd neon
make

```

## usage

```bash
. .venv/bin/activate

python -c 'import neon'

python examples/mnist_mlp.py -b gpu

deactivate
```

## System-wide install

```bash
git clone https://github.com/NervanaSystems/neon.git
cd neon
make sysinstall

```
