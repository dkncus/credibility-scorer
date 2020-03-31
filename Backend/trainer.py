"""
Trainer file with the majority of the model code
"""

import pickle
import numpy as np 
import tensorflow as tf

def main():

    with open("./data/all_kaggle_data.pickle", 'rb') as handle:
        all_data = pickle.load(handle)

        #Planning to import pretrained word embeddings here

if __name__ == '__main__':
    main()