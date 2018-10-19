import numpy as np
import lmdb
import caffe

def read_by_key(lmdb_file_name):
    env = lmdb.open(lmdb_file_name, readonly=True)
    with env.begin() as txn:
        raw_datum = txn.get(b'00000000')

        datum = caffe.proto.caffe_pb2.Datum()
        datum.ParseFromString(raw_datum)

        flat_x = np.fromstring(datum.data, dtype=np.uint8)
        x = flat_x.reshape(datum.channels, datum.height, datum.width)
        y = datum.label
        print("x.shape", x.shape)

def read_one_by_one(lmdb_file_name):
    env = lmdb.open(lmdb_file_name, readonly=True)
    with env.begin() as txn:
        cursor = txn.cursor()
        # for test in ipython
        # key = cursor.key()
        # value = cursor.value()
        for key, value in cursor:
            print("key:",key)
            raw_datum = value

            datum = caffe.proto.caffe_pb2.Datum()
            datum.ParseFromString(raw_datum)

            flat_x = np.fromstring(datum.data, dtype=np.uint8)
            x = flat_x.reshape(datum.channels, datum.height, datum.width)
            y = datum.label
            print("x.shape", x.shape)
# with env.begin() as txn:
#     cursor = txn.cursor()
#     for key, value in cursor:
#         print(key, value)

# read_by_key('mylmdb')
read_one_by_one('mylmdb')