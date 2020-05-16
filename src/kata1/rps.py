from random import randint

options = ["Piedra", "Papel", "Tijeras"]

def quienGana(player, ai):
    player = player.lower()
    ai = ai.lower()
    
    if player == ai:
        return 'Empate!'
    elif player == "piedra" and ai == "tijeras":
        return "Ganaste!"
    elif player == "papel" and ai == "piedra":
        return "Ganaste!"
    elif player == "tijeras" and ai == "papel":
        return "Ganaste!"

    return "Perdiste!"
        
def Game():
    player = input("¿Piedra, Papel o Tijeras?")
    print("Elegiste: " + player)

    ai = options[randint(0,2)]
    print("AI eligio: " + ai)

    winner = quienGana(player, ai)

    print("Por lo tanto, haz: "  + winner )

