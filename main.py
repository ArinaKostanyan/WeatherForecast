from get_weather_info import get_weather_table


def get_location_data():
    city = input('Please, enter a city name if you know or skip: ')
    zip_code = input('Please, enter a zip code if you know or skip: ')

    if not (city or zip_code):
        print('Not a valid data provided.')
        print('Please try once more', '\n')

    return city if city else zip_code

if __name__ == '__main__':
    loc_value = None
    while not loc_value:
        loc_value = get_location_data()
    get_weather_table(loc_value)