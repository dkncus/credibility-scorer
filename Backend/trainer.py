"""
Trainer file with the majority of the model code
"""

import pickle
import numpy as np 
import tensorflow as tf
from keras.layers import Embedding

def main():

    with open("./data/kaggle_train.pickle", 'rb') as handle:
        x_train, y_train = pickle.load(handle)
        

        #TODO: add in padding, model and training

if __name__ == '__main__':
    main()