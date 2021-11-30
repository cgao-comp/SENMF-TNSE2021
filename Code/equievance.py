import numpy as np
from sklearn import preprocessing

def getLs(orbitFile_url):
    GDVM = np.loadtxt(orbitFile_url)
    S=cos_similarity(GDVM)
    Ls=Laplacian(S)
    return S

def cos_similarity(array):  # n x d
    n=array.shape[0]

    print('begin standardization')
    array=preprocessing.scale(array)
    #cos_similarity
    vector_norm=np.linalg.norm(array, axis=1)
    S=np.zeros((n,n))

    for i in range(n):
        #print('cos_similarity:',i/n)
        S[i,i]=1
        for j in range(i+1,n):
            #if W[i,j]!=0:
            S[i,j]= np.dot( array[i,:],array[j,:] ) / (vector_norm[i]*vector_norm[j])
            S[i,j]=0.5+0.5*S[i,j]
            S[j,i]= S[i,j]
    return S

def Laplacian(W):
    """
    input matrix W=(w_ij)
    "compute D=diag(d1,...dn)
    "and L=D-W
    "and Lbar=D^(-1/2)LD^(-1/2)
    "return Lbar
    """
    d=[np.sum(row) for row in W]
    D=np.diag(d)
    #L=D-W
    #Dn=D^(-1/2)
    Dn=np.ma.power(np.linalg.matrix_power(D,-1),0.5)
    Lbar=np.dot(np.dot(Dn,W),Dn)

    return np.mat(Lbar)



