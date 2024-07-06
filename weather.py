import requests,json
def weather (location):
    r = f"http://api.weatherapi.com/v1/current.json?key=5f2c0d4cbe9245ffacb114438232506&q=Chennai&aqi=no"
    res = requests.get(r)
    content_str = res.content
    content1 = content_str.decode('utf-8')
    content = json.loads(content1)

    # print(content['location']['name'])
    # print(int(content['current']['temp_c']),"°C")
    return int(content['current']['temp_c'])

def get_ip_location():
    try:
        response = requests.get('https://ipinfo.io')
        
        if response.status_code == 200:
            data = response.json()
            
            ip = data.get('ip', 'N/A')
            city = data.get('city', 'N/A')
            region = data.get('region', 'N/A')
            country = data.get('country', 'N/A')
            location = data.get('loc', 'N/A')

            return city
        else:
            print(f"Failed to retrieve location information. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# weather('Chennai')
