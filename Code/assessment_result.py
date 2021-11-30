from sklearn.cluster import KMeans
import numpy as np
from sklearn import metrics
import warnings
import pandas as pd
from sklearn.metrics import adjusted_rand_score
import loadData
from calculation_helper import graph_reader
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score,f1_score

warnings.filterwarnings("ignore")

def getQ2(G, labels, input_path, n_clusters):
    matrix = pd.read_csv(input_path)
    matrix = np.asarray(matrix, dtype=int)
    A = loadData.getAdjacencyMatrix(matrix)
    n = len(G.nodes)
    e = len(G.edges)

    S = np.zeros((n, n_clusters))
    for index, value in enumerate(G.nodes):
        S[index][labels[index]] = 1

    B = np.zeros((n, n))
    for i, v_i in enumerate(G.nodes):
        for j, v_j in enumerate(G.nodes):
            B[i][j] = A[i][j] - G.degree(v_i) * G.degree(v_j) / (2 * e)

    Q = 1 / (2 * e) * np.trace(S.T @ B @ S)
    return Q

def getQ(G,labels,input_path):
    matrix = pd.read_csv(input_path)
    matrix = np.asarray(matrix,dtype=int)
    A = loadData.getAdjacencyMatrix(matrix)
    edges_num = len(G.edges)
    sum = 0
    for i,d_i in enumerate(G.degree()):
        for j,d_j in enumerate(G.degree()):
            if labels[i] == labels[j]:
                sum += A[i][j] - d_i[1]*d_j[1]/(2*edges_num)
    Q = sum/(2*edges_num)
    return Q

def assement_Q(input_path,embedding_path):
    k = 4
    graph = graph_reader(input_path)
    x = pd.read_csv(embedding_path)
    clf = KMeans(k)
    y_pred = clf.fit_predict(x)
    Q = getQ(graph,y_pred,input_path)
    return Q

def eval_classification(X,Y,train_percent=0.8):
    X = pd.read_csv(X)
    Y = loadData.getLabelMatrix(Y)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, train_size=train_percent, test_size=1 - train_percent,random_state=666)
    # clf = SVC(C=20)
    clf=LinearSVC()
    clf.fit(X_train, y_train)
    res = clf.predict(X_test)
    accuracy = accuracy_score(y_test, res)
    macro = f1_score(y_test, res, average='macro')
    micro = f1_score(y_test, res, average='micro')
    return micro, macro, accuracy

def assement_result(labes_filePath,embedding_path,k):
    origin_cluster = loadData.getLabelMatrix(labes_filePath)
    x = pd.read_csv(embedding_path)
    a = 0
    sum = 0
    sumF1score = 0
    sumARI = 0
    sumAccuracy = 0
    while a < 10:
        clf = KMeans(k)
        y_pred = clf.fit_predict(x)

        c = y_pred.T
        epriment_cluster = c ;
        NMI = metrics.normalized_mutual_info_score(origin_cluster, epriment_cluster)
        F1_score = f1_score(origin_cluster, epriment_cluster, average='micro')
        ARI = adjusted_rand_score(origin_cluster, epriment_cluster)
        accuracy = accuracy_score(origin_cluster, epriment_cluster)
        sum = sum + NMI
        sumF1score = sumF1score + F1_score
        sumARI = sumARI + ARI
        sumAccuracy = accuracy + sumAccuracy
        a = a + 1
    average_NMI = sum / 10
    average_F1score = sumF1score / 10
    average_ARI = sumARI / 10
    average_Accuracy = sumAccuracy / 10
    return average_NMI, average_F1score, average_ARI




