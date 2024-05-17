# python-api-citation-extractor
    1 . Introduction
            This script fetches data from a specified API, processes it to find citations for given responses, and saves the results to a JSON file. The script includes functionality for handling errors during the              API request and excludes citations with empty links.
    2 . Requirements
            Python 3.x
            requests library
            To install the requests library, use:
            pip install requests
    3. Usage
            Ensure you have the requests library installed.
            Update the api_url variable with the appropriate API URL.
            Run the script to fetch, process, and save the data.
    4 . Code Overview
            fetch_data
            Fetches data from the given API URL with error handling.
    5 . find_citations
            Finds citations for a given response text based on sources.
    6 . process_api_data
            Processes API data to extract responses and their citations.
    7 . process_mock_data
            Processes mock data to extract responses and their citations.
    8 . Testing with Mock Data
            The script includes a mock data set to test the find_citations function.
    9 . Saving the Output
            The script saves the processed data to a JSON file.
