import unittest
from app import app

class DisagreementEndpointTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def setUpPayload(self):
        # Define the base payload
        self.payload = {
            "disagreement_metric": "case_align",
            "data_to_explain": [1, 2, 3, 4, 5],
            "model": "model.h5",
            "explainers": {
                "LIME": [0.1, 0.2, 0.3, 0.4, 0.5],
                "SHAP": [0.5, 0.4, 0.3, 0.2, 0.1],
                "IG": [0.2, 0.4, 0.6, 0.8, 1.0]
                    },
            "scope": "local",
            "average_method": "median"

            }

    def test_disagreement_calculation(self):
        self.setUpPayload()

        # Make a POST request to the disagreement endpoint
        response = self.app.post('/disagreement', json=self.payload)

        # Assert the response status code
        self.assertEqual(response.status_code, 200)

        # Assert the response content
        response_data = response.get_json()
        self.assertEqual(response_data['disagreement_metric'], 'case_align')
        self.assertIsInstance(response_data['overall_disagreement'], float)
        self.assertIsInstance(response_data['disagreement_scores'], dict)
        self.assertIsInstance(response_data['average_method'], str)

    def test_missing_params(self):
        PARAMS = ["disagreement_metric", "scope", "model", "explainers","average_method", "data_to_explain"]
        i=0

        for param in PARAMS:
            with self.subTest(i=i):
                # Prepare an invalid request payload
                self.setUpPayload()
                del self.payload[param]

                # Make a POST request to the disagreement endpoint
                response = self.app.post('/disagreement', json=self.payload)
                # Assert the response status code
                self.assertEqual(response.status_code, 400)

                i += 1

    def test_invalid_metric(self):

        # Prepare an invalid request payload
        self.setUpPayload()
        self.payload["disagreement_metric"] = "This shouldn't work"

        # Make a POST request to the disagreement endpoint
        response = self.app.post('/disagreement', json=self.payload)
        # Assert the response status code
        self.assertEqual(response.status_code, 400)

    def test_invalid_average(self):

        # Prepare an invalid request payload
        self.setUpPayload()
        self.payload["average_method"] = "This shouldn't work"

        # Make a POST request to the disagreement endpoint
        response = self.app.post('/disagreement', json=self.payload)
        # Assert the response status code
        self.assertEqual(response.status_code, 400)

    def test_invalid_scope(self):

        # Prepare an invalid request payload
        self.setUpPayload()
        self.payload["scope"] = "This shouldn't work"

        # Make a POST request to the disagreement endpoint
        response = self.app.post('/disagreement', json=self.payload)
        # Assert the response status code
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
