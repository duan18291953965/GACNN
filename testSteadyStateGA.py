# -*- coding: utf-8 -*-
"""
Created on 2019/11/12 16:28 
@file: testSteadyStateGA.py
@author: Matt
"""
from DataMgr import load_cifar10, write_performance
from SteadyStateGA import SteadyStateGA
from keras.utils import to_categorical

root = 'D:/datasets/cifar10'
# root = '/home/u800199/workdir/datasets/cifar10'
X_train, y_train, X_test, y_test = load_cifar10(root)
y_train, y_test = to_categorical(y_train), to_categorical(y_test)
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

train_size = len(X_train)
test_size = len(X_test)
g = SteadyStateGA(
    _X_train=X_train[:train_size],
    _y_train=y_train[:train_size],
    _X_test=X_test[:test_size],
    _y_test=y_test[:test_size],
    _pop_size=20,
    _r_mutation=0.1,
    _p_crossover=0.7,
    _p_mutation=0,  # no use
    _max_iter=10,
    _min_fitness=0.95,
    _batch_size=5000,
    _elite_num=0,  # no use
    _mating_pool_size=0,  # no use
)
g.run()

write_performance(g.evaluation_history, 'SteadyStateGA_CIFAR10.txt')
