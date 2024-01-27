# Digit prediction API

This API allows the client to predict which digit is handwritten in a given image, returning the digit and its
confidence.

## Setup

- **Model**: TensorFlow model loaded from `./../Model/digit_model.h5`

## Endpoints

### 1. Health Check (`/hc`)

- **Method**: GET
- **Description**: Returns the current server date and time, along with the uptime since the app's launch.
- **Parameters**: None
- **Response Format**: JSON object with keys:
    - date: Current date and time of the server
    - uptime: seconds since the server was launched

- **Examples**
    - Success response:
        ```json
        {
            "date": "January 27, 2024 14:35:31",
            "uptime": "4928.41"
        }
        ```

### 2. Predict (`/predict`)

- **Method**: POST
- **Description**: Predicts a digit from a given picture
- **Parameters**: Multi-part form with the following parameter
    - digit: Image with a .jpg or .jpeg, .png extension
- **Response**: JSON object with keys:
    - digit: digit predicted by the model
    - score: confidence of the model predicting the digit (0 to 1)

- **Examples**
    - Success Response:
        ```json
        {
          "digit": "1",
          "score": "0.99"
        }
        ```
    - Error Response:
        ```json
        {
           "msg": "Error message."
        }
        ```