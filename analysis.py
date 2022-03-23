import logging
from surround import Assembler, Config, RunMode
from stages import DataInput, DataProcess, DataState, InputValidator, ModelStage, Scores


if __name__ == "__main__":
    logging_fmt = "{} {}: {}".format("%(asctime)s.%(msecs)03d", "%(levelname)s %(name)s", "%(message)s")
    logging.basicConfig(level=logging.INFO, format=logging_fmt, datefmt='%Y-%m-%d %H:%M:%S')
    data_state = DataState()
    config_params = Config(project_root=".", auto_load=True)
    assembler = Assembler("Forecasting Analysis")
    assembler.set_stages([InputValidator(), DataInput(), DataProcess(), ModelStage(), Scores()])
    assembler.set_config(config=config_params)
    assembler.run(data_state, mode=RunMode.TRAIN)
