from get_weather_info import get_weather_table

def get_location_data():
    attempts = 0
    while attempts < 5:
        city = input('Please, enter a city name if you know or skip: ')
        zip_code = input('Please, enter a zip code if you know or skip: ')

        if city or zip_code:
            return city if city else zip_code
        else:
            attempts += 1
            print(f'Not a valid input provided. {5 - attempts} attempts left. \n')
    
    print('Maximum attempts reached. Exiting the program.')
    return None

if __name__ == '__main__':
    loc_value = get_location_data()
    if loc_value:
        get_weather_table(loc_value)
    else:
        print('No location provided, terminating the weather retrieval process.')
