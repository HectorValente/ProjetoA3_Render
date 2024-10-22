from flask import Flask, render_template, request, jsonify
import random
import os

app = Flask(__name__)

# Dicionário de Pokémon
pokemon_dic = {
    25: {"Codigo": 25, "Nome": "Pikachu", "HP": 35, "ATK": 55, "DEF": 40, "SP ATK": 50, "SP DEF": 50, "SPD": 90},
    1: {"Codigo": 1, "Nome": "Bulbasaur", "HP": 45, "ATK": 49, "DEF": 49, "SP ATK": 65, "SP DEF": 65, "SPD": 45},
    4: {"Codigo": 4, "Nome": "Charmander", "HP": 39, "ATK": 52, "DEF": 43, "SP ATK": 60, "SP DEF": 50, "SPD": 65},
    7: {"Codigo": 7, "Nome": "Squirtle", "HP": 44, "ATK": 48, "DEF": 65, "SP ATK": 50, "SP DEF": 64, "SPD": 43}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/battle', methods=['POST'])
def battle():
    data = request.json
    atri_esco = data.get("attribute")
    poke_esco1 = int(data.get("pokemon_code"))

    # Seleciona um Pokémon adversário aleatoriamente
    codigo_pokemons = list(pokemon_dic.keys())
    codigo_pokemons.remove(poke_esco1)
    poke_esco2 = random.choice(codigo_pokemons)

    valor_jogador = pokemon_dic[poke_esco1][atri_esco]
    valor_adversario = pokemon_dic[poke_esco2][atri_esco]

    result = "Empate..."
    if valor_jogador > valor_adversario:
        result = "Você venceu!"
    elif valor_jogador < valor_adversario:
        result = "Você perdeu :("

    response = {
        "player_pokemon": pokemon_dic[poke_esco1],
        "opponent_pokemon": pokemon_dic[poke_esco2],
        "chosen_attribute": atri_esco,
        "player_value": valor_jogador,
        "opponent_value": valor_adversario,
        "result": result
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
