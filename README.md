# Modelado de la Base de Datos de la PokeAPI

## 📌 Introducción
Este proyecto implementa un modelo de base de datos inspirado en la [PokeAPI](https://pokeapi.co/), estructurando la información de los Pokémon, sus habilidades, movimientos, tipos, formas y versiones en un modelo relacional utilizando **SQLAlchemy ORM** en Python.

El objetivo principal es representar de manera eficiente las relaciones entre las entidades de la PokeAPI, asegurando que la base de datos sea escalable y optimizada para consultas rápidas.

## 📊 Diagrama de Base de Datos
El modelo de base de datos se ha construido siguiendo un diagrama entidad-relación que organiza la información en las siguientes tablas:

### 🔹 **Tablas principales**
1. **`Pokemon`**: Contiene la información básica de cada Pokémon.
2. **`Ability`**: Lista de habilidades disponibles en el juego.
3. **`Move`**: Lista de movimientos que pueden aprender los Pokémon.
4. **`Type`**: Lista de tipos de Pokémon (Agua, Fuego, Planta, etc.).
5. **`Form`**: Diferentes formas en las que puede aparecer un Pokémon.
6. **`Version`**: Versiones de los juegos donde aparecen los Pokémon.

### 🔹 **Tablas intermedias**
Estas tablas establecen las relaciones entre los elementos anteriores:
1. **`PokemonAbility`**: Relaciona los Pokémon con sus habilidades.
2. **`PokemonMove`**: Relaciona los Pokémon con los movimientos que pueden aprender.
3. **`PokemonType`**: Relaciona los Pokémon con sus tipos.
4. **`PokemonForm`**: Relaciona los Pokémon con sus distintas formas.

## 💻 Instalación
Para ejecutar este proyecto, sigue estos pasos:

1. Clona este repositorio:
   ```bash
   git clone https://github.com/JulioRom/exercise-pokeapi-data-modeling
   cd exercise-pokeapi-data-modeling
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows usa: env\Scripts\activate
   pip install -r requirements.txt
   ```

3. Genera la base de datos y el diagrama ejecutando:
   ```bash
   python src/models.py
   ```

4. Verifica que se haya generado el archivo `diagram.png` con el modelo de datos.

## 🏗️ Modelado de la Base de Datos
A continuación, se explican las entidades clave y sus relaciones:

### 1️⃣ **Pokemon**
- `pokemon_id`: Identificador único.
- `name`: Nombre del Pokémon.
- `base_experience`: Puntos de experiencia base.
- `height`: Altura en decímetros.
- `is_default`: Indica si es la forma principal.
- `game_index`: Índice en los juegos.
- `version_id`: Clave foránea a `Version`.

### 2️⃣ **Ability**
- `ability_id`: Identificador único.
- `name`: Nombre de la habilidad.
- `url`: URL de referencia.

### 3️⃣ **Move**
- `move_id`: Identificador único.
- `name`: Nombre del movimiento.
- `url`: URL de referencia.

### 4️⃣ **Type**
- `type_id`: Identificador único.
- `name`: Nombre del tipo (ej. Agua, Fuego).
- `url`: URL de referencia.

### 5️⃣ **Version**
- `version_id`: Identificador único.
- `name`: Nombre de la versión del juego.
- `url`: URL de referencia.
- `version_group`: Grupo de versiones.

### 6️⃣ **Tablas intermedias**
Estas tablas permiten relaciones **muchos a muchos**:
- **`PokemonAbility`**: Relaciona los Pokémon con habilidades.
- **`PokemonMove`**: Relaciona los Pokémon con movimientos.
- **`PokemonType`**: Relaciona los Pokémon con tipos.
- **`PokemonForm`**: Relaciona los Pokémon con sus formas.

## 🏆 Características del Proyecto
✅ Modelado de datos basado en la PokeAPI.<br>
✅ Uso de **SQLAlchemy ORM** para la manipulación de datos.<br>
✅ Generación de diagrama automática con `eralchemy2`.<br>
✅ Relación entre entidades optimizada.<br>
✅ Base de datos escalable y optimizada para consultas rápidas.<br>

## 🛠️ Herramientas y Tecnologías
- **Python 3**
- **SQLAlchemy ORM**
- **PostgreSQL o SQLite** (según configuración)
- **Eralchemy2** (para generar diagramas)

## 📜 Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

## 📢 Contribuciones
Si deseas contribuir a este proyecto, por favor abre un _issue_ o envía un _pull request_ con tus mejoras.

---

Con esta estructura, el modelo de datos está listo para integrarse con cualquier aplicación basada en la PokeAPI. 🎮🔥

## 👨‍💻 **Autor**

- **Desarrollado por JulioRom**
- 📧 **Correo:** [julioandrescampos@gmail.com](mailto:julioandrescampos@gmail.com)
- 🔗 **GitHub:** [https://github.com/JulioRom](https://github.com/JulioRom)