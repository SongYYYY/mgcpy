from mgcpy.independence_tests.mdmr.mdmr import MDMR
from mgcpy.independence_tests.mdmr.mdmrfunctions import compute_distance_matrix
import numpy as np


def test_mdmr():
    #load data from csv files
    X = np.genfromtxt('./mgcpy/independence_tests/unit_tests/mdmr/data/X_mdmr.csv', delimiter=",")
    
    Y = np.genfromtxt('./mgcpy/independence_tests/unit_tests/mdmr/data/Y_mdmr.csv', delimiter=",")

    mdmr = MDMR(compute_distance_matrix)
    a, b1, results1 = mdmr.test_statistic(X, Y, individual=1)
    b2, results2 = mdmr.p_value(X, Y, individual = 1)
    
    #test get_name
    assert mdmr.get_name() == 'mdmr'
    
    #test statistic
    assert np.allclose(a, 75.11630064)
    
    #p-value
    assert np.allclose(b2, 0.000999)
    
    #individual statistics
    assert np.allclose(results1[0,1], 10.39953044)
    assert np.allclose(results2[0,2], 0.000999)
    assert np.allclose(results1[1,1], 4.12263312)
    assert np.allclose(results2[1,2], 0.000999)
    assert np.allclose(results1[2,1], 11.31712737)
    assert np.allclose(results2[2,2], 0.000999)