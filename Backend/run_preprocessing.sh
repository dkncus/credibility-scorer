#!/bin/bash

TRUE_DATA_PATH=./data/True.csv
FALSE_DATA_PATH=./data/False.csv
PICKLE_DATA=./data/kaggle_train.pickle

if [[ -f "${TRUE_DATA_PATH}" ]] || [[ -f "${FALSE_DATA_PATH}" ]] ; then
    
    if [[ ! -f "${PICKLE_DATA}" ]] ; then
        echo "Converting CSV files into pickle..."
        python preprocess_kaggle.py
    fi

else
    
    echo "Kaggle data isn't in the data folder"

fi