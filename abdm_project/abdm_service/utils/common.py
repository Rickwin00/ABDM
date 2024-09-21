from datetime import datetime, timezone
import uuid
import json

import requests


def generate_uuid():
    generated_uuid = uuid.uuid4()
    return str(generated_uuid)


def get_token():

    session_url = "https://dev.abdm.gov.in/gateway/v0.5/sessions"

    # payload = json.dumps({
    #   "clientId": "SBX_002928",
    #   "clientSecret": "5b24ab9e-2194-4f5f-aca3-fdb0a4872312",
    #   "grantType": "client_credentials"
    # })
    payload = json.dumps({
      "clientId": "SBX_004588",
      "clientSecret": "34f903bb-98e2-447e-b176-9092ca1455ac",
      "grantType": "client_credentials"
    })
    headers = {
      'accept': 'application/json',
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", session_url, headers=headers, data=payload)

    return response.json().get("accessToken")

def get_current_time():
    now = datetime.now(timezone.utc)
    iso_format = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    return str(iso_format)

def get_bridge_id():
    Bridge_id = "SBX_004588"
    return Bridge_id

print(get_current_time())