import requests
import json
URL = "http://vmipaddress/computeMetadata/v1/"
response = requests.get(url = URL)
 if response.status_code == 200:
            print("sucessfully fetched the instance metadata")
            self.formatted_print(response.json())
        else:
            print("Unable to find instance metadata {response.status_code}")
  