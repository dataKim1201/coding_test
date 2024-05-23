# import sys
# input = sys.stdin.readline
# case = input().strip()

# result = -1
# def backtracking(cnt =0):
#     if cnt %30 == 0:
#         result= max(result,cnt)
import random
def get_gold(cand):
    gold = []    
    for item in range(300):
        res = random.sample(range(len(cand)),10)
        res2 = random.sample(range(256,len(cand)),10)
        gold.append(res + res2)
    return gold

import torch

query = torch.randn(10,768)
cand = torch.randn(256,768)
cand2 = torch.randn(300,768)

cand = torch.cat([cand,cand2],0)

gold = get_gold(cand)
result = query@cand.T
print(result.shape)
cand_inds = list(range(256))
cand2_inds = [len(cand_inds) + i for i in range(300)]
cand_inds += cand2_inds
for i in range(result.shape[0]):
    item = result[i]
    _,topk_indices = item.topk(3)
    print(i,topk_indices)
    n_covered_top_k = sum([ids in gold[i] for ids in topk_indices])
    print('n_covered_top_k',n_covered_top_k)
