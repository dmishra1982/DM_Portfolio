# Program Name     : mishra_assignment12.1
# Program Overview : Program as per week 12 requirement - Final Project.
# -------------------------------------------------------------------------------------------------
# Version | Course # or Channel | Week# | Program Description    | Author            | Date       |
# --------|---------------------|-------|------------------------|-------------------|------------|
# 1.000   | DSC510 T301-2231-1  | 12    | Programming Assignment | DEBABRATA MISHRA  | 11/19/2022 |
#         |                     |       | for week # 12          |                   |            |
# ------------------------------------------------------------------------------------------------|
# ************************************************************************************************|
#                                            CHANGE LOG                                           |
# ************************************************************************************************|
# -------------------------------------------------------------------------------------------------
# Version | Change Request #    | Change(s) Description          | Author            | Date       |
# --------|---------------------|--------------------------------|-------------------|------------|
#         |                     |                                |                   |            |
#         |                     |                                |                   |            |
# --------|---------------------|--------------------------------|-------------------|------------|

# Imports
import requests
import json
import time
from tabulate import tabulate
from prettytable import PrettyTable

welcome_text = " Welcome to DM-Weather Information program Powered by OpenWeather !!! " \
               "\n Access current weather data for over 200,000 cities. For a precise forecast:" \
               "\n " \
               "\n US Location, Please enter :" \
               "\n                           5 digit U.S. Zip Code and Country Code (ex: 77494,US) " \
               "\n                        or City Name,State Code and Country Code (ex: Katy,TX,US)" \
               "\n " \
               "\n International Location, Please enter :" \
               "\n                           Postal / Zip Code and Country Code (ex: 411027,IN) " \
               "\n                        or City Name and Country Code (ex: Pune,IN)" \
               "\n"


def get_lon_lat():
    """ Get request for latitude and longitude based on user input """

    zip_url = 'http://api.openweathermap.org/geo/1.0/zip?'
    direct_url = 'http://api.openweathermap.org/geo/1.0/direct'
    latitude = 0.0
    longitude = 0.0
    appid = '02eb8187f8185c044ee3cd3a0f82b2d8'

    print("\n To get the weather forecast or current weather \n"
          " 1 - Lookup by City , State and country\n"
          " 2 - Lookup by Zip Code\n")

    user_option = input(" Please select one of the above : ").strip()
    while not (user_option == '1' or user_option == '2'):
        print(" You did not enter a valid selection, Please enter 1 - for lookup by location  or 2 - for ZIP ")
        user_option = input("\n Please select one of the above : ").strip()

    if user_option == '1':
        location_city = str(input(" Please enter the City name: ")).lower().strip()
        while not (len(location_city) > 0):
            print(" Please enter valid city name \n")
            location_city = str(input(" Please enter the City name: ")).lower().strip()

        location_country = str(input(" Please enter Country Code: ")).lower().strip()
        while not (len(location_country) >= 2):
            print(" Please enter valid country Code \n")
            location_country = str(input(" Please enter Country Code: ")).lower().strip()

        location_state = str(input(" Please enter state code (only for the US): ")).lower().strip()
        if location_country[:2] == "us":
            while not (len(location_state) >= 2):
                print(" Please enter valid US State Code \n")
                location_state = str(input(" Please enter US state Code: ")).lower().strip()

        if len(location_state) == 0:
            location = location_city + ',' + location_country[:2]
        else:
            location = location_city + ',' + location_state + ',' + location_country[:2]

        query_params = {'q': location, 'appid': appid}
        request_url = direct_url

    else:

        location_country = str(input(" Please enter Country Code:")).lower().strip()
        while not (len(location_country) >= 2):
            print(" Please enter valid country Code \n")
            location_country = str(input(" Please enter Country Code:")).lower().strip()

        location_zip = str(input(" Please enter Zip or Postal Code: ")).lower().strip()
        if location_country[:2] == "us" and location_zip[:5].isnumeric() is False:
            location_zip = ""
        while not (len(location_zip) >= 3):
            print(" Please enter valid Zip or Postal Code \n")
            location_zip = str(input(" Please enter Zip or Postal Code: ")).lower().strip()
            if location_country[:2] == "us" and location_zip[:5].isnumeric() is False:
                location_zip = ""

        if location_country[:2] == "us":
            location = location_zip[:5] + ',' + location_country[:2]
        else:
            location = location_zip + ',' + location_country[:2]

        query_params = {'zip': location, 'appid': appid}
        request_url = zip_url

    status = ""
    error_msg = ""

    try:
        get_response = requests.get(request_url, params=query_params, timeout=(5, 14))
        error_msg, status = api_error_check(get_response)
        if status == "fail":
            raise requests.ConnectionError

    except requests.exceptions.ConnectionError or requests.ConnectionError:
        print("\n" * 1)
        print("--------------------------------------------------------------------------------- ")
        print_text = " " * 81
        print(ansi_color('b_red', ansi_color('italic', print_text)))
        if len(error_msg.strip()) == 0:
            error_msg = " Internet Connection Error or HTTP Error"
            status = "fail"
        print(error_msg)
        print(" Please provide correct location details to get weather information....           ")
        print(ansi_color('b_red', ansi_color('italic', print_text)))
        print("--------------------------------------------------------------------------------- ")

    else:
        if get_response.status_code == 200 and len(json.loads(get_response.text)) != 0:
            get_response_parsed = json.loads(get_response.text)
            if user_option == '2':
                latitude = get_response_parsed['lat']
                longitude = get_response_parsed['lon']
            else:
                latitude = get_response_parsed[0]['lat']
                longitude = get_response_parsed[0]['lon']

    return error_msg, location, status, latitude, longitude
# ----------------------------------------------------------------------------------------------------------------------


def weather_current_and_forecast(latitude, longitude, location):
    """Makes a """

    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather'
    forecast_weather_url = 'https://api.openweathermap.org/data/2.5/forecast'
    appid = '02eb8187f8185c044ee3cd3a0f82b2d8'

    unit = input(" Please enter unit of temperature, F - Fahrenheit, C- Celsius, or K - Kelvin: ").upper().strip()
    while not (unit == 'F' or unit == 'C' or unit == 'K'):
        print(" Please enter valid  temperature unit/scale, Valid values are F or C or K \n")
        unit = input(" Please enter unit of temperature, F - Fahrenheit, C- Celsius, "
                     "or K - Kelvin: ").upper().strip()
    if unit == 'F':
        units = 'imperial'
    elif unit == 'C':
        units = 'metric'
    else:
        units = 'standard'

    query_params = {'lat': latitude, 'lon': longitude, 'units': units, 'appid': appid}
    status = ""
    error_msg = ""
    try:
        get_response = requests.get(current_weather_url, params=query_params, timeout=(5, 14))
        error_msg, status = api_error_check(get_response)

        if status == "fail":
            raise requests.ConnectionError

    except requests.exceptions.ConnectionError or requests.ConnectionError:
        print("\n" * 1)
        print("--------------------------------------------------------------------------------- ")
        print_text = " " * 81
        print(ansi_color('b_red', ansi_color('italic', print_text)))
        if len(error_msg.strip()) == 0:
            error_msg = " Internet Connection Error or HTTP Error"
            status = "fail"
        print(error_msg)
        print("--------------------------------------------------------------------------------- ")

    else:
        if get_response.status_code == 200 and len(json.loads(get_response.text)) != 0:
            current_parsed = json.loads(get_response.text)
            current_formatted(current_parsed, location, unit)

    if status == "pass":

        query_params = {'lat': latitude, 'lon': longitude, 'units': units, 'appid': appid}
        try:
            get_response = requests.get(forecast_weather_url, params=query_params, timeout=(5, 14))
            error_msg, status = api_error_check(get_response)

            if status == "fail":
                raise requests.ConnectionError

        except requests.exceptions.ConnectionError or requests.ConnectionError:
            print("\n" * 1)
            print("--------------------------------------------------------------------------------- ")
            print_text = " " * 81
            print(ansi_color('b_red', ansi_color('italic', print_text)))
            if len(error_msg.strip()) == 0:
                error_msg = " Internet Connection Error or HTTP Error"
            print(error_msg)
            print("--------------------------------------------------------------------------------- ")

        else:
            if get_response.status_code == 200 and len(json.loads(get_response.text)) != 0:
                current_parsed = json.loads(get_response.text)
                forecast_formatted(current_parsed, unit)

# ----------------------------------------------------------------------------------------------------------------------


def api_error_check(response):
    """ Validate the response message of API call """
    error_msg = ""
    status = "pass"
    try:
        response.raise_for_status()
        if response.status_code == 200 and len(json.loads(response.text)) == 0:
            error_msg = " " + str(response.status_code) + " - The entered location details are not correct."
            status = "fail"

    # except requests.exceptions.HTTPError:
    #    error_msg = " " + str(response.status_code) + " - HTTP Error."
    #    status = "fail"

    except requests.ConnectionError:
        error_msg = " " + str(response.status_code) + " - No Internet connection/ Error in connection."
        status = "fail"

    except requests.TooManyRedirects:
        error_msg = " " + str(response.status_code) + " - Exceeds maximum number of redirections."
        status = "fail"

    except requests.Timeout:
        error_msg = " " + str(response.status_code) + " - Timeout Error."
        status = "fail"

    except requests.RequestException:
        error_msg = " " + str(response.status_code) + " - The entered value(s) were not valid."
        status = "fail"

    return error_msg, status
# ----------------------------------------------------------------------------------------------------------------------


def current_formatted(parsed, location, unit):
    """Decodes the JSON data, formats the time variables to match proper time zones, then formats the printable
    output of the current weather"""

    city = str(json.dumps(parsed['name'])).replace('"', '')
    country = str(json.dumps(parsed['sys']['country'])).replace('"', '')
    timezone = int(json.dumps(parsed['timezone']))
    dt_value = int(json.dumps(parsed['dt']))
    current_time = time.strftime("%A, %b %d, %Y %I:%M %p", time.gmtime(dt_value + timezone))

    temp = "{:.2f}".format(float(json.dumps(parsed['main']['temp'])))
    feels_like = "{:.2f}".format(float(json.dumps(parsed['main']['feels_like'])))
    temp_min = "{:.2f}".format(float(json.dumps(parsed['main']['temp_min'])))
    temp_max = "{:.2f}".format(float(json.dumps(parsed['main']['temp_max'])))
    pressure = "{:.2f}".format(float(json.dumps(parsed['main']['pressure'])))
    humidity = int(json.dumps(parsed['main']['humidity']))
    conditions = str(json.dumps(parsed['weather'][0]['description'])).replace('"', '').title()

    print("_" * 81)
    print_text = " Current Weather Information for : " + location.upper() + (" " * (46 - len(location)))
    print(ansi_color('bold', ansi_color('b_green', ansi_color('italic', print_text))))
    print(f"\n Weather Report Reference Location    :  {city}, {country} ")
    print(f" Weather Report Reference Time(local) :  {current_time} \n")
    # Format and set up the data for display in table format
    table = [['Current Temperature', str(temp) + chr(176) + unit],
             ['Feels Like Temperature', str(feels_like) + chr(176) + unit],
             ['Minimum Temperature', str(temp_min) + chr(176) + unit],
             ['maximum Temperature', str(temp_max) + chr(176) + unit],
             ['pressure:', str(pressure) + ' hPa'],
             ['Humidity:', str(humidity) + ' %'],
             ['Current Conditions:', conditions]
             ]

    # Print the output in table format
    print(tabulate(table, tablefmt='fancy_grid'))
# ----------------------------------------------------------------------------------------------------------------------


def forecast_formatted(data, unit):
    """ Formatting of 5 day / 3 hours forecast data """

    # Define the pretty table
    forecast_table = PrettyTable(['Date/Time (Local Time)', 'Temp', 'Min Temp', 'Max Temp', 'Pressure', 'Humidity',
                                  'Clouds', 'Condition'])

    timezone = int(json.dumps(data['city']['timezone']))

    # Read the JSON data and parse the required fields/information for display
    print("_" * 141)
    print_text = "                             Coming 5 days Weather Forecast with every 3 hours Data    " + (" " * 54)
    print(ansi_color('bold', ansi_color('b_green', ansi_color('italic', print_text))))
    for i in range(0, 39):
        data_01 = time.strftime(" %b %d, %Y %I:%M %p ",
                                time.gmtime(int(json.dumps(data['list'][i]['dt'])) + timezone))

        data_02 = "{:.2f}".format(float(json.dumps(data['list'][i]['main']['temp']))) + chr(176) + unit
        data_03 = "{:.2f}".format(float(json.dumps(data['list'][i]['main']['temp_min']))) + chr(176) + unit
        data_04 = "{:.2f}".format(float(json.dumps(data['list'][i]['main']['temp_max']))) + chr(176) + unit
        data_05 = "{:.2f}".format(float(json.dumps(data['list'][i]['main']['pressure']))) + " hpa"
        data_06 = json.dumps(data['list'][i]['main']['humidity']) + " %"
        data_07 = json.dumps(data['list'][i]['clouds']['all']) + " %"
        data_08 = str(json.dumps(data['list'][i]['weather'][0]['description'])).replace('"', '').title()
        forecast_table.add_row([data_01, data_02, data_03, data_04, data_05, data_06, data_07, data_08])
        forecast_table.add_row(["                           ", "           ", "            ", "            ",
                                "            ", "            ", "          ", "                    "])

    print(forecast_table)
# ----------------------------------------------------------------------------------------------------------------------


def ansi_color(style, str_value):
    """ Function to format & style the string as per calling function """

    code = {"italic": 3, "white": 37, "b_black": 40, "b_red": 41, "b_green": 42, "bold": 1,
            "b_yellow": 43, "b_blue": 44, "magenta": 35}

    while True:
        try:
            num = str(code[style])

        except KeyError:
            value = str_value
            return value
        else:
            value = "\033["+num+"m"+str_value+"\033[0m"
            return value
# ----------------------------------------------------------------------------------------------------------------------


def main():
    """Main function to process the Weather current/forecast Program using OpenWeather API"""

    print_text = "                  Welcome to Weather Forecast - The DM Program                    "
    print(ansi_color('bold', ansi_color('b_yellow', print_text)))
    print("--------------------------------------------------------------------------------- ")
    print(ansi_color('italic', welcome_text))
    print("--------------------------------------------------------------------------------- ")

    user_option = input("\n Do you like to use the Weather Forecast Program (Y / N) : ").strip()

    while True:
        try:
            if len(user_option) > 0 and (user_option.upper() == "Y" or user_option.upper() == "YES"):
                error_msg, location, status_code, latitude, longitude = get_lon_lat()
                if status_code == "pass":
                    weather_current_and_forecast(latitude, longitude, location)
            else:
                raise ValueError

        except ValueError:
            if len(user_option) > 0 and (user_option.upper() == "N" or user_option.upper() == "NO"):
                print("\n" * 1)
                print("--------------------------------------------------------------------------------- ")
                print_text = "                      Thank You for your response !!!                            "
                print(ansi_color('b_blue', ansi_color('italic', print_text)))
                print(" Thank You for using my program.                                                   ")
                print(" Please comeback here when you want to use the weather program later...            ")
                print_text = " " * 81
                print(ansi_color('b_blue', ansi_color('italic', print_text)))
                print("--------------------------------------------------------------------------------- ")
                break
            else:
                print("\n Please provide valid response ")
                user_option = input("\n Do you like to use the Weather Forecast Program (Y / N) : ").strip()
                continue
        else:
            # Ask the user if he/she wants to use the application for another location or not
            user_option = input("\n Do you like to use Weather Forecast Program for "
                                "another location (Y / N) : ").strip()
            continue
# ----------------------------------------------------------------------------------------------------------------------


# Execute the main function
if __name__ == "__main__":
    main()
