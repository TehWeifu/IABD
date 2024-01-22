# Digit prediction model API

This API allows the client to predict which digit in handwritten in a given image, returning the digit and its
confidence

## Endpoints

### hc (Heal Check)

This endpoint returns the current server time and the time in seconds since starting the server

* URL: /hc
* Method: GET
* Parameters: None
* Response: JSON object with the following keys
    * date: Current date and time of the server
    * timestamp: second since the sever was launched

### predict

This endpoint predicts a digit given a picture

* URL: /predict
* Method: POST
* Parameters: Multi-part form with the following parameter
    * digit: Image with a .jpg or .jpeg, .png extension
* Response: JSON object with the following keys
    * prediction: the digit predicted by the model
    * score: the confidence of the model predicting the digit (0 to 1)
