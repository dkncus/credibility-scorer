"""
Program to take kaggle dataset and put only text and labels into a pickle file.
"""

import csv
import pickle
from sklearn.model_selection import train_test_split
import numpy as np 

FALSE = 0
TRUE = 1
TEST_SIZE = 0.2
RANDOM_SEED = 22

def main():

    embeddings_dict = {}

    #importing in pretrained word embeddings
    with open("./data/glove.6B.300d.txt") as f:
        for line in f:
            values = line.split()
            word = values[0]
            embedding = np.asarray(values[1:], dtype='float32')
            embeddings_dict[word] = embedding

    print("Done loading in GloVe embeddings")

    all_x = []
    all_y = []

    with open("./data/Fake.csv") as f:
        csv_reader = csv.reader(f, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue #ignore first line -- just template info

            line_count += 1

            title = row[0]
            text = row[1]
            subject = row[2]
            date = row[3]
            
            #currently, just storings text and labels. 

            #take text and get pretrained embeddings
            article_embedding = []
            for word in text:
                word_embedding = embeddings_dict.get(word)
                if word_embedding is not None: #ignore words not found
                    article_embedding.append(word_embedding)

            all_x.append(article_embedding)
            all_y.append(FALSE)
            
        print(f"Read in {line_count} examples")

    with open("./data/True.csv") as f:
        csv_reader = csv.reader(f, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue #ignore first line -- just template info

            line_count += 1

            title = row[0]
            text = row[1]
            subject = row[2]
            date = row[3]
            
            #currently, just storings text and labels. 

            #take text and get pretrained embeddings
            article_embedding = []
            for word in text:
                word_embedding = embeddings_dict.get(word)
                if word_embedding is not None: #ignore words not found
                    article_embedding.append(word_embedding)

            all_x.append(article_embedding)
            all_y.append(TRUE)
            
        print(f"Read in {line_count} examples")

    x_train, x_test, y_train, y_test = train_test_split(all_x, all_y, test_size=TEST_SIZE, random_state=RANDOM_SEED, shuffle=True)

    assert len(x_train) == len(y_train)
    assert len(x_test) == len(y_test)

    with open("./data/kaggle_train.pickle", 'wb') as handle:
        pickle.dump([x_train, y_train], handle)

    with open("./data/kaggle_test.pickle", 'wb') as handle:
        pickle.dump([x_test, y_test], handle)

if __name__ == '__main__':
    main()