import os
from os.path import isfile, join
import csv

from google.cloud import bigquery


def load_data(path):
    for entry in os.listdir(path):
        filepath = join(path, entry)

        if not isfile(filepath):
            continue

        with open(filepath) as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                print(row)



if __name__=='__main__':
    bigquery_client = bigquery.Client()

    dataset_id = 'my_new_dataset'

    # Prepares a reference to the new dataset
    dataset_ref = bigquery_client.dataset(dataset_id)
    dataset = bigquery.Dataset(dataset_ref)

    # Creates the new dataset
    dataset = bigquery_client.create_dataset(dataset)

    print('Dataset {} created.'.format(dataset.dataset_id))
