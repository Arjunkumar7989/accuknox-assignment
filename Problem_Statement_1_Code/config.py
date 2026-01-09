# config.py
# Centralized configuration for production readiness

DB_PATH = "../database/accuknox.db"
MODEL_PATH = "trained_model.pkl"

RANDOM_SEED = 42
TEST_SIZE = 0.2

LOG_LEVEL = "INFO"

# ML Hyperparameters
LOGISTIC_REGRESSION_PARAMS = {
    "max_iter": 500,
    "solver": "lbfgs"
}
