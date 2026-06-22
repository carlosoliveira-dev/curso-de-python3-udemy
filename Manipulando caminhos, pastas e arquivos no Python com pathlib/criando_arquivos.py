from pathlib import Path

caminho_projeto = Path()
caminho_arquivo = Path(__file__)

print(caminho_projeto.absolute())
print(caminho_arquivo)
print(caminho_arquivo.parent)
print(caminho_arquivo.parent.parent)

ideias = caminho_arquivo.parent / 'ideias'
print(ideias)
print(ideias / 'arquivo.txt')
print(Path.home() / 'Desktop' / 'a')
arquivo = caminho_arquivo.parent / 'arquivo.txt'
print(arquivo)

# cria o arquivo no caminho escolhido
arquivo.touch()

arquivo.write_text('Olá mundo!', encoding='utf8')
print(arquivo.read_text(encoding='utf8'))
print()

# apaga o arquivo
arquivo.unlink()

# with abre e fecha o arquivo automaticamente
caminho_arquivo = caminho_arquivo.parent / 'arquivo.txt'
with caminho_arquivo.open('a+') as file:
    file.write('Uma linha \n')
    file.write('Outra linha \n')

