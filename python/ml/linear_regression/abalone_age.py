
from regression import *
from numpy import *


if __name__ == '__main__':
    from minitest import *

    with test_case("abalone_age"):

        with test("lwlr"):
            abX,abY=get_dataset_from_file('abalone.dataset')
            yHat01=lwlr_list(abX[0:99],abX[0:99],abY[0:99],0.1)
            yHat1=lwlr_list(abX[0:99],abX[0:99],abY[0:99],1)
            yHat10=lwlr_list(abX[0:99],abX[0:99],abY[0:99],10)
            regress_error(abY[0:99],yHat01.T).must_equal(56.7889824825, key=allclose)
            regress_error(abY[0:99],yHat1.T).must_equal(429.89056187, key=allclose)
            regress_error(abY[0:99],yHat10.T).must_equal(549.118170883, key=allclose)
            yHat1_01=lwlr_list(abX[100:199],abX[0:99],abY[0:99],0.1)
            pass

        with test("overfit"):
            regress_error(abY[100:199],yHat1_01.T).must_equal(45649.712634923126, key=allclose)
            yHat1_1=lwlr_list(abX[100:199],abX[0:99],abY[0:99],1)
            regress_error(abY[100:199],yHat1_1.T).must_equal(573.5261441895808, key=allclose)
            yHat1_10=lwlr_list(abX[100:199],abX[0:99],abY[0:99],10)
            regress_error(abY[100:199],yHat1_10.T).must_equal(517.57119053830979, key=allclose)

            ws = standard_regress(abX[0:99],abY[0:99])
            yHat=mat(abX[100:199])*ws
            # even the most simple standard regress will go well with new points.
            regress_error(abY[100:199],yHat.T.A).must_equal(518.63631532450131, key=allclose)
            pass