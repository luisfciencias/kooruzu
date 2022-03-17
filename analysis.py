import argparse
import os
import pandas as pd

parser = argparse.ArgumentParser(description="Command line arguments")
parser.add_argument('--train', type=str, help='path to csv training file', default=os.path.join("data", "train.csv"))
parser.add_argument('--test', type=str, help='path to csv test file', default=os.path.join("data", "test.csv"))
args = parser.parse_args()

df_train = pd.read_csv(args.train)
print(df_train)
