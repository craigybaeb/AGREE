from flask import abort
from services.aggregate_service import AggregateService

class AggregateController:
    AGGREGATE_METHODS = ["method1", "method2", "method3"]

    @staticmethod
    def calculate_aggregate(data):
        aggregate_method = data.get("aggregate_method")

        if aggregate_method not in AggregateController.AGGREGATE_METHODS:
            abort(400, f"Invalid aggregate method. Expected one of: {', '.join(AggregateController.AGGREGATE_METHODS)}")

        # Call the AggregateService to perform the aggregation calculation
        result = AggregateService.calculate_aggregate(data)

        # Return the response
        return result
