import requests

def buscar_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        nombre = data["name"].capitalize()
        altura = data["height"]
        peso = data["weight"]
        tipos = [tipo["type"]["name"] for tipo in data["types"]]

        print("\nInformación del Pokémon:")
        print("Nombre:", nombre)
        print("Altura:", altura)
        print("Peso:", peso)
        print("Tipo(s):", ", ".join(tipos))
    else:
        print("No se encontró el Pokémon.")

if __name__ == "__main__":
    pokemon = input("Ingresa el nombre del Pokémon: ")
    buscar_pokemon(pokemon)
