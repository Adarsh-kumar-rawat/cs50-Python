import sys
import requests

def main():
    # Ensure a command-line argument is provided
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        # Parse the number of Bitcoins to buy
        n = float(sys.argv[1])
        if n <= 0:
            raise ValueError
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Define the API endpoint and your API key
    url = "https://rest.coincap.io/v3/assets/bitcoin"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        price = float(data['data']['priceUsd'])
    except requests.RequestException:
        sys.exit("Request failed")
    except KeyError:
        sys.exit("Invalid response structure")

    total_cost = n * price
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
