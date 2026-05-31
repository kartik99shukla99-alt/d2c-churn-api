# D2C Churn Prediction API

## Project Overview

This project predicts whether a Direct-to-Consumer (D2C) customer is likely to churn within the next 60 days using a Logistic Regression model trained on customer behavior, engagement, support, and transaction features.

## Model Performance

* Accuracy: 82.44%
* Precision: 79.14%
* Recall: 88.10%
* F1 Score: 83.38%
* ROC-AUC: 88.73%

## Project Structure

d2c-churn-api/

* app/main.py
* tests/test_api.py
* model.pkl
* Dockerfile
* requirements.txt
* README.md
* monitoring_plan.md

## API Endpoints

### GET /

Returns API status message.

### GET /health

Returns service health status.

### GET /model

Checks whether the model is loaded successfully.

### POST /predict

Predicts customer churn.

Example Response:

{
"prediction": 0
}

Where:

* 0 = Customer not likely to churn
* 1 = Customer likely to churn

## Running Locally

```bash
uvicorn app.main:app --reload
```

Swagger UI:

http://localhost:8000/docs

## Running with Docker

```bash
docker build -t churn-api .
docker run -p 8000:8000 churn-api
```

Swagger UI:

http://localhost:8000/docs

## Running Tests

```bash
python -m pytest
```

Expected Result:

3 passed

## Monitoring

See monitoring_plan.md for:

* API monitoring
* Prediction monitoring
* Error monitoring
* Responsible AI considerations

## Author

Kartik Shukla
