from pathlib import Path


caminho_pasta = Path(__file__).parent / 'Python é legal'
caminho_pasta.mkdir(exist_ok=True)
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

arquivo = subpasta / 'arquivo.txt'
arquivo.touch()
arquivo.write_text('hey')

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(5):
    file = files / f'file_{i}.txt'

    if file.exists():
        file.unlink()
    else:
        file.touch()
    
    with file.open('a+', encoding='utf8') as text_file:
        text_file.write('Olá mundo\n')
        text_file.write(f'file_{i}.txt')

# apaga a pasta e os arquivos recursivamente
def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR:', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE:', file)
            file.unlink()

    if remove_root:
        root.rmdir()

rmtree(files)
