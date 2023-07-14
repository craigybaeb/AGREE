from flask import jsonify, request
from controllers.disagreement_controller import DisagreementController
from controllers.aggregate_controller import AggregateController

from routes import api

@api.route('/', methods=['GET'])
def index():
    welcome_message = "Welcome to the API! This API provides functionality for calculating disagreement and aggregation between explainers."

    routes = [
        {
            'route': '/disagreement',
            'method': 'POST',
            'description': 'Calculate disagreement between explainers',
            'parameters': [
                {
                    'name': 'disagreement_metric',
                    'type': 'string',
                    'description': 'Method used to calculate disagreement',
                    'required': True
                },
                {
                    'name': 'overall_disagreement',
                    'type': 'float',
                    'description': 'Overall agreement confidence between explainers',
                    'required': True
                },
                # Add more parameters as needed
            ],
            'response': {
                'disagreement_metric': 'string',
                'overall_disagreement': 'float',
                'disagreement_scores': 'dictionary',
                'average_method': 'string'
            },
            'status_codes': [200, 400]
        },
        {
            'route': '/aggregate',
            'method': 'POST',
            'description': 'Calculate aggregation of explanations',
            'parameters': [
                {
                    'name': 'aggregate_method',
                    'type': 'string',
                    'description': 'Method used for aggregation',
                    'required': True
                },
                # Add more parameters as needed
            ],
            'response': {
                'aggregate_explanation': 'string',
                'scope': 'string'
            },
            'status_codes': [200, 400]
        },
        # Add more routes here
    ]

    return jsonify({
        'message': welcome_message,
        'routes': routes
    })
    
# Add the /disagreement route
@api.route('/disagreement', methods=['POST'])
def calculate_disagreement():
    data = request.get_json()
    return DisagreementController.calculate_disagreement(data)

# Add the /aggregate route
@api.route('/aggregate', methods=['POST'])
def calculate_aggregate():
    data = request.get_json()
    return AggregateController.calculate_aggregate(data)
