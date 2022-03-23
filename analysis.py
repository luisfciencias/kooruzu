import logging
from surround import Assembler, Config, Estimator, Stage, State, RunMode


class InputValidator(Stage):
    def operate(self, state, config):
        if state.text:
            raise ValueError("'text' is not None")


class DataInput(Stage):
    def operate(self, state, config):
        print("Data input stage ...")


class DataProcess(Stage):
    def operate(self, state, config):
        print("Data processing stage ...")


class ModelStage(Estimator):
    def estimate(self, state, config):
        print("Inference stage ...")
        state.text = "Info here"

    def fit(self, state, config):
        print("No training implemented")


class DataState(State):
    text = None
    p1 = 3
    p2 = "Info"


if __name__ == "__main__":
    logging_fmt = "{} {}: {}".format("%(asctime)s.%(msecs)03d", "%(levelname)s %(name)s", "%(message)s")
    logging.basicConfig(level=logging.INFO, format=logging_fmt, datefmt='%Y-%m-%d %H:%M:%S')
    data_state = DataState()
    config_params = Config(project_root=".", auto_load=True)
    assembler = Assembler("Forecasting Analysis")
    assembler.set_stages([InputValidator(), DataInput(), DataProcess(), ModelStage()])
    assembler.set_config(config=config_params)
    assembler.run(data_state, mode=RunMode.PREDICT)
    print("data.p1 is {}".format(data_state.p1))
    print("data.p2 is {}".format(data_state.p2))
