import pandas as pd

m1 = pd.read_csv('/home/glard/AML/roost/roost/examples/roost_simple_candidate_exp1_M0_0224.csv')
m201 = pd.read_csv('/home/glard/AML/roost/roost/examples/roost_simple_candidate_exp2_bs_M10001.csv')
m211 = pd.read_csv('/home/glard/AML/roost/roost/examples/roost_simple_candidate_exp2_bo_M10016.csv')
m3 = pd.read_csv('/home/glard/AML/roost/roost/examples/roost_simple_candidate_exp3_base.csv')
m31 = pd.read_csv('/home/glard/AML/roost/roost/examples/roost_simple_candidate_exp3_bo.csv')

# m1_candidates = m1['composition']

set_m1_candidates = set(m1['composition'].unique())
set_m201_candidates = set(m201['composition'].unique())
set_m211_candidates = set(m211['composition'].unique())

set_m3_candidates = set(m3['composition'].unique())
set_m31_candidates = set(m31['composition'].unique())
# -----------------------------------------------------------------------------------
common_1_201 = set_m1_candidates & set_m201_candidates
common_1_211 = set_m1_candidates & set_m211_candidates
print(len(common_1_201))
print(len(common_1_211))

print(f"Screening Accuracy for exp2 bs is {len(common_1_201)/len(set_m1_candidates)}")

print(f"Screening Accuracy for exp2 al is {len(common_1_211)/len(set_m1_candidates)}")
# --------------------------------------------------------------------------------------
common_1_3 = set_m1_candidates & set_m3_candidates
common_1_31 = set_m1_candidates & set_m31_candidates
print(len(common_1_3))
print(len(common_1_31))

print(f"Screening Accuracy for exp3 bs is {len(common_1_3)/len(set_m1_candidates)}")

print(f"Screening Accuracy for exp3 al is {len(common_1_31)/len(set_m1_candidates)}")