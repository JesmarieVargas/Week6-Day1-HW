# Exploring Web Technologies and Python Programming

# Task 2: Fetching Data from the Pokémon API

import requests
import json

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')

pokemon_info = response.json()

print(f"Pokemon Name:")
print(pokemon_info['name'].title())
print(f"Pokemon Abilities:")
print(pokemon_info['abilities'])

# Task 3: Analyzing and Displaying Data

def fetch_pokemon_data(pokemon_name):
    url = (f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    response = requests.get(url)
    if response.status_code == 200:
        # print(f" Fetch data for {pokemon_name}")
        return response.json()
    else:
        return None

def calculate_average_weight(pokemon_list):
    total_weight = 0
    count = 0
    for pokemon in pokemon_list:
        if pokemon:
            print(f"Pokemon Names:{pokemon_names}")
            total_weight += pokemon['weight']
            count += 1
    if count > 0:
        return total_weight / count
    else:
        return 0

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data = []

for names in pokemon_names:
    data = fetch_pokemon_data(names)
    if data:
        pokemon_data.append(data)

average_weight = calculate_average_weight(pokemon_data)

print(f"Average Weight of Pokemons: {average_weight}")

for pokemon in pokemon_data:
    name = pokemon['name'].title()
    abilities = pokemon['abilities']

    print(f"Name: {name}, Abilities: {abilities}")


