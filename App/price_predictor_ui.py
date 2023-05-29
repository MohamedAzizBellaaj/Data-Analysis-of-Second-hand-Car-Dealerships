# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'price_predictor.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLCDNumber,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_PricePredictor(object):
    def setupUi(self, PricePredictor):
        if not PricePredictor.objectName():
            PricePredictor.setObjectName(u"PricePredictor")
        PricePredictor.resize(832, 611)
        self.centralwidget = QWidget(PricePredictor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_11.addWidget(self.label)

        self.mileage_line_edit = QLineEdit(self.centralwidget)
        self.mileage_line_edit.setObjectName(u"mileage_line_edit")

        self.horizontalLayout_11.addWidget(self.mileage_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_10.addWidget(self.label_2)

        self.year_line_edit = QLineEdit(self.centralwidget)
        self.year_line_edit.setObjectName(u"year_line_edit")

        self.horizontalLayout_10.addWidget(self.year_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_9.addWidget(self.label_3)

        self.power_line_edit = QLineEdit(self.centralwidget)
        self.power_line_edit.setObjectName(u"power_line_edit")

        self.horizontalLayout_9.addWidget(self.power_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.engine_size_line_edit = QLineEdit(self.centralwidget)
        self.engine_size_line_edit.setObjectName(u"engine_size_line_edit")

        self.horizontalLayout_8.addWidget(self.engine_size_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_12.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.brand_combo_box = QComboBox(self.centralwidget)
        self.brand_combo_box.setObjectName(u"brand_combo_box")

        self.horizontalLayout_7.addWidget(self.brand_combo_box)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.model_combo_box = QComboBox(self.centralwidget)
        self.model_combo_box.setObjectName(u"model_combo_box")

        self.horizontalLayout_6.addWidget(self.model_combo_box)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.location_combo_box = QComboBox(self.centralwidget)
        self.location_combo_box.setObjectName(u"location_combo_box")

        self.horizontalLayout_5.addWidget(self.location_combo_box)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.body_type_combo_box = QComboBox(self.centralwidget)
        self.body_type_combo_box.setObjectName(u"body_type_combo_box")

        self.horizontalLayout_4.addWidget(self.body_type_combo_box)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_3.addWidget(self.label_9)

        self.fuel_combo_box = QComboBox(self.centralwidget)
        self.fuel_combo_box.setObjectName(u"fuel_combo_box")

        self.horizontalLayout_3.addWidget(self.fuel_combo_box)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.transmission_combo_box = QComboBox(self.centralwidget)
        self.transmission_combo_box.setObjectName(u"transmission_combo_box")

        self.horizontalLayout_2.addWidget(self.transmission_combo_box)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout.addWidget(self.label_11)

        self.color_combo_box = QComboBox(self.centralwidget)
        self.color_combo_box.setObjectName(u"color_combo_box")

        self.horizontalLayout.addWidget(self.color_combo_box)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_12.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.estimate_price_button = QPushButton(self.centralwidget)
        self.estimate_price_button.setObjectName(u"estimate_price_button")

        self.horizontalLayout_13.addWidget(self.estimate_price_button)

        self.estimated_price_view = QLCDNumber(self.centralwidget)
        self.estimated_price_view.setObjectName(u"estimated_price_view")

        self.horizontalLayout_13.addWidget(self.estimated_price_view)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        PricePredictor.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PricePredictor)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 832, 22))
        PricePredictor.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PricePredictor)
        self.statusbar.setObjectName(u"statusbar")
        PricePredictor.setStatusBar(self.statusbar)

        self.retranslateUi(PricePredictor)

        QMetaObject.connectSlotsByName(PricePredictor)
    # setupUi

    def retranslateUi(self, PricePredictor):
        PricePredictor.setWindowTitle(QCoreApplication.translate("PricePredictor", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("PricePredictor", u"Mileage", None))
        self.label_2.setText(QCoreApplication.translate("PricePredictor", u"Year", None))
        self.label_3.setText(QCoreApplication.translate("PricePredictor", u"Power", None))
        self.label_4.setText(QCoreApplication.translate("PricePredictor", u"Engine Size", None))
        self.label_5.setText(QCoreApplication.translate("PricePredictor", u"Brand", None))
        self.label_6.setText(QCoreApplication.translate("PricePredictor", u"Model", None))
        self.label_7.setText(QCoreApplication.translate("PricePredictor", u"Location", None))
        self.label_8.setText(QCoreApplication.translate("PricePredictor", u"Body Type", None))
        self.label_9.setText(QCoreApplication.translate("PricePredictor", u"Fuel", None))
        self.label_10.setText(QCoreApplication.translate("PricePredictor", u"Transmission", None))
        self.label_11.setText(QCoreApplication.translate("PricePredictor", u"Color", None))
        self.estimate_price_button.setText(QCoreApplication.translate("PricePredictor", u"Estimate", None))
    # retranslateUi

