from surround import Stage


class DataProcess(Stage):
    def operate(self, state, config):
        gb_item = state.df_store.groupby("item_nbr")
        dict_info = dict()
        for k, gp in gb_item:
            df_item = gp[["date", "item_nbr", "unit_sales"]]
            unit_sales_per_day = df_item.set_index(df_item.pop('date')).resample('D')['unit_sales'].sum()
            df_unit_sales = unit_sales_per_day.to_frame()
            dict_info[str(k)] = df_unit_sales
        state.dict_info = dict_info
