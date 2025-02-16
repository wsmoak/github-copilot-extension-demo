from flask import Flask, request, jsonify
from src.functions.subscription import create_subscription
import yaml
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

# Load skillset definition
with open(os.path.join(BASE_DIR, 'src', 'skillset.yaml'), 'r') as file:
    skillset = yaml.safe_load(file)

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy"})

@app.route('/manifest', methods=['GET'])
def get_manifest():
    """Return the skillset manifest"""
    return jsonify(skillset)

@app.route('/create_subscription', methods=['POST'])
def handle_create_subscription():
    """Handle subscription creation requests"""
    try:
        data = request.json

        # Extract parameters from request
        product_id = data.get('product_id')
        customer_email = data.get('customer_email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        # Validate required parameters
        if not all([product_id, customer_email, first_name, last_name]):
            return jsonify({
                "error": "Missing required parameters"
            }), 400

        # Call the subscription creation function
        result = create_subscription(
            product_id=product_id,
            customer_email=customer_email,
            first_name=first_name,
            last_name=last_name
        )

        return jsonify(result)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)