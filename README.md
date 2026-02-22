# Proyecto Pokémon con Poetry

Este es mi proyecto en Python donde utilizo la [PokéAPI](https://pokeapi.co/) para consultar información de un Pokémon. El programa recibe el nombre de un Pokémon y devuelve sus datos principales: nombre, altura, peso y tipos.

## Requisitos
- Python 3.14
- [Poetry](https://python-poetry.org/) para manejar dependencias

## Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/lorenadreyes01-wq/MANON.git
   cd MANON

2. Instalar las dependencias:
```bash
poetry install
```

# Uso
Para ejecutar el programa:
```bash
poetry run python main.py 
```

El sistema pedirá el nombre de un Pokémon.
Por ejemplo:
```Pikachu```

## Ejemplo de salida

```bash
Información del Pokémon:
Nombre: Pikachu
Altura: 4
Peso: 60
Tipo: electric 
```

## Estructura del proyecto

``` bash 
git MANON/
│
├── src/              # (opcional) tu código organizado en módulos
├── tests/            # (opcional) tus pruebas
├── main.py           # tu script principal
├── pyproject.toml    # configuración de Poetry
├── poetry.lock       # archivo de dependencias (se ignora en git)
├── README.md         # documentación del proyecto
├── .gitignore        # exclusiones de git```


