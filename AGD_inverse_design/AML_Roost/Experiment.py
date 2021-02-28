"""
This file is used to conduct experiment
"""

import SearchStrategy
import preprocessing
import numpy as np
import model_inference

if __name__ == '__main__':

    #filepath = './superconduct/train.csv'
    #dataset = 'superconductivity'
    filepath = './Utils/bd_AML_whole_for_autoencoder.csv'
    dataset = 'bandgap'
    # prepare corresponding dataset, initialize preprocessing class, set label
    # drop duplicate records, generate sorted pandas data frame
    p = preprocessing.preprocessing(filepath,dataset)
    # provide initial sample points for bo to reference
    # x, y is used

    X, y, top10, cols = p.bo_read_data()

    pbounds = p.get_range_dic()
    # bf = BlackboxFunc(func_name='RF', p=p)
    # function = bf.bandgap_inference
    function = model_inference.inference

    para = np.asarray(X, dtype=np.float32)

    para_dic_in_list = []
    for l in X:
        p_dic = {}
        for key, v in zip(cols, l):
                p_dic[key] = v
        para_dic_in_list.append(p_dic)

    target = np.asarray(y, dtype=np.float32)

    s = SearchStrategy.SearchStrategy(satisfactory_value = top10, target_func = function,
                                           initial_para = para_dic_in_list,
                                           initial_target = target,
                                           mode = 1,
                                           boundary=pbounds, budget = 500)
    s.bo_opt_circle()
    print('success')
