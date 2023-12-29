import requests, json, threading, time

RESULTS_FILE_NAME = "discrot_res.txt"

url = "https://api.discord.gx.games/v1/direct-fulfillment"

payload = json.dumps({
    "partnerUserId": "07dfa2474d25b0814182b182fb2efdd9ad678b563884ed896a0c043f90e002fc"
})
        
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Length': '84',
    'Content-Type': 'application/json',
    'Origin': 'https://www.opera.com',
    'Referer': 'https://www.opera.com/',
    'Sec-Ch-Ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'
}

while True:
    try:
        response = requests.request("POST", url, headers=headers, data=payload).json()

        token = response['token']

        url_discord = "https://discord.com/billing/partner-promotions/1180231712274387115/"
        url_nitro = url_discord+token

        print(url_nitro)

        with open(RESULTS_FILE_NAME, 'a') as file:
            file.write(f"{url_nitro}\n")
    except Exception as e: 
        print("\nError: {}\n".format(e))