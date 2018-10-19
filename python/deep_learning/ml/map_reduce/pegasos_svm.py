from mrjob.job import MRJob
import pickle
from numpy import *

class MRsvm(MRJob):
    DEFAULT_INPUT_PROTOCOL = 'json_value'
    def __init__(self, *args, **kwargs):
        super(MRsvm, self).__init__(*args, **kwargs)
        self.data = pickle.load(open('./svmDat27'))
        self.w = 0
        self.eta = 0.69
        self.dataList = []
        self.k = self.options.batchsize
        self.numMappers = 1
        self.t = 1

    def configure_options(self):
        super(MRsvm, self).configure_options()
        self.add_passthrough_option(
            '--iterations', dest='iterations', default=2, type='int',
            help='T: number of iterations to run')
        self.add_passthrough_option(
            '--batchsize', dest='batchsize', default=100, type='int',
            help='k: number of data points in a batch')

    def steps(self):
        return ([self.mr(mapper=self.map, mapper_final=self.map_fin,\
                            reducer=self.reduce)]*self.options.iterations)

    def map(self, mapperId, inVals):
        if False: yield
        if inVals[0]=='w':
            self.w = inVals[1]
        elif inVals[0]=='x':
            self.dataList.append(inVals[1])
        elif inVals[0]=='t': 
            self.t = inVals[1]

    def map_fin(self):
        labels = self.data[:,-1]
        X=self.data[:,0:-1]
        if self.w == 0: 
            self.w = [0.001]*shape(X)[1]
        for index in self.dataList:
            p = mat(self.w)*X[index,:].T
            if labels[index]*p < 1.0:
                yield (1, ['u', index])
        yield (1, ['w', self.w])
        yield (1, ['t', self.t])

    def reduce(self, _, packedVals):
        for valArr in packedVals:
            if valArr[0]=='u':  self.dataList.append(valArr[1])
            elif valArr[0]=='w': self.w = valArr[1]
            elif valArr[0]=='t':  self.t = valArr[1]
        labels = self.data[:,-1]; X=self.data[:,0:-1]
        wMat = mat(self.w);   wDelta = mat(zeros(len(self.w)))
        for index in self.dataList:
            wDelta += float(labels[index])*X[index,:]
        eta = 1.0/(2.0*self.t)
        wMat = (1.0 - 1.0/self.t)*wMat + (eta/self.k)*wDelta
        for mapperNum in range(1,self.numMappers+1):
            yield (mapperNum, ['w', wMat.tolist()[0] ])
            if self.t < self.options.iterations:
                yield (mapperNum, ['t', self.t+1])
                for j in range(self.k/self.numMappers):
                    yield (mapperNum, ['x',\
                    random.randint(shape(self.data)[0]) ])
                    
def predict(weights, x):
    return weights*x.T

def batchPegasos(dataSet, labels, lam, iteration_count, batch_size):
    m,n = shape(dataSet)
    weights = zeros(n)
    row_index_range = range(m)
    for iter_index in range(1, iteration_count+1):
        wDelta = mat(zeros(n))
        eta = 1.0/(lam*iter_index)
        random.shuffle(row_index_range)
        for j in range(batch_size):
            row_index = row_index_range[j]
            p = predict(weights, dataSet[row_index,:])
            if labels[row_index]*p < 1:
                wDelta += labels[row_index]*dataSet[row_index,:].A
        weights = (1.0 - 1/iter_index)*weights + (eta/batch_size)*wDelta
    return weights


if __name__ == '__main__':
    MRsvm.run()
#     from minitest import *

#     with test(""):

#         pass