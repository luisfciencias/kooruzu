import numpy as np
from sklearn.metrics import mean_squared_error
from surround import Stage


class Scores(Stage):
    def operate(self, state, config):
        print("scores here ...")
        s1 = np.sqrt(np.sum(np.log(1 + state.y_true) - np.log(1 + state.y_pred)) ** 2)
        s2 = mean_squared_error(state.y_true, state.y_pred)
        print("Score:", s1)
        print("Score:", s2)
