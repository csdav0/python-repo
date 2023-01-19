#!/usr/bin/env python3

import requests
import datetime
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"

def main():

    req = requests.get(URL).json()
    position= {}
    position['Lon'] = req['iss_position']['longitude']
    position['Lat'] = req['iss_position']['latitude']
    coordinates= (position['Lat'], position['Lon'])
    locate = rg.search(coordinates)
    city = locate[0]['name']
    country = locate[0]['cc']
    print("CURRENT LOCATION OF THE ISS:")
    print(f"Timestamp: {datetime.datetime.fromtimestamp(req['timestamp'])}")
    print(f"Lon: {position['Lon']}")
    print(f"Lat: {position['Lat']}")
    print(f"City/Country: {city}, {country}")

if __name__ == "__main__":
    main()
