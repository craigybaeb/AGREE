# AGREE API

AGREE (Aggregation for Robust Explanation Experiences) API is a Flask-based API developed by the Robert Gordon University that calculates disagreement between explainers and provides aggregate explanations. It is designed to determine the level of disagreement in factual explainers and provide an aggregated explanation that combines the knowledge from a given number of explainers.

[![The Robert Gordon University](https://i0.wp.com/ecareersgrad.co.uk/wp-content/uploads/2022/07/RGU-logo-1.png?ssl=1)](https://www.rgu.ac.uk/)


## Features

- Calculate disagreement between explainers using various metrics
- Perform aggregation on explanations to generate an aggregate explanation
- Support for both global and local explanations
- Configurable average method (mean or median)
- Error handling and validation of input parameters
- Dockerized setup for easy deployment

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Performance Considerations](#performance-considerations)
- [API Endpoints](#api-endpoints)
  - [Calculate Disagreement](#calculate-disagreement)
  - [Perform Aggregation](#perform-aggregation)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [Author](#author)
- [Future Work](#future-work)
- [Contact](#contact)
- [License](#license)

## Installation

The installation guide assumes that you have python3, pip3 and git installed.

1. Clone the repository:

   `git clone https://github.com/craigybaeb/AGREE.git`

2. Navigate to the project src directory:

   `cd AGREE-API/src`

3. Install the required dependencies:

   `pip3 install -r requirements.txt`

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

To start the AGREE API server using Python, run the following command from the /src directory:

`python -m flask run`

By default, the API server will run on `http://localhost:5000`.

## Performance Considerations

The AGREE API provides powerful functionality for calculating disagreement and performing aggregation. However, there are a few performance considerations to keep in mind to ensure optimal usage:

### Number of Explainers

The computation time for calculating disagreement increases exponentially with the number of explainers used. Therefore, it is recommended to reduce the number of instances to explain as the number of explainers increases. This can help mitigate longer computation times and ensure efficient processing of the API requests.

### Disagreement Metric

By default, the AGREE API uses the "Case Alignment" metric for calculating disagreement. While this metric is more robust and provides better aggregations, it may take longer to compute. If faster explanations are desired, it is recommended to use alternative feature overlap-based methods, such as "Feature Agreement," "Sign Agreement," or others provided by the API.

Consider your specific requirements and time constraints when choosing the appropriate disagreement metric to strike a balance between accuracy and computation time.

## API Endpoints

The AGREE API exposes the following endpoints:

### `POST /disagreement`

Calculate the disagreement between explainers.

**Request Parameters**

- `disagreement_metric` (string): The method used to calculate disagreement.
- `average_method` (string): The average method used in aggregation (median or mean).
- `data_to_explain` (numpy array): A numpy array of the data to explain.
- `scope` (string): The scope of the explanation (global or local).
- `num_neighbours` (integer): The number of neighbours to compare in the case base when using case align.
- `k` (integer): The number of features used to determine feature agreement (does not apply to case align).
- `f` (integer[]): A list of feature IDs to compare in pairwise rank agreement and rank correlation.

**Example Request**

```bash
curl -X POST http://localhost:5000/disagreement \
  -H "Content-Type: application/json" \
  -d '{
    "disagreement_metric": "case_align",
    "disagreement_scores": {
      "LIME": 0.9,
      "SHAP": 0.8
    },
    "average_method": "mean",
    "data_to_explain": [[1, 2, 3], [4, 5, 6]],
    "scope": "global",
    "k": 3,
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

**Status Codes**

- `200 OK`: Indicates a successful calculation. The response will contain the calculated disagreement information.
- `400 Bad Request`: Indicates that the input parameters are invalid or missing.

  - If any of the following parameters are missing, the API will return a 400 error:
    - `disagreement_metric`: The method used to calculate disagreement.
    - `overall_disagreement`: The overall agreement confidence between explainers.
    - `disagreement_scores`: A dictionary containing all of the explainers used and their disagreement scores.
    - `average_method`: The method used to determine the average (median or mean).
    - `data_to_explain`: A numpy array of the data to explain.
    - `model`: A Keras model file to explain.
    - `scope`: The scope of the explanation (global or local).

  - Additional requirements and validation for the input parameters:
    - `data_to_explain` must be a 2D array of the same shape.
    - There must be at least 2 explainers in the `disagreement_scores` dictionary.
    - The `model` file must have the extension `.h5`.
    - The `scope` parameter must be either "local" or "global".
    - The `average_method` parameter must be either "mean" or "median".
    - The `disagreement_metric` must be one of the predefined values.

- `500 Internal Server Error`: Indicates an unexpected error occurred during the calculation.

Please note that the API server should be running locally at \`http://localhost:5000`.

## Contributing

Contributions to the AGREE API are welcome! If you find any issues or would like to propose improvements, please open an issue or submit a pull request.

## Author
[![Craig Pirie](https://scholar.googleusercontent.com/citations?view_op=medium_photo&user=LEqE644AAAAJ&citpid=1)](https://scholar.google.com/citations?user=LEqE644AAAAJ&hl=en)

Craig Pirie is a part-time PhD student at the Robert Gordon University (RGU), specializing in ensemble explainable (XAI) methods and solving the disagreement problem between explainers. He is currently working as a full-time research assistant at RGU. He is expected to complete his PhD studies in the year 2025.

To explore more of Craig's research and academic profiles, you can visit the following links:

- [Google Scholar](https://scholar.google.com/citations/your-profile)
- [ORCID](https://orcid.org/your-profile) - (Or use the ORCID 0000-0002-6799-0497)
- [RGU Worktribe](https://rgu-repository.worktribe.com/person/1065030/craig-pirie)
- [LinkedIn](https://www.linkedin.com/in/craig-pirie-aberdeen/)

Feel free to reach out to Craig for any inquiries or collaborations at [c.pirie11@rgu.ac.uk](mailto:c.pirie11@rgu.ac.uk).

## Future Work

In the future, Craig plans to further extend the AGREE (Aggregation for Robust Explanation Experience) method and API to enhance its capabilities and address additional challenges in the field of explainable AI. Some of the planned extensions include:

1. **Integration of Counterfactual Explanations**: Craig aims to incorporate counterfactual explanations into the AGREE framework. This will allow the measurement of disagreement between counterfactual explanations and the aggregation of these explanations. The counterfactual explanations will adhere to the principles of fairness, providing only plausible and actionable insights.

2. **Natural Language Explanations**: Craig aims to introduce natural language explanations within the AGREE API. This extension aims to alleviate the cognitive burden associated with the disagreement problem. The natural language explanations will not only explain the underlying models but also provide insights into the explainers themselves and their levels of disagreement.

3. **Front-End Interface**: To enhance usability and accessibility, Craig plans to develop a user-friendly front-end interface that interacts with the AGREE API. This interface will allow users to conveniently call the AGREE API and receive aggregated explanations through an intuitive and interactive platform.

Stay tuned for these exciting developments!

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or inquiries about the AGREE API, please contact:

Email: c.pirie11@rgu.ac.uk

---

## Citation

If you use the AGREE API in your research work or publications, please cite it as:

```bash
@article{pirie2023agree,
  title={AGREE: A Feature Attribution Aggregation Framework to Address Explainer Disagreements with Alignment Metrics},
  author={Pirie, Craig and Wiratunga, Nirmalie and Wijekoon, Anjana and Moreno-Garcia, Carlos Francisco},
  year={2023}
}
```
