import time
import requests
import json
import datetime


TELEGRAM_BOT_TOKEN = "#token#"
CHAT_ID = "#chat_id#"

username = "....@hotmail.com"
password = "foobar"
login_url = "https://ais.usvisa-info.com/tr-tr/niv/users/sign_in"

ist_check_url = "https://ais.usvisa-info.com/tr-tr/niv/schedule/45756650/appointment/days/125.json?appointments[expedite]=false"
ank_check_url = "https://ais.usvisa-info.com/tr-tr/niv/schedule/45756650/appointment/days/124.json?appointments[expedite]=false"


def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)


while True:
    payload = f"utf8=%E2%9C%93&user%5Bemail%5D={username}&user%5Bpassword%5D={password}&policy_confirmed=1&commit=Oturum+A%C3%A7"
    headers = {
        "Accept": "*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "_yatri_session=Z0pnU2pmMWkzeFZ1K1VOWFoxbCthVFEzcU9qTEVTQjJRSnJ2WlJoNUc0Y0xpSXJ3NUNkNm5XbWMraVRwUm8xN3ZjbFB3Zy91TVc0OW50QjdaSkdNeklYWWxwM2RlU0kxaTF5eWo1R0dsY2FYT0JhcVZCdmV3VTh1bDl5SFFkenBmK0xkV0FqSXVCWk10UDBoYnZFYmZNd0svRmlkdDIzZDdUejBUV1ZYQVA5QjVQb1hyUHREc2t0bVVOYlBVa1VDdkJxRmRKNDR0d01CemxPOFR6KzJhdkN3Y2J3UEkvVjVDWkpST3VJRi9TWVJrMVExYmR6M0xuSi8rSTA4ckcrYVAyQVNUOEs1ZmZrTlBhYnFxdXY0d2FUZENKVk1sdmlsSWUwR2N1MVF3ZDNpaEIrbnBqK3pZZ0JJQllGWVZKaithVWZpZ2JsSkFmMTRYcHhhT0xxaldBYmx6bThyZUR2RVo4eFc2bGRBblNJPS0tcndiQnlwaFhuYlM3Y0Zzb1E5Z1VkUT09--2385f72d171a40e71d7504fb02ecff45472fbd55; _yatri_session=WnY0aUFLaE1tKzZZZTl4U1BsSStjQk5QMUVmYVd4RFAxY3czMEptc3p3aVNPb2NEK2hEL3NlcFdiYW9zUE4zZENDMVRObzIwZjFVTDBKRlpCY2hydDZQeTBrVUNobE1UVmQrcXozZmZZR2RibUNjTkF1SCtDNnpEd1U3UXZTSkxta3ZhVnhPVm54Y3ZQUHJVZFdrZE5aZkg3VVJQMjN2QjNPNkJKanppcHJtdlJlUytXRGdybXVKaURhZzg4Qi9waEhCczZaa2hUZG4wb2lSOVFTTGxOZHIrSnRNcEs5V3hVVHcyalByVkh4MkFnQkM3amYvZHhWRlFWUXo1RWxjV1FheXZWTnhpV2Z4ZTUvcTdxcjhzcCtXNjJBbGNBQVhaVCtqMGRzWUZoY09rR21tSElKeFcwZXFkOGF5eHFjUnNWMXozUGdLdmIzNDBMQi9FODNrTEJDTWF0UVFnaE9zQnBQQ0NsL1JNU3pGRW1GVnBtaFNZR0c1OFNBOTV2KzFKNDlBZlFwU1VWcTRMa1doSHV1ODc1SlBJMFc4eW8rVWVKY09td3NKRkhOVmNuVkZkb1dPQkpDeThKamV1YmVzci0tWHhMaWkrdllJS1RQNkdQR0wrbXY1dz09--3b2707851051112b19b12e1a0a59fbb797c8b361",
        "Origin": "https://ais.usvisa-info.com",
        "Pragma": "no-cache",
        "Referer": "https://ais.usvisa-info.com/tr-tr/niv/users/sign_in",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "X-CSRF-Token": "ccU8Qet5sTM3J/Q9hWvi9U0LwhU8Fz963G0VxkrotsDdNjTwMqMqYiWDSsl3DaIAwvjZZbaixrTl9AeUu89X+A==",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }

    response = requests.request("POST", login_url, headers=headers, data=payload)

    yatri_session_cookie = response.cookies["_yatri_session"]

    with open("log", "a") as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": f"_yatri_session={yatri_session_cookie}",
        "Pragma": "no-cache",
        "Referer": "https://ais.usvisa-info.com/tr-tr/niv/schedule/45756650/appointment?utf8=%E2%9C%93&applicants%5B%5D=53232831&applicants%5B%5D=53232841&confirmed_limit_message=1&commit=Devam+Et",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "X-CSRF-Token": "X+JoUqtXXf586Uwlg7ibfuK1GKG7eje66GcnNGFjy2b1OGk2UV6fAm1JfNKgu5Bw1Q1KiHm4FsIlrhIRZ76FJw==",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    response = requests.get(ist_check_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = json.loads(response.text)
        for appointment in data:
            date = datetime.datetime.strptime(appointment["date"], "%Y-%m-%d").date()
            with open("log", "a") as f:
                f.write(f"{date}\n")
            if date <= datetime.date(2023, 10, 10):
                message = f'A new appointment is available on {appointment["date"]}'
                send_telegram_message(message)

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": f"_yatri_session={yatri_session_cookie}",
        "Pragma": "no-cache",
        "Referer": "https://ais.usvisa-info.com/tr-tr/niv/schedule/45756650/appointment?utf8=%E2%9C%93&applicants%5B%5D=53232831&applicants%5B%5D=53232841&confirmed_limit_message=1&commit=Devam+Et",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "X-CSRF-Token": "X+JoUqtXXf586Uwlg7ibfuK1GKG7eje66GcnNGFjy2b1OGk2UV6fAm1JfNKgu5Bw1Q1KiHm4FsIlrhIRZ76FJw==",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    response = requests.get(ank_check_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = json.loads(response.text)
        for appointment in data:
            date = datetime.datetime.strptime(appointment["date"], "%Y-%m-%d").date()
            with open("log", "a") as f:
                f.write(f"{date}\n")
            if date <= datetime.date(2023, 10, 10):
                message = f'A new appointment is available on {appointment["date"]}'
                send_telegram_message(message)

    time.sleep(600)  # Pause for 10 minutes (600 seconds)
