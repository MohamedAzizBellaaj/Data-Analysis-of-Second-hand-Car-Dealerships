import sys

# import qdarkstyle
from PySide6.QtWidgets import QApplication
from price_predictor import PricePredictor

if __name__ == "__main__":
    app = QApplication([])
    # app.setStyleSheet()
    window = PricePredictor()
    window.show()
    app.exec()
