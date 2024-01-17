# Property Price Prediction API Documentation

***

# Table of Contents
1. [Overview](#overview)
2. [Endpoints](#endpoints)
   - [1. Predict Property Price](#1-predict-property-price)
3. [How to Run](#how-to-run)
4. [Error Handling](#error-handling)

***

## Overview

This API is designed to predict property prices based on geographical coordinates. It utilizes a decision tree model to estimate property prices per square meter at a given latitude and longitude.

***

## Endpoints

### 1. Predict Property Price
- **URL**: `/predict_get`
- **Method**: `GET`
- **Query Params**: 
  - `latitude=[float]` (required)
  - `longitude=[float]` (required)
- **Success Response**: JSON object with the predicted price per square meter.
- **Error Response**: 
  - 400 Bad Request if query parameters are missing or invalid
  - 503 Service Unavailable if the model is not loaded
  - 500 Internal Server Error for other issues
- **Example**: `http://localhost:5000/predict_get?latitude=48.8566&longitude=2.3522`

***

## How to Run

- Ensure FastAPI, Uvicorn, and necessary dependencies are installed.
- Load the decision tree model named `decision_tree_model.pkl`.
- Run the server using `uvicorn main:app --host=localhost --port=5000`, with `main.py` being the script containing the FastAPI app.
- Access the API at `http://localhost:5000`.

***

## Error Handling

- Custom error handling is implemented to manage internal server errors.
- The server returns appropriate error messages and HTTP status codes based on the nature of the error encountered.
- The API checks for the model's availability before making predictions, ensuring reliable responses.

***
