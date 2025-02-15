# Maxio Copilot Extension

This GitHub Copilot Extension allows you to create subscriptions in Maxio (formerly Chargify) directly through GitHub Copilot Chat.

## Setup

1. Create a GitHub App and configure it as a Copilot Extension
2. Copy the `.env.example` file to `.env` and set your environment variables:
   ```
   MAXIO_API_KEY=your_api_key_here
   MAXIO_SUBDOMAIN=your_subdomain_here
   PORT=5000
   ```

## Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the Flask server:
   ```bash
   python app.py
   ```

The server will start on http://localhost:5000 with the following endpoints:
- GET /health - Health check endpoint
- GET /manifest - Returns the skillset manifest
- POST /create_subscription - Creates a new subscription

## Testing Locally

You can test the API using curl:

```bash
# Health check
curl http://localhost:5000/health

# Get manifest
curl http://localhost:5000/manifest

# Create subscription
curl -X POST http://localhost:5000/create_subscription \
  -H "Content-Type: application/json" \
  -d '{
    "product_id": "prod_123",
    "customer_email": "customer@example.com",
    "payment_details": {
      "credit_card_attributes": {
        "first_name": "John",
        "last_name": "Doe",
        "card_number": "4111111111111111",
        "expiration_month": "12",
        "expiration_year": "2025",
        "cvv": "123"
      }
    }
  }'
```

## Development

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your environment variables in `.env`
4. Make your changes
5. Push to deploy (requires GitHub App configuration)

## Production Deployment

For production, you'll need to:
1. Deploy this Flask app to a server with HTTPS support
2. Set the appropriate environment variables
3. Update your GitHub App's webhook URL to point to your deployed instance

## License

MIT