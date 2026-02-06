import pandas as pd

def predict_least_crowded():
    df = pd.read_csv("data/gym_usage.csv")

    # Sort by users (ascending)
    best_slot = df.sort_values("users").iloc[0]

    return {
        "hour": int(best_slot["hour"]),
        "expected_users": int(best_slot["users"])
    }
