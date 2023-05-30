import qdarkstyle
from price_predictor import PricePredictor
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api="pyside6"))
    window = PricePredictor()
    window.show()
    app.exec()
