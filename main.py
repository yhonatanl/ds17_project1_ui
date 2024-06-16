import datetime as dt
import pytz
import requests
import tzlocal
from timezonefinder import TimezoneFinder
import wikipedia
import json
import streamlit as st

api_key = 'f513b165eec4b1323ce1b29006f77ffe'

st.header('Project 1 - DS17', divider=True)
st.subheader('by Yehonatan Levi')

with open('settings.json', 'r') as f:
    fav_cities = json.load(f)
    city_name = fav_cities.get("1")
    st_city = city_name
user_option = [city for rank, city in fav_cities.items()]
user_option.append('Type your own city')

st.caption(f"""\n\nThis app will provide weather information for a city of your liking. 
The current default city is {city_name}. However, you can choose another city from my favorites list,
or type a name of another city. \n""")


def show_system_dt():
    # This function shows the date and the system's time and location in a readable format.
    usrtz = tzlocal.get_localzone_name()
    st.caption(f'\nToday is {now.strftime("%A")}, {now.strftime("%B")} {now.strftime("%d")}, {now.strftime("%Y")}')
    if '/' in usrtz:  # This will show the city only, instead of showing the timezone.
        st.caption(f'The Current time is {now.strftime("%H")}:{now.strftime("%M")} in {usrtz.split("/")[-1]}\n')
    else:
        st.caption(f'\nThe Current time is {now.strftime("%H")}:{now.strftime("%M")} in {usrtz}\n')


now = dt.datetime.now()
show_system_dt()


def choose_scale():
    # This function let the user choose between Celsius and Fahrenheit.
    global unit_symbol
    scale = st.radio(
        'Would you prefer to get your weather information in Celsius or Fahrenheit:question:',
        [':globe_with_meridians: Celsius', ':earth_americas: Fahrenheit'],
        index=0,
    )
    if scale == ":globe_with_meridians: Celsius":
        unit_symbol = 'C'
    elif scale == ":earth_americas: Fahrenheit":
        unit_symbol = 'F'


choose_scale()

city_options = st.selectbox('Please choose a City.', user_option, index=0)

if city_options == 'Type your own city':
    your_input = st.text_input('please type the city name')
    city_name = your_input
else:
    city_name = city_options

deploy_weather = st.button('Get Weather info')


def get_city_info():
    # This function gets the information needed to provide the weather for the selected city.
    if deploy_weather:

        geocoder = requests.get(
            f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}')
        latitude = geocoder.json()[0]['lat']
        longitide = geocoder.json()[0]['lon']
        tf = TimezoneFinder()
        tz_lat_lon = tf.timezone_at(lat=latitude, lng=longitide)
        pytz_timezone = pytz.timezone(tz_lat_lon)
        weatherinfo = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitide}&appid={api_key}&units=metric'
        )
        if unit_symbol == 'F':
            fweatherinfo = (weatherinfo.json()["main"]["temp"] * 9 / 5) + 33.8
            fweatherinfofeelslike = (weatherinfo.json()["main"]["feels_like"]* 9 / 5) + 33.8
            st.write(f'\nThe temperature in {city_name}: right now is {fweatherinfo:.2f}°{unit_symbol}, '
                     f'and it feels like {fweatherinfofeelslike:.2f}°{unit_symbol}')
            st.write(f'\nHumidity Level: {weatherinfo.json()["main"]["humidity"]}%')
            st.write(f'\nCurrent time in {city_name} is {dt.datetime.now(pytz_timezone).strftime("%H:%M")}')
        else:
            st.write(
                f'\nThe temperature in {city_name}: right now is {weatherinfo.json()["main"]["temp"]}°{unit_symbol}, '
                f'and it feels like {weatherinfo.json()["main"]["feels_like"]}°{unit_symbol}')
            st.write(f'\nHumidity Level: {weatherinfo.json()["main"]["humidity"]}%')
            st.write(f'\nCurrent time in {city_name} is {dt.datetime.now(pytz_timezone).strftime("%H:%M")}')


get_city_info()


def did_u_know(city_name):
    # This Function provide a short summary of the city's page in Wikipedia.
    try:
        entry = wikipedia.page(city_name)
        return entry.summary.split('. ')[0]
    except wikipedia.PageError:
        return f"Sorry, there is no Wikipedia page for {city_name}."
    except Exception as e:
        return f"An error occurred: {e}"
        # The exception in this function meant to deal with typical errors from wikipedia's api.


st.caption(f'\nAbout {city_name}:\n{did_u_know(city_name)}.')


def update_favorite_city():
    # This function will update the first entry in the list of favorite cities. it will only run if the user will click on the "Update" button.
    with open('settings.json', 'r+') as f:
        fav_cities = json.load(f)
        if city_name == fav_cities.get("1"):
            st.write(f'{city_name} is already the default city.')
        else:
            fav_cities["1"] = city_name
            f.seek(0)
            json.dump(fav_cities, f, indent=4)
            f.truncate()
            st.write(f'{city_name}is now the default city.')


update_button = st.button('Update default city')
if update_button:
    update_favorite_city()

rerun = st.button('Restart the app')
if rerun:
    st.rerun()
