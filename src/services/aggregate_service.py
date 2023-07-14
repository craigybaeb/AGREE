class AggregateService:
    @staticmethod
    def calculate_aggregate(data):
        # Perform the aggregation calculation
        # ...

        # Return the response
        response = {
            "aggregate_explanation": "This is the aggregate explanation",  # Replace with the actual aggregate explanation
            "scope": data.get("scope")
        }

        return response
