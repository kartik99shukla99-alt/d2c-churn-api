from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_predict():
    response = client.post(
        "/predict",
        json={
            "city_tier": 1,
            "age_group": 1,
            "acquisition_channel": 1,
            "loyalty_tier": 1,
            "preferred_category": 1,
            "marketing_consent": 1,
            "recency_days": 10,
            "frequency_180d": 5,
            "monetary_180d": 5000,
            "return_rate_180d": 0.1,
            "avg_discount_pct_180d": 0.2,
            "avg_rating_180d": 4.5,
            "category_diversity_180d": 3,
            "ticket_count_90d": 1,
            "negative_ticket_rate_90d": 0,
            "avg_resolution_hours_90d": 12,
            "days_since_signup": 300,
            "sessions_30d": 10,
            "product_views_30d": 20,
            "cart_adds_30d": 5,
            "wishlist_adds_30d": 2,
            "abandoned_carts_30d": 1,
            "email_opens_30d": 4,
            "campaign_clicks_30d": 2,
            "last_visit_days_ago": 5
        }
    )

    assert response.status_code == 200