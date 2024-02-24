import shutil

texto = 'hello'
tamanho = shutil.get_terminal_size().columns - len(texto)

print(f'\033[41m{texto}', end=tamanho*' ')
print(f'\033[m')
