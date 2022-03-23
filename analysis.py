import logging
from surround import Assembler, Config, State, RunMode
from stages import DataInput, DataProcess, InputValidator, ModelStage


class DataState(State):
    text = None
    df_store = None
    df_test = None
    df_stores_info = None
    df_items = None
    df_transactions = None
    df_oil = None
    df_holidays = None
    df_units_sale = None
    dict_info = None
    y_true = None
    y_pred = None


if __name__ == "__main__":
    logging_fmt = "{} {}: {}".format("%(asctime)s.%(msecs)03d", "%(levelname)s %(name)s", "%(message)s")
    logging.basicConfig(level=logging.INFO, format=logging_fmt, datefmt='%Y-%m-%d %H:%M:%S')
    data_state = DataState()
    config_params = Config(project_root=".", auto_load=True)
    assembler = Assembler("Forecasting Analysis")
    assembler.set_stages([InputValidator(), DataInput(), DataProcess(), ModelStage()])
    assembler.set_config(config=config_params)
    assembler.run(data_state, mode=RunMode.TRAIN)
