import argparse
import os
import pandas as pd

parser = argparse.ArgumentParser(description="Command line arguments")
parser.add_argument('--train', type=str, help='path to csv training file', default=os.path.join("data", "train.csv"))
parser.add_argument('--test', type=str, help='path to csv test file', default=os.path.join("data", "test.csv"))
args = parser.parse_args()

df_train = pd.read_csv(args.train, low_memory=False)
gb_store = df_train.groupby("store_nbr")

path_dir_store_batches = os.path.join("data", "stores")
if not os.path.exists(path_dir_store_batches):
    os.makedirs(path_dir_store_batches)
for k, gp in gb_store:
    csv_file = "store" + str(k).zfill(2) + ".csv"
    path_save_csv = os.path.join(path_dir_store_batches, csv_file)
    gp.to_csv(path_save_csv, index=False)
