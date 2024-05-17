import requests
import json

def fetch_data(api_url):
    """
    Fetch data from the given API URL with error handling.
    
    Parameters:
        api_url (str): The URL of the API to fetch data from.
    
    Returns:
        dict or None: The JSON response from the API if successful, None otherwise.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

def find_citations(response_text, sources):
    """
    Find citations for a given response text based on sources.

    Parameters:
        response_text (str): The response text to find citations for.
        sources (list): A list of source dictionaries, each containing 'id', 'context', and 'link'.

    Returns:
        list: A list of citation dictionaries with 'id' and 'link' keys.
    """
    citations = []
    for source in sources:
        context_keywords = source['context'].split()
        matched = False
        for keyword in context_keywords:
            if keyword.lower() in response_text.lower():
                matched = True
        if matched and source.get('link'):  # Check if link is not empty
            citation = {
                'id': source['id'],
                'link': source['link']
            }
            citations.append(citation)
    return citations

def process_api_data(api_url):
    """
    Process API data to extract responses and their citations.

    Parameters:
        api_url (str): The URL of the API to fetch data from.

    Returns:
        list: A list of dictionaries containing 'response' and 'citations'.
    """
    data = fetch_data(api_url)
    if not data:
        return []

    result = []
    for item in data:
        response = item['response']
        sources = item['sources']
        citations = find_citations(response, sources)
        result.append({
            'response': response,
            'citations': citations
        })
    return result

# Mock data for testing
mock_response = [
    {
        "response": "Yes, we offer online delivery services through major platforms like Swiggy and Zomato. You can also reserve a table directly from our website if you are planning to have breakfast!",
        "sources": [
            {
                "id": "71",
                "context": "Order online Thank you for your trust in us! We are available on all major platforms like zomato, swiggy. You can also order directly from our website",
                "link": "https://orders.brikoven.com"
            },
            {
                "id": "75",
                "context": "Do you give franchise if the brand No, we currently don't offer franchise opportunities for BrikOven! Although do feel free to drop in an email at theteam@brikoven.com so we can get in touch with you at a later stage if we do decide to give out franchisees",
                "link": ""
            },
            {
                "id": "8",
                "context": "Breakfast Reservations For Breakfast, we recommend making reservations in advance. Reservation is only available through our website",
                "link": "https://www.brikoven.com/reservations"
            }
        ]
    }
]

def process_mock_data(mock_data):
    """
    Process mock data to extract responses and their citations.

    Parameters:
        mock_data (list): A list of mock data dictionaries containing 'response' and 'sources'.

    Returns:
        list: A list of dictionaries containing 'response' and 'citations'.
    """
    result = []
    for item in mock_data:
        response = item['response']
        sources = item['sources']
        citations = find_citations(response, sources)
        result.append({
            'response': response,
            'citations': citations
        })
    return result

# Testing the find_citations function with mock data
response_text = mock_response[0]["response"]
sources = mock_response[0]["sources"]
citations = find_citations(response_text, sources)

expected_citations = [
    {
        "id": "71",
        "link": "https://orders.brikoven.com"
    },
    {
        "id": "8",
        "link": "https://www.brikoven.com/reservations"
    }
]
api_url = "https://devapi.beyondchats.com/api/get_message_with_sources"

# Process mock data
processed_data = process_mock_data(mock_response)
if processed_data:
    print(json.dumps(processed_data, indent=2))

# Save the result to a JSON file
with open('citations_output.json', 'w') as f:
    json.dump(processed_data, f, indent=2)

print("Citations have been saved to citations_output.json")
