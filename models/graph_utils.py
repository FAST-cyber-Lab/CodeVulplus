

import torch
import networkx as nx
import numpy as np
from scipy.sparse import csgraph

def build_dynamic_graph(code_snippet, sequence_length=256, device="cpu"):
    G = nx.erdos_renyi_graph(sequence_length, 0.2)
    adj_matrix = nx.to_numpy_array(G)
    adj_matrix = csgraph.laplacian(adj_matrix, normed=True)
    return torch.tensor(adj_matrix, dtype=torch.float32, device=device)
