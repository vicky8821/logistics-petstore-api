import requests
import json

def get_endpoints(swagger_url):
    response = requests.get(swagger_url)
    swagger_json = response.json()
    endpoints = swagger_json.get('paths', {}).keys()
    return endpoints

if __name__ == "__main__":
    swagger_url = "http://petstore.swagger.io/v2/swagger.json"
    endpoints = get_endpoints(swagger_url)
    for endpoint in endpoints:
        print(endpoint)
