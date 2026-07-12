''' PyPDF2 para manipular arquivos PDF (PdfMerger) '''

from pathlib import Path

from PyPDF2 import PdfMerger, PdfReader

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20230210.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

page0 = reader.pages[0]
imagem0 = page0.images[0]

files = [
    PASTA_NOVA / 'page1.pdf',
    PASTA_NOVA / 'page2.pdf',

]

merger = PdfMerger()
for file in files:
    merger.append(file)

merger.write(PASTA_NOVA / 'MERGED.pdf')
merger.close()
