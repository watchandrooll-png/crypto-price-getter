import requests

while True:
    choice = input("what crypto price do you wanna see g?\nchoice: ")

    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": f"{choice}",
        "vs_currencies": "usd"
    }

    response = requests.get(url,params)
    data = response.json()
    print(data)