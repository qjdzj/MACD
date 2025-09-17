import os, sys

sys.path.append(os.getcwd())
from utils.logging import read_from_pickle_file
import ipdb

results = []
for r in read_from_pickle_file(
    "results/Llama-3.1-8B-Instruct_baseline/pancreatitis.pkl"
):
    results.append(r)
results = {k: v for d in results for k, v in d.items()}
ipdb.set_trace()
