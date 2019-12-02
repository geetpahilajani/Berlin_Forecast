import requests
import json
from flatten_json import flatten
import csv


def api_read():
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    api = '3a875dd4a8f56d02cccbc8c8fdfe8f39'
    city = 'Berlin,DE'

    # Formatting the Url for the request to call

    format_url = '{0}?q={1}&appid={2}'.format(url, city, api)

    try:
        response = requests.get(format_url)

        forecast_jsn = response.json()

        forecast_dump = json.dumps(forecast_jsn, indent=5)

        response.raise_for_status()

    except requests.exceptions.HTTPError as http_err:

        print("Http Error:", http_err)

    except requests.exceptions.ConnectionError as conn_err:

        print("Error Connecting:", conn_err)

    except requests.exceptions.Timeout as time_err:

        print("Timeout Error:", time_err)

    return forecast_dump

# Writing a json string into a json file


def Write_File(jsondata):

    Js_dump = jsondata()

    file = open('Berlin_forecast.json', 'w')

    file.write(Js_dump)

#   Writing the data in csv file
    parsed_json = json.loads(Js_dump)
    flat = flatten(parsed_json)
    with open('forecast.csv', 'w') as file:
        w = csv.DictWriter(file, flat.keys())
        w.writeheader()
        w.writerow(flat)

    print("Files are Created")


if __name__ == '__main__':
    Write_File(api_read)





