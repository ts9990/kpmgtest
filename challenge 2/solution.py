import requests

ENDPOINT = "http://169.254.169.254/metadata/instance?api-version=2021-02-01"
particular_data_key = "osType"
# Extract VM particular_data_key from instance metadata endpoint
headers = {'Metadata': 'True'}
data_dict = requests.get(ENDPOINT, headers=headers).json()


required_string = data_dict['particular_data_key']
print(required_string)
