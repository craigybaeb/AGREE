# AGREE API

AGREE (Aggregation for Robust Explanation Experience) API is a Flask-based API that calculates disagreement between explainers and provides aggregate explanations. It is designed to determine the level of disagreement in factual explainers and provide an aggregated explanation that combines the knowledge from a given number of explainers.

## Features

- Calculate disagreement between explainers using various metrics
- Perform aggregation on explanations to generate an aggregate explanation
- Support for both global and local explanations
- Configurable average method (mean or median)
- Error handling and validation of input parameters
- Dockerized setup for easy deployment

## Installation

1. Clone the repository:

   `git clone https://github.com/craigybaeb/AGREE.git`

2. Navigate to the project directory:

   `cd AGREE-API`

3. Install the required dependencies:

   `pip install -r requirements.txt`

## Configuration

The application can be configured using the `config.py` file in the project root directory. Adjust the configuration parameters to match your environment.

## Usage

### Running with Docker

To run the AGREE API server using Docker, make sure you have Docker installed on your system. Then, follow these steps:

1. Build the Docker image:

   `docker build -t agree-api .`

2. Run the Docker container:

   `docker run -p 5000:5000 agree-api`

The API server will be accessible at `http://localhost:5000`.

### Running with Docker Compose

To run the AGREE API server using Docker Compose, make sure you have Docker Compose installed on your system. Then, follow these steps:

1. Start the Docker Compose services:

   `docker-compose up`

The API server will be accessible at `http://localhost:5000`.

### Running with Python

To start the AGREE API server using Python, run the following command from the project root directory:

`python -m flask run`

By default, the API server will run on `http://localhost:5000`.

## API Endpoints

The AGREE API exposes the following endpoints:

### `POST /disagreement`

Calculate the disagreement between explainers.

**Request Parameters**

- `disagreement_metric` (string): The method used to calculate disagreement.
- `overall_disagreement` (float): The overall agreement confidence between explainers.
- `disagreement_scores` (dictionary): A dictionary containing all of the explainers used and their disagreement scores.
- `average_method` (string): The method used to determine the average (median or mean).
- `data_to_explain` (numpy array): A numpy array of the data to explain.
- `model` (file): A Keras model file to explain.
- `scope` (string): The scope of the explanation (global or local).

**Example Request**

```bash
curl -X POST http://localhost:5000/disagreement \
  -H "Content-Type: application/json" \
  -d '{
    "disagreement_metric": "case_align",
    "overall_disagreement": 0.85,
    "disagreement_scores": {
      "explainer1": 0.9,
      "explainer2": 0.8
    },
    "average_method": "mean",
    "data_to_explain": [[1, 2, 3], [4, 5, 6]],
    "model": "@path/to/model.h5",
    "scope": "global"
  }'
```

**Response Parameters**

- `disagreement_metric` (string): The method used to calculate disagreement.
- `overall_disagreement` (float): The overall agreement confidence between explainers.
- `disagreement_scores` (dictionary): A dictionary containing all of the explainers used and their disagreement scores.
- `average_method` (string): The method used to determine the average (median or mean).
- `explainers` (list of strings): The explainers used in the disagreement calculation.

**Example Response**

```json
{
  "disagreement_metric": "case_align",
  "overall_disagreement": 0.85,
  "disagreement_scores": {
    "explainer1": 0.9,
    "explainer2": 0.8
  },
  "average_method": "mean",
  "explainers": ["explainer1", "explainer2"]
}
```

Please note that the API server should be running locally at \`http://localhost:5000\`.

## Contributing

Contributions to the AGREE API are welcome! If you find any issues or would like to propose improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or inquiries about the AGREE API, please contact:

Email: c.pirie11@rgu.ac.uk

---

## Citation

If you use the AGREE API in your research work or publications, please cite it as:

[Provide citation details here]
