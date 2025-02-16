import requests
import json
import os

def create_subscription(product_id: str, customer_email: str, first_name: str, last_name: str):
    """
    Creates a new subscription in Maxio/Chargify using remittance as the payment collection method

    Args:
        product_id: The ID of the product to subscribe to
        customer_email: The customer's email address
        first_name: The customer's first name
        last_name: The customer's last name

    Returns:
        dict: The created subscription details
    """
    api_key = os.environ.get('MAXIO_API_KEY')
    subdomain = os.environ.get('MAXIO_SUBDOMAIN')

    if not api_key or not subdomain:
        raise ValueError("MAXIO_API_KEY and MAXIO_SUBDOMAIN environment variables must be set")

    headers = {
        'Content-Type': 'application/json'
    }

    auth = (api_key, 'x')

    payload = {
        'subscription': {
            'product_id': product_id,
            'customer_attributes': {
                'email': customer_email,
                'first_name': first_name,
                'last_name': last_name
            },
            'payment_collection_method': 'remittance'
        }
    }

    response = requests.post(
        f'https://{subdomain}.chargify.com/subscriptions.json',
        headers=headers,
        auth=auth,
        json=payload
    )

    try:
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        error_message = f"Error creating subscription: {str(e)}"
        if response.text:
            try:
                error_details = response.json()
                error_message += f"\nDetails: {json.dumps(error_details, indent=2)}"
            except json.JSONDecodeError:
                error_message += f"\nResponse: {response.text}"
        raise Exception(error_message)

    return response.json()