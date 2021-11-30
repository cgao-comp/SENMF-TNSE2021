from modularity_nmf import SENMF
from parser2 import parameter_parser
from calculation_helper import tab_printer
import assessment_result
import time
import numpy as np


def create_and_run_model(args):
    """
    Function to read the graph, create an embedding and train it.
    :param args: Object with parameters -- paths and parameters.
    """
    tab_printer(args)
    model = SENMF(args)
    model.optimize()

if __name__ == "__main__":

    begin = time.time()
    NMI_list = []
    for i in range(3):
        args = parameter_parser()
        create_and_run_model(args)
        edges_path = 'data\\europeFlights_edges.csv'  ## file path
        label_path = "data\\europeFlights_labels.txt"
        embedding_path = "output\\embeddings\\europeFlights_embedding.csv"
        average_NMI, average_F1score, average_ARI = assessment_result.assement_result(label_path, embedding_path, args.k)
        micro, macro, accuracy = assessment_result.eval_classification(embedding_path, label_path, 0.8)
        NMI_list.append(average_NMI)

    max_NMI = max(NMI_list)
    mean_NMI = np.mean(NMI_list)
    print("The maximum value of NMI is：{}".format(max_NMI))
    print("The mean value of NMI is ：{}".format(mean_NMI))


