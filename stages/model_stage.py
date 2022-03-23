import numpy as np
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.ar_model import AutoReg
from surround import Estimator


class ModelStage(Estimator):
    def estimate(self, state, config):
        print("Inference stage ...")
        state.text = "Info here"

    def fit(self, state, config):
        print("Training stage")
        print(state.dict_info["105575"])
        x = state.dict_info["105575"]
        h = 7
        y_train, y_test = x[0:len(x)-h], x[len(x)-h:]
        model = AutoReg(y_train.values, lags=7)
        model_fit = model.fit()
        predictions = model_fit.predict(start=len(y_train),
                                        end=len(y_train)+len(y_test)-1)
        y_pred = np.array(predictions)
        y_true = y_test["unit_sales"].values
        s1 = np.sqrt(np.sum(np.log(1 + y_true) - np.log(1 + y_pred))**2)
        s2 = mean_squared_error(y_true, y_pred)
        print("Score:", s1)
        print("Score:", s2)
