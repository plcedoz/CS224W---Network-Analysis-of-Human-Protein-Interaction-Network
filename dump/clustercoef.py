import networkx as nx

from read_graph import read_graph
from common.pipeline import Pipeline
from common.feature_generators import *

# Loading PPI graph
Graph, node_names = read_graph(directed=False)

pipeline = Pipeline(ClusteringCoefficient())
_ = pipeline.apply(Graph)
