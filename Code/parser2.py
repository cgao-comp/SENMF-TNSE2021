import argparse


def parameter_parser():

    parser = argparse.ArgumentParser(description="Run M-NMF.")

    parser.add_argument("--input",
                        nargs="?",
                        default="./data/food_edges.csv",
                        help="Input graph path.")

    parser.add_argument("--embedding-output",
                        nargs="?",
                        default="./output/embeddings/food_embedding.csv",
                        help="Embeddings path.")

    parser.add_argument("--cluster-mean-output",
                        nargs="?",
                        default="./output/cluster_means/food_means.csv",
                        help="Cluster means path.")

    parser.add_argument("--log-output",
                        nargs="?",
                        default="./output/logs/food.json",
                        help="Log path.")

    parser.add_argument("--assignment-output",
                        nargs="?",
                        default="./output/assignments/food.json",
                        help="Assignment path.")

    parser.add_argument("--dump-matrices",
                        type=bool,
                        default=True,
                        help="Save the embeddings to disk or not.")

    parser.add_argument("--dimensions",
                        type=int,
                        default=16,
                        help="Number of dimensions.")

    parser.add_argument("--clusters",
                        type=int,
                        default=4,
                        help="Number of clusters.")

    parser.add_argument("--lambd",
                        type=float,
                        default=0.2,
                        help="Weight of the cluster membership constraint.")

    parser.add_argument("--alpha",
                        type=float,
                        default=0.05,
                        help="Weight of clustering cost.")

    parser.add_argument("--beta",
                        type=float,
                        default=0.05,
                        help="Weight of modularity cost.")

    parser.add_argument("--iteration-number",
                        type=int,
                        default=200,
                        help="Number of weight updates.")

    parser.add_argument("--early-stopping",
                        type=int,
                        default=3,
                        help="Number of iterations to do after reaching the best modularity value.")

    parser.add_argument("--lower-control",
                        type=float,
                        default=10 ** -15,
                        help="Lowest possible component value.")

    parser.add_argument("--eta",
                        type=float,
                        default=1.0,
                        help="Weight of second order similarities.")

    parser.add_argument("--mu",
                        type=float,
                        default=0.5,
                        help="Weight of currency adjacency matrix.")

    parser.add_argument("--gamma",
                        type=float,
                        default=0.5,
                        help="Weight of currency community structure.")

    parser.add_argument("--k",
                        type=int,
                        default=5,
                        help="the number of cluster that implement in spectral clustering.")

    parser.add_argument("--theta",
                        type=float,
                        default=1,
                        help="Weight of equivalence matrix.")

    parser.add_argument("--file_num",
                        type=int,
                        default=10,
                        help="the number of files in a absolute path.")

    parser.add_argument("--omega",
                        type=float,
                        default=0.1,
                        help="Weight of similarity matrix.")

    return parser.parse_args()
