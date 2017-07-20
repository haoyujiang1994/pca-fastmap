import numpy as np
datanup = np.loadtxt("pca-data.txt",dtype=float)
def pca(datanup,k):
# data preprocessing
    meannup = np.mean(datanup,axis=0)
    new_datanup = datanup - meannup
# calculate covariance matrix
    sigma = np.cov(new_datanup,rowvar=0)
# calculate eigvalues and eigvectors
    eigvalues, eigvectors = np.linalg.eig(sigma)
# calculate eigvectors_truncate
    new_eigvaluesindex = np.argsort(-eigvalues)
    new_eigvectors = eigvectors[:,new_eigvaluesindex]
    eigvectors_truncate = new_eigvectors[:,0:k]
# dimensional reduction
    new_datanup = np.dot(eigvectors_truncate.T,datanup.T)
    return new_datanup.T


print pca(datanup,2)



