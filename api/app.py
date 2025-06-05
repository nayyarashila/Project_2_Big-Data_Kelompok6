from fastapi import FastAPI, Query
import pandas as pd

app = FastAPI()

# Load prediction results
predicted_df = pd.read_parquet("models/predicted_severity.parquet")
clustered_df = pd.read_parquet("models/clustered_data.parquet")
recommender_df = pd.read_parquet("models/recommendation_data.parquet")

# Endpoint 1: Get batch prediction result (by index)
@app.get("/get_predicted_severity")
def get_predicted_severity(index: int = Query(...)):
    if index < 0 or index >= len(predicted_df):
        return {"error": "Index out of range"}
    return predicted_df.iloc[index].to_dict()

# Endpoint 2: Get batch cluster result (by index)
@app.get("/get_cluster_result")
def get_cluster_result(index: int = Query(...)):
    if index < 0 or index >= len(clustered_df):
        return {"error": "Index out of range"}
    return clustered_df.iloc[index].to_dict()

# Endpoint 3: Get recommendation result (by rating)
@app.get("/get_recommendation_result")
def get_recommendation_result(user_rating: float = Query(...)):
    rec = recommender_df[recommender_df["label"] == user_rating]
    if rec.empty:
        return {"message": "No recommendation for this rating"}
    return rec.to_dict(orient="records")
