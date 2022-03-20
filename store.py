import argparse
import os
import matplotlib.pyplot as plt
import pandas as pd

parser = argparse.ArgumentParser(description="Command line arguments")
parser.add_argument('--store', type=str, help='path to csv store training file',
                    default=os.path.join("data", "stores", "store01.csv"))
args = parser.parse_args()

df_store = pd.read_csv(args.store, low_memory=False,
                       usecols=["date", "item_nbr", "unit_sales", "onpromotion"],
                       parse_dates=["date"])

gb = df_store.groupby("item_nbr")
path_dir_figs = os.path.join("output", "figures")
if not os.path.exists(path_dir_figs):
    os.makedirs(path_dir_figs)
for k, gp in gb:
    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.plot(gp["date"], gp["unit_sales"])
    ax.set_title(str(k))
    fig_file = "fig_item" + str(k) + ".png"
    path_save_fig = os.path.join(path_dir_figs, fig_file)
    fig.savefig(path_save_fig, dpi=128)
    plt.close(fig)
