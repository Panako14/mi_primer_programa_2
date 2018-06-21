pokemon_elegido = input('Elige un enemigo (Bulbasaur / Charmander / Squirtle): ')

vida_pikachu = 100
vida_enemigo = 0
ataque_enemigo = 0

if pokemon_elegido == 'Bulbasaur':
    vida_enemigo = 100
    ataque_enemigo = 25

elif pokemon_elegido == 'Charmander':
    vida_enemigo = 80
    ataque_enemigo = 40

elif pokemon_elegido == 'Squirtle':
    vida_enemigo = 90
    ataque_enemigo = 30


while vida_enemigo > 0 and vida_pikachu > 0:

    ataque_pikachu = input('Elige un ataque( Chispazo / Rayo ): ')
    daño = 0
    if ataque_pikachu == 'Chispazo':
        daño = 30
        vida_enemigo -= daño

    elif ataque_pikachu == 'Rayo':
        daño = 40
        vida_enemigo -= daño

    print('Pikachu usa {} y causa un daño de {}, la vida de {} es de {}.'.format(ataque_pikachu, daño, pokemon_elegido, vida_enemigo))
    vida_pikachu -= ataque_enemigo
    print('{} usa ataque y causa un daño de {}, la vida de Pikachu es de {}'.format(pokemon_elegido, ataque_enemigo, vida_pikachu))

if vida_pikachu <= 0:
        print('¡Has perdido!')
if vida_enemigo <= 0:
        print('!Has ganado¡')

print('El combate ha terminado.')


