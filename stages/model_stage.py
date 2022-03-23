import numpy as np
from statsmodels.tsa.ar_model import AutoReg
from surround import Estimator


class ModelStage(Estimator):
    def estimate(self, state, config):
        print("Inference stage ...")
        state.text = "Info here"

    def fit(self, state, config):
        print("Training stage")
        # single item test
        nominated_item = config["nominated_item"]
        x = state.dict_info[nominated_item]
        h = 7
        y_train, y_test = x[0:len(x)-h], x[len(x)-h:]
        model = AutoReg(y_train.values, lags=7)
        model_fit = model.fit()
        predictions = model_fit.predict(start=len(y_train),
                                        end=len(y_train)+len(y_test)-1)
        y_pred = np.array(predictions)
        y_true = y_test["unit_sales"].values
        state.y_pred = y_pred
        state.y_true = y_true
