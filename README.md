# SENMF-TNSE2021
The code related to the paper below：

Junyou Zhu, Chunyu Wang, Chao Gao*, Fan Zhang, Zhen Wang*, Xuelong Li, Community detection in graph: An embedding method, IEEE Transactions on Network Science and Engineering, 2021, doi: 10.1109/TNSE.2021.3130321

# Running the code

Some examples execute commands as shown below:

python code/main.py --input data/europeFlights_edges.csv  --embedding-output data/output/embeddings/europeFlights_embedding.csv --cluster-mean-output data/output/cluster_means/europeFlights_means.csv --dimensions 64 --clusters 4 --alpha 0.59 --beta 3 --k 4 --theta 8 --eta 5 --lambd 6.399 --iteration-number 600 --early-stopping 100 --lower-control 22 --omega 0.01

python code/main.py --input data/polbooks_edges.csv  --embedding-output data/output/embeddings/polbooks_embedding.csv --cluster-mean-output data/output/cluster_means/polbooks_means.csv --dimensions 64 --clusters 3 --alpha 0.59 --beta 3 --k 3 --theta 0.01 --eta 5 --lambd 6.399 --iteration-number 600 --early-stopping 100 --lower-control 22 --omega 1

# Reference
If you make advantage of SENMF in your research, please cite the following in your manuscript:

```
@ARTICLE{9626627,
  author={Zhu, Junyou and Wang, Chunyu and Gao, Chao and Zhang, Fan and Wang, Zhen and Li, Xuelong},
  journal={IEEE Transactions on Network Science and Engineering}, 
  title={Community Detection in Graph: An Embedding Method}, 
  year={2021},
  volume={},
  number={},
  pages={},
  doi={10.1109/TNSE.2021.3130321}}
```

 
