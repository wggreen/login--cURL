import requests

session = requests.Session()

##Login

url = "http://www.toasttab.com/login"

payload={}
headers = {
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

response = session.request("GET", url, headers=headers, data=payload)

##Login 2

url = "https://www.toasttab.com/login"

payload={}
headers = {
  'authority': 'www.toasttab.com',
  'pragma': 'no-cache',
  'cache-control': 'no-cache',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'sec-fetch-site': 'none',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-user': '?1',
  'sec-fetch-dest': 'document',
  'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
  'sec-ch-ua-mobile': '?0',
  'accept-language': 'en-US,en;q=0.9'
}

response = session.request("GET", url, headers=headers, data=payload)

login_cookies = session.cookies.items()

cookie_string = login_cookies[1][0] + '=' + login_cookies[1][1] + '; ' + login_cookies[7][0] + '=' + login_cookies[7][1] + '; ' + login_cookies[0][0] + '=' + login_cookies[0][1]


##authorize?

url = "https://auth.toasttab.com/authorize?force_mfa=false&client_id=TKTKTK&redirect_uri=https://www.toasttab.com/authentication/callback&response_type=code&scope=openid%20profile&audience=https://toast-users-api/&state=TKTKTK"

payload={}
headers = {
  'Connection': 'keep-alive',
  'Pragma': 'no-cache',
  'Cache-Control': 'no-cache',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Sec-Fetch-Site': 'none',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-User': '?1',
  'Sec-Fetch-Dest': 'document',
  'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
  'sec-ch-ua-mobile': '?0',
  'Accept-Language': 'en-US,en;q=0.9',
  'Cookie': cookie_string
}

response = session.request("GET", url, headers=headers, data=payload)

authorize_cookies = session.cookies.items()

cookie_string = authorize_cookies[4][0] + '=' + authorize_cookies[4][1] + '; ' + authorize_cookies[2][0] + '=' + authorize_cookies[2][1] + '; ' + authorize_cookies[5][0] + '=' + authorize_cookies[5][1] + '; ' + authorize_cookies[3][0] + '=' + authorize_cookies[3][1] + '; ' + authorize_cookies[1][0] + '=' + authorize_cookies[1][1] + '; ' + authorize_cookies[7][0] + '=' + authorize_cookies[7][1] + '; ' + authorize_cookies[0][0] + '=' + authorize_cookies[0][1]

#login?

url = "https://auth.toasttab.com/login?state=TKTKTK&client=TKTKTK&protocol=oauth2&force_mfa=false&redirect_uri=https%3A%2F%2Fwww.toasttab.com%2Fauthentication%2Fcallback&response_type=code&scope=openid%20profile&audience=https%3A%2F%2Ftoast-users-api%2F"

payload={}
headers = {
  'Connection': 'keep-alive',
  'Pragma': 'no-cache',
  'Cache-Control': 'no-cache',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Sec-Fetch-Site': 'none',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-User': '?1',
  'Sec-Fetch-Dest': 'document',
  'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
  'sec-ch-ua-mobile': '?0',
  'Accept-Language': 'en-US,en;q=0.9',
  'Cookie': cookie_string}

response = session.request("GET", url, headers=headers, data=payload)

print(response.status_code)

login_cookies = session.cookies.items()

##for x in range(0, len(login_cookies)):
##    if(authorize_cookies[x][1] != login_cookies[x][1]):
##        print(login_cookies[x][0], "changed from authorize to login")


##bundle.min.js

url = "https://browser.sentry-cdn.com/5.19.2/bundle.min.js"

payload={}
headers = {
  'authority': 'browser.sentry-cdn.com',
  'pragma': 'no-cache',
  'cache-control': 'no-cache',
  'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
  'origin': 'https://auth.toasttab.com',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
  'accept': '*/*',
  'sec-fetch-site': 'cross-site',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'script',
  'accept-language': 'en-US,en;q=0.9'
}

response = session.request("GET", url, headers=headers, data=payload)

bundle_cookies = session.cookies.items()

for x in range(0, len(bundle_cookies)):
    if(login_cookies[x][1] != bundle_cookies[x][1]):
        print(bundle_cookies[x][0], "changed from login to bundle")

##lock.min.js

url = "https://cdn.auth0.com/js/lock/11.23/lock.min.js"

payload={}
headers = {
  'authority': 'cdn.auth0.com',
  'pragma': 'no-cache',
  'cache-control': 'no-cache',
  'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
  'accept': '*/*',
  'sec-fetch-site': 'cross-site',
  'sec-fetch-mode': 'no-cors',
  'sec-fetch-dest': 'script',
  'accept-language': 'en-US,en;q=0.9'
}

response = session.request("GET", url, headers=headers, data=payload)

lock_cookies = session.cookies.items()

for x in range(0, len(lock_cookies)):
    if(bundle_cookies[x][1] != lock_cookies[x][1]):
        print(lock_cookies[x][0], "changed from login to bundle")

##pVItbBZWkpwu8H9Ddm0oPcSfagxrkrtB

url = "https://config.toasttab.auth0.com/client/TKTKTK"

payload={}
headers = {
  'authority': 'config.toasttab.auth0.com',
  'pragma': 'no-cache',
  'cache-control': 'no-cache',
  'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
  'accept': '*/*',
  'sec-fetch-site': 'cross-site',
  'sec-fetch-mode': 'no-cors',
  'sec-fetch-dest': 'script',
  'accept-language': 'en-US,en;q=0.9',
  'Cookie': 'TKTKTK'
}

response = session.request("GET", url, headers=headers, data=payload)

config_cookies = session.cookies.items()

for x in range(0, len(config_cookies)):
    if(lock_cookies[x][1] != config_cookies[x][1]):
        print(config_cookies[x][0], "changed from login to bundle")
    
##challenge

url = "https://auth.toasttab.com/usernamepassword/challenge"

payload="{\"state\":\"TKTKTK\"}"
headers = {
  'Connection': 'keep-alive',
  'Pragma': 'no-cache',
  'Cache-Control': 'no-cache',
  'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
  'Auth0-Client': 'TKTKTK',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
  'Content-Type': 'application/json',
  'Accept': '*/*',
  'Origin': 'https://auth.toasttab.com',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'TKTKTK',
  'Accept-Language': 'en-US,en;q=0.9',
  'Cookie': 'TKTKTK'
}

response = session.request("POST", url, headers=headers, data=payload)

challenge_cookies = session.cookies.items()

for x in range(0, len(challenge_cookies)):
    if(config_cookies[x][1] != challenge_cookies[x][1]):
        print(challenge_cookies[x][0], "changed from login to bundle")

##toast-login.json

url = "https://pos.toasttab.com/toast-login.json"

payload={}
headers = {
  'authority': 'pos.toasttab.com',
  'pragma': 'no-cache',
  'cache-control': 'no-cache',
  'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
  'accept': '*/*',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
  'origin': 'https://auth.toasttab.com',
  'sec-fetch-site': 'same-site',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'accept-language': 'en-US,en;q=0.9'
}

response = session.request("GET", url, headers=headers, data=payload)

##ssodata

url = "https://auth.toasttab.com/user/ssodata"

payload={}
headers = {
  'Connection': 'keep-alive',
  'Pragma': 'no-cache',
  'Cache-Control': 'no-cache',
  'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
  'Accept': '*/*',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'TKTKTK',
  'Accept-Language': 'en-US,en;q=0.9',
  'Cookie': 'TKTKTK'
}

response = session.request("GET", url, headers=headers, data=payload)

cookies = session.cookies.items()

csrf = cookies[6][1]
