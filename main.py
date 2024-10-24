import requests

# Define the API endpoint
API_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_data(pokemon_name):
    response = requests.get(API_URL + pokemon_name.lower())
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
# Example
if __name__ == "__main__":
    pokemon_name = "pikachu" # Can be any Pokemon name you want
    data = get_pokemon_data(pokemon_name)
    if data:
        print(f"Name: {data['name'].capitalize()}")
        print("Stats: ")
        for stat in data['stats']:
            print(f"- {stat['stat']['name'].capitalize()}: {stat['base_stat']}")
        print(f"Type: {data['types'][0]['type']['name'].capitalize()}")
        print(f"Weight: {data['weight']} hectograms")
    else:
        print(f"Was unable to fine '{pokemon_name}'. Please check again")
   
   
