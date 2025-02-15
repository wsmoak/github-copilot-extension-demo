# Maxio Copilot Extension

This GitHub Copilot Extension allows you to create subscriptions in Maxio (formerly Chargify) directly through GitHub Copilot Chat.

## Setup

1. Create a GitHub App and configure it as a Copilot Extension
2. Set the following environment variables:
   - `MAXIO_API_KEY`: Your Maxio/Chargify API key
   - `MAXIO_SUBDOMAIN`: Your Maxio/Chargify subdomain

## Usage

In GitHub Copilot Chat, you can create a subscription using natural language:

```
/maxio-subscription create a new subscription for product ABC123 for customer user@example.com
```

## Development

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your environment variables in a `.env` file
4. Make your changes
5. Push to deploy (requires GitHub App configuration)

## License

MIT