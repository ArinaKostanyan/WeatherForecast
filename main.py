from get_weather_info import get_info


def get_location_data():
    city = input('Please, enter a city name if you know or skip: ')
    zip_code = input('Please, enter a zip code if you know or skip: ')

    if not (city or zip_code):
        print('Not a valid data provided.', '\n')

    return city if city else zip_code

if __name__ == '__main__':
    loc_value = None
    while not loc_value:
        loc_value = get_location_data()
    temperature_type = input('Please, choose temperature unit (Celsius or Fahrenheit): ')
    get_info(loc_value, temperature_type)