from flask import abort
from services.disagreement_service import DisagreementService
import numpy as np

class DisagreementController:
    DISAGREEMENT_METRICS = [
        "case_align",
        "feature_agreement",
        "feature_agreement",
        "feature_agreement",
        "sign_agreement",
        "rank_agreement",
        "signed_rank_agreement",
        "pairwise_rank_agreement",
        "rank_corellation"
    ]
    AVERAGE_METHODS = ["mean", "median"]

    @staticmethod
    def calculate_disagreement(data):
        # Validate the required parameters
        required_parameters = ["data_to_explain", "average_method", "disagreement_metric", "explainers", "model", "scope"]
        missing_parameters = [param for param in required_parameters if param not in data]
        if missing_parameters:
            abort(400, f"Missing required parameter(s): {', '.join(missing_parameters)}")


        dataset = data.get("data_to_explain")
        average_method = data.get("average_method")
        disagreement_metric = data.get("disagreement_metric")
        explainers = data.get("explainers")
        model = data.get("model")
        scope = data.get("scope")

        # Validate the average_method parameter
        if average_method not in DisagreementController.AVERAGE_METHODS:
            abort(400, f"Invalid average method. Expected one of: {', '.join(DisagreementController.AVERAGE_METHODS)}")

        # Validate the disagreement_metric parameter
        if disagreement_metric not in DisagreementController.DISAGREEMENT_METRICS:
            abort(400, f"Invalid disagreement metric. Expected one of: {', '.join(DisagreementController.DISAGREEMENT_METRICS)}")

        # # Validate the model file extension
        # if not model.endswith(".h5"):
        #     abort(400, "Invalid model file. Expected a .h5 file")

        # Convert dataset and explainers to numpy arrays
        dataset = np.array(dataset)
        explainers = {explainer: np.array(explanation) for explainer, explanation in explainers.items()}

        # Validate the scope parameter
        if scope not in ["global", "local"]:
            abort(400, "Invalid scope. Expected 'global' or 'local'")

        # Call the DisagreementService to perform the disagreement calculation
        result = DisagreementService.calculate_disagreement(data)

        # Return the response
        return result
