from surround import Estimator


class ModelStage(Estimator):
    def estimate(self, state, config):
        print("Inference stage ...")
        state.text = "Info here"

    def fit(self, state, config):
        print("No training implemented")
