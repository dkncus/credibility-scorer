"""
Program to take kaggle dataset and put only text and labels into a pickle file.
"""

import csv
import pickle

FALSE = 0
TRUE = 1

def main():

    all_data = {}
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
            
            #currently, just storing text and labels. 
            all_data[text] = FALSE
            
        print(f"Read in {line_count} examples into all_data")

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
            
            #currently, just storing text and labels. 
            all_data[text] = TRUE
            
        print(f"Read in {line_count} examples into all_data")

    with open("./data/all_kaggle_data.pickle", 'wb') as handle:
        pickle.dump(all_data, handle)

if __name__ == '__main__':
    main()