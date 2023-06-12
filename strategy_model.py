import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

def run_strategy_model(data_path):
    df = pd.read_csv(data_path)
    X = df.drop('impact_score', axis=1)
    y = df['impact_score']
    model = GradientBoostingClassifier()
    model.fit(X, y)
    return model