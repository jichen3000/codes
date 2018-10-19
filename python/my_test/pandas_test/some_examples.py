# pandas packeg python as R, based on numpy
import numpy as np
import pandas as pd

from StringIO import StringIO

if __name__ == '__main__':
    from minitest import *
    only_test("load")

    with test(pd.DataFrame):
        x = np.arange(12).reshape(3,4)
        n,m = x.shape
        row_names = ["row_"+str(i) for i in range(n)]
        col_names = ["col_"+str(i) for i in range(m)]
        df = pd.DataFrame(data=x, 
                index=row_names, columns=col_names)
        df.pp()

        # just like R
        df.describe().pp() 

        df['col_0'].value_counts().pp()

        # df['col_0'].qcut(2,labels=False).pp()
        pd.qcut(df['col_0'], 2,labels=False).pp()

        df.cumsum().pp()


    with test("save"):
        # sudo pip install tables
        x = np.arange(12).reshape(3,4)
        n,m = x.shape
        row_names = ["row_"+str(i) for i in range(n)]
        col_names = ["col_"+str(i) for i in range(m)]
        df = pd.DataFrame(data=x, 
                index=row_names, columns=col_names)

        hdf5_db = pd.HDFStore("example.h5")
        hdf5_db["test_df"] = df

    with test("load"):
        hdf5_db = pd.HDFStore("example.h5")
        hdf5_db["test_df"].pp()




