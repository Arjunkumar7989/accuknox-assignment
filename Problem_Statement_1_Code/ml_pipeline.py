import sqlite3
import logging
import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

import config

# -----------------------------
# LOGGING SETUP
# -----------------------------
logging.basicConfig(
    level=config.LOG_LEVEL,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------
# LOAD DATA
# -----------------------------
def load_data():
    try:
        conn = sqlite3.connect(config.DB_PATH)
        df = pd.read_sql("SELECT * FROM users", conn)
        conn.close()

        if df.empty:
            raise ValueError("Database table is empty")

        logging.info("Data loaded successfully from SQLite")
        return df

    except Exception as e:
        logging.error(f"Failed to load data: {e}")
        raise


# -----------------------------
# FEATURE ENGINEERING
# -----------------------------
def feature_engineering(df):
    # Edge case: missing columns
    required_columns = {"id", "name", "email"}
    if not required_columns.issubset(df.columns):
        raise ValueError("Required columns missing in data")

    # Simple feature logic for demonstration
    df["name_length"] = df["name"].astype(str).apply(len)
    df["email_length"] = df["email"].astype(str).apply(len)

    # Target (synthetic for demonstration)
    df["target"] = np.where(df["email_length"] > 12, 1, 0)

    X = df[["name_length", "email_length"]]
    y = df["target"]

    return X, y


# -----------------------------
# TRAIN MODEL
# -----------------------------
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=config.TEST_SIZE,
        random_state=config.RANDOM_SEED
    )

    model = LogisticRegression(**config.LOGISTIC_REGRESSION_PARAMS)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    logging.info("Model training completed")
    logging.info(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    logging.info("\n" + classification_report(y_test, y_pred))

    return model


# -----------------------------
# MAIN PIPELINE
# -----------------------------
def main():
    logging.info("Starting ML pipeline")

    df = load_data()
    X, y = feature_engineering(df)
    model = train_model(X, y)

    joblib.dump(model, config.MODEL_PATH)
    logging.info(f"Model saved to {config.MODEL_PATH}")

    logging.info("ML pipeline executed successfully")


if __name__ == "__main__":
    main()
