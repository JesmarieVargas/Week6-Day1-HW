# Exploring the Digital Cosmos with Python and the Web

# Task 2: Fetch Data from a Space API

import requests
import json

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue']
            orbit_period = planet['sideralOrbit']
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()

# Task 3: Data Presentation and Analysis

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    data = response.json()['bodies']

    planets = []
    for planet in data:
        if planet['isPlanet']:
            planets.append({
                'name': planet['englishName'],
                'mass': planet['mass']['massValue'] * 10**planet['mass']['massExponent'],
                'orbit_period': planet['sideralOrbit']
                })
    return planets

def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key=lambda planet: planet['mass'])
    return heaviest_planet['name'], heaviest_planet['mass']

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f" The heaviest planet is {name} with a mass of {mass} kg.")