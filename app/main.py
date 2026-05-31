from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load model
model = joblib.load("model.pkl")


@app.get("/")
def home():
    return {"message": "D2C Churn API Running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/model")
def model_status():
    return {"model_loaded": True}


class CustomerData(BaseModel):
    city_tier: int
    age_group: int
    acquisition_channel: int
    loyalty_tier: int
    preferred_category: int
    marketing_consent: int

    recency_days: float
    frequency_180d: float
    monetary_180d: float
    return_rate_180d: float
    avg_discount_pct_180d: float
    avg_rating_180d: float
    category_diversity_180d: float

    ticket_count_90d: float
    negative_ticket_rate_90d: float
    avg_resolution_hours_90d: float

    days_since_signup: float
    sessions_30d: float
    product_views_30d: float
    cart_adds_30d: float
    wishlist_adds_30d: float
    abandoned_carts_30d: float

    email_opens_30d: float
    campaign_clicks_30d: float
    last_visit_days_ago: float


@app.post("/predict")
def predict(data: CustomerData):

    features = np.array([[
        data.city_tier,
        data.age_group,
        data.acquisition_channel,
        data.loyalty_tier,
        data.preferred_category,
        data.marketing_consent,

        data.recency_days,
        data.frequency_180d,
        data.monetary_180d,
        data.return_rate_180d,
        data.avg_discount_pct_180d,
        data.avg_rating_180d,
        data.category_diversity_180d,

        data.ticket_count_90d,
        data.negative_ticket_rate_90d,
        data.avg_resolution_hours_90d,

        data.days_since_signup,
        data.sessions_30d,
        data.product_views_30d,
        data.cart_adds_30d,
        data.wishlist_adds_30d,
        data.abandoned_carts_30d,

        data.email_opens_30d,
        data.campaign_clicks_30d,
        data.last_visit_days_ago
    ]])

    prediction = model.predict(features)[0]

    return {
        "prediction": int(prediction)
    }