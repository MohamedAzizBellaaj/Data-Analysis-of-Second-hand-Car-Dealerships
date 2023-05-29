import json

import pandas as pd
import xgboost as xgb
from price_predictor_ui import Ui_PricePredictor
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QMainWindow
from sklearn.preprocessing import OneHotEncoder


class PricePredictor(QMainWindow, Ui_PricePredictor):
    def __init__(self):
        super().__init__()
        self.setup()
        self.brand_combo_box.activated.connect(self.handle_combo_box_activated)
        self.estimate_price_button.clicked.connect(
            self.handle_estimate_price_button_clicked
        )

    def setup(self):
        self.setupUi(self)
        double_validator = QDoubleValidator()

        self.mileage_line_edit.setValidator(double_validator)
        self.year_line_edit.setValidator(double_validator)
        self.power_line_edit.setValidator(double_validator)
        self.engine_size_line_edit.setValidator(double_validator)

        with open("../Values/brand_models.json", "r") as f:
            brand_models = json.load(f)
            for brand in brand_models.keys():
                self.brand_combo_box.addItem(brand)

        with open("../Values/location.json", "r") as f:
            locations = json.load(f)
            for location in locations:
                self.location_combo_box.addItem(location)

        with open("../Values/body_type.json", "r") as f:
            body_types = json.load(f)
            for body_type in body_types:
                self.body_type_combo_box.addItem(body_type)

        with open("../Values/fuel.json", "r") as f:
            fuels = json.load(f)
            for fuel in fuels:
                self.fuel_combo_box.addItem(fuel)

        with open("../Values/transmission.json", "r") as f:
            transmissions = json.load(f)
            for transmission in transmissions:
                self.transmission_combo_box.addItem(transmission)

        with open("../Values/color.json", "r") as f:
            colors = json.load(f)
            for color in colors:
                self.color_combo_box.addItem(color)

    def handle_combo_box_activated(self):
        brand = self.brand_combo_box.currentText()
        with open("../Values/brand_models.json", "r") as f:
            brand_models = json.load(f)
            models = brand_models[brand]
            self.model_combo_box.clear()
            for model in models:
                self.model_combo_box.addItem(model)

    def handle_estimate_price_button_clicked(self):
        new_data = self.get_data()

        test = xgb.DMatrix(new_data)

        model = xgb.Booster()

        model.load_model("../Machine Learning/model.xgb")
        

        prediction = model.predict(test)[0]

        rounded_prediction = round(prediction / 100) * 100

        self.estimated_price_view.display(rounded_prediction)

    def get_data(self):
        brand = self.brand_combo_box.currentText()
        model = self.model_combo_box.currentText()
        mileage = float(self.mileage_line_edit.text())
        year = float(self.year_line_edit.text())
        power = float(self.power_line_edit.text())
        engine_size = float(self.engine_size_line_edit.text())
        location = self.location_combo_box.currentText()
        body_type = self.body_type_combo_box.currentText()
        fuel = self.fuel_combo_box.currentText()
        transmission = self.transmission_combo_box.currentText()
        color = self.color_combo_box.currentText()

        data = {
            "brand": brand,
            "model": model,
            "mileage": mileage,
            "year": year,
            "power": power,
            "engine_size": engine_size,
            "location": location,
            "body_type": body_type,
            "fuel": fuel,
            "transmission": transmission,
            "color": color,
        }

        df = pd.DataFrame(data, index=[0])

        new_data = pd.get_dummies(df)
        
        return new_data