import requests
import json
import os
import sys

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from abdm_service.utils.common import get_token, generate_uuid, get_current_time



class ABHARequestOTPView(APIView):
    def get(self, request):
        try:
            url = "https://abhasbx.abdm.gov.in/abha/api/v3/phr/web/login/abha/request/otp"

            payload = json.dumps({
                "loginHint": "abha-address",
                "loginId": "Oa5p3yymN7dzfqL/hjW8+yTWXqD9EqGoqQPKEs7bVd1HoD+Kp3D30DIf32s4zR52W30IfTYf2OT97GHy1mAToKTF/N6j4SCNA93Zed+Kg3O3CDOQJYIuvgaPFekbVIuoYEmB4MUbr3I/w6EKHXkndAtWs6dHsaYnfRFjfzq/u0htflCCGugelRO2a2I1w+XORaSBQsOeCDtSZPXiAzaFgOSxralfjtybooIYLrOh5UFlXUYbrJTr9HXHRNGxYFzYD00ujjNbOWMp3QH1LPkE/nbyOmoiIzQPJmYbPAxL3i3Slu6c1enKeUvOSrmVdvv32eFfDH1s1n35n2KgWIgfzgCLC4m1Z+3D5ejAk/gH47viYt2aV4tbOmsM23+r9jLyJWG1QfbVDhK0H35j4J1B2qiCuZ+HKwnafbu5fIQJ1b9cAsxt88W17etJC1HJwWkvI1KR3XQNPXAPyXcYvh3eMXelwvnsWGXxsmvIinPqV7c2OjV1FnWu3m6cxObwP0Qmq3x27lmqDRQW1jH02w5nzIpkkJL20iHw5D22xUM7eV/JiEtQJK5kS5o6/d/fkmzB3xo2C5D0B8Eo8/cXr4sUUbLbkz7yO4vNTqcpZtpKtK+g02zlAYMoDo0JM0cfzOBEXlTAuXVDSlkSzSifblb4JMRAKqMi1C037QLX2iAaUyQ=",
                "otpSystem": "abdm",
                "scope": [
                    "abha-address-login",
                    "mobile-verify"
                ]
            })

            headers = {
                'Content-Type': 'application/json',
                'REQUEST-ID': f'{generate_uuid()}',
                'TIMESTAMP': f'{get_current_time()}',
                'Authorization': f'Bearer {get_token()}'
            }

            response = requests.request("POST", url, headers=headers, data=payload, verify=False)
            response.raise_for_status()
            return Response(response.json(), status=status.HTTP_200_OK)
        except requests.exceptions.Timeout:
            return Response({"error": "Request timed out"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class HealthView(APIView):
    def get(self, request):
        return Response({"message":"Service is up"}, status=status.HTTP_200_OK)

class ABHASessionView(APIView):
    def get(self, request):
        try:
            session_url = "https://dev.abdm.gov.in/gateway/v0.5/sessions"

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
            response.raise_for_status()
            return Response(response.json(), status=status.HTTP_200_OK)
        except requests.exceptions.Timeout:
            return Response({"error": "Request timed out"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_200_OK)
