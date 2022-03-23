import os
import pandas as pd
from surround import Stage


class DataInput(Stage):
    def operate(self, state, config):
        state.df_store = pd.read_csv("data/stores/store01.csv", low_memory=False, parse_dates=["date"])
        state.df_test = pd.read_csv(os.path.join("data", "test.csv"), parse_dates=["date"])
        state.df_stores_info = pd.read_csv(os.path.join("data", "stores.csv"))
        state.df_items = pd.read_csv(os.path.join("data", "items.csv"))
        state.df_transactions = pd.read_csv(os.path.join("data", "transactions.csv"))
        state.df_oil = pd.read_csv(os.path.join("data", "oil.csv"))
        state.df_holidays = pd.read_csv(os.path.join("data", "holidays_events.csv"))
