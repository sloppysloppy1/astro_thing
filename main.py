import requests as req
import sqlite3
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from tzwhere import tzwhere
import re


from natalchart import NatalChart

try:
    sqlite_conn = sqlite3.connect('people.db')
    cursor = sqlite_conn.cursor()
except sqlite3.Error as error:
    print("бля", error)

def send_reqs(birth_data):
    def get_coordinates(place):
        cords = geolocator.geocode(place)
        lt, ln = cords[1][0], cords[1][1]
        w = tzwhere.tzwhere()
        tz_city, tz_country = w.tzNameAt(cords[1][0], cords[1][1]).split('/')

        return lt, ln, tz_city, tz_country

    geolocator = Nominatim(user_agent="app")

    lt, ln, tz_city, tz_country = get_coordinates(birth_data['city'] + ', ' + birth_data['country'])
    print("got lat, ln: ", lt, ln, tz_city, tz_country)

    parse_url = """https://geocult.ru/natalnaya-karta-onlayn-raschet?
    fn=&fd={}&fm={}&fy={}&fh={}&fmn={}&c1={}%2C+{}&ttz=20
    &tz={}%2F{}&tm=12&lt={}&ln={}&hs=W&sb=1""".format(
        birth_data['day'],
        birth_data['month'],
        birth_data['year'],
        birth_data['hour'],
        birth_data['mins'],
        birth_data['city'],
        birth_data['country'],
        tz_city,
        tz_country,
        lt, ln,
    )

    r = req.get(parse_url)

    soup = BeautifulSoup(r.text, 'html5lib')

    centers = soup.find_all('center')

    placements = centers[1].find('table').find_all('tr')
    placements.pop(0), placements.pop(-1) # удаляем мусор

    list_of_placements = []
    for _placement in placements:
        placement, retrograde = {}, False
        __placement = _placement.findAll('td')

        name = __placement[0].text.split()[1]
        house =  __placement[2].text.replace(u'\xa0', '').strip()

        sign_n_degree = __placement[1].text.split()
        sign, degrees = sign_n_degree[1], re.findall(r'\d+', sign_n_degree[2])
        if 'R' in sign_n_degree:
            retrograde = True

        placement['name'], placement['house'] = name, house
        placement['sign'], placement['degrees'] = sign, degrees
        placement['retro'] = retrograde

        print(placement)

        list_of_placements.append(placement)

    houses = centers[3].find('table').find_all('tr')
    houses.pop(0), houses.pop(-1) # удаляем мусор

    list_of_houses = []
    for _house in houses:
        house = {}
        __house = _house.findAll('td')

        sign_n_degree = __house[1].text.split()
        sign, degrees = sign_n_degree[1], re.findall(r'\d+', sign_n_degree[2])

        house['sign'], house['degrees'] = sign, degrees

        print(house)

        list_of_houses.append(house)

    aspects = centers[5].find('table').find_all('tr')
    aspects.pop(0), aspects.pop(-1) # удаляем мусор

    list_of_aspects = []
    for _aspect in aspects:
        aspect = {}
        __aspect = _aspect.findAll('td')




birth_data = {
    'day': 3,
    'month': 9,
    'year': 2009,
    'hour': 10,
    'mins': 25,
    'city': 'Novosibirsk',
    'country': 'Russia',
}

send_reqs(birth_data)
