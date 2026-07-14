'''
python -m venv venv
source venv/Scripts/Activate
pip install pyside6
pip install qdarkstyle
pip install pyinstaller
pip install pillow
clear ; python main.py

Pyinstaller no Windows 11 usando Git Bash:
pyinstaller --name="Calculadora" --noconfirm --noconsole --onefile --add-data="../files/:files" --icon="../files/icon.png" --clean --log-level=WARN --distpath="output/dist" --workpath="output/build" --specpath="output" main.py
'''
import sys

from buttons import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
