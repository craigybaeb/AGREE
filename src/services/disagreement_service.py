class DisagreementService:
    @staticmethod
    def calculate_disagreement(data):
        # Perform the disagreement calculation
        # ...

        # Return the response
        response = {
            "disagreement_metric": data.get("disagreement_metric"),
            "overall_disagreement": 0.8,  # Replace with the actual overall disagreement value
            "disagreement_scores": {
                "explainer1": 0.9,  # Replace with the actual disagreement scores
                "explainer2": 0.7,
                "explainer3": 0.6
            },
            "average_method": data.get("average_method")
        }

        return response
