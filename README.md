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

   `git clone <repository_url>`

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

   `docker-compose up\`

The API server will be accessible at `http://localhost:5000`.

### Running with Python

To start the AGREE API server using Python, run the following command from the project root directory:

`python -m flask run`

By default, the API server will run on `http://localhost:5000`.

## API Endpoints

The AGREE API exposes the following endpoints:

- `POST /disagreement`: Calculate the disagreement between explainers.
- `POST /aggregate`: Perform aggregation on explanations.
- `GET /`: Display the API information, available routes, and usage details.

For detailed information on the request parameters, response formats, and error codes, please refer to the API documentation.

## Contributing

Contributions to the AGREE API are welcome! If you find any issues or would like to propose improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or inquiries about the AGREE API, please contact:

Email: your-email@example.com

---

## Citation

If you use the AGREE API in your research work or publications, please cite it as:

[Provide citation details here]
