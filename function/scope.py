champion = 'Lux'

def show_global_champion():
    print(f'show_global_champion: {champion}')
    print('show_global_champion: {}'.format(champion))

def change_global_champion():
    print('before change_global_champion: {}'.format(champion))
    champion = 'Ahri'
    print('after change_global_champion: {}'.format(champion))

show_global_champion()
change_global_champion()
