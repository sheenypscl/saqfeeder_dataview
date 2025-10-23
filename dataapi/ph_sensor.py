# dataapi/ph_sensor.py
import time
import random  # remove this once you read real data

# replace with python code for calibration reading
class PHCalibrator:
    def __init__(self):
        self.acid_voltage = None

    def calibrate_acid(self):
        time.sleep(2)  # simulate delay while measuring
        temp_acid = 25.3  # replace with real temp read
        self.acid_voltage = random.uniform(1700, 1800)  # simulate sensor mV

        return f"Acid Calibration Complete: {self.acid_voltage:.3f} mV at {temp_acid:.3f} °C"

# replace with python code for calibration reading
class DOCalibrator: 
    def __init__(self):
        self.do_voltage = None

    def calibrate_do(self):
        time.sleep(1)  # simulate delay while measuring
        self.temp_sensor = 22.5
        voltage_mv = random.uniform(800, 900)  # simulate sensor mV
        do_mg_per_L = 1500.0  # simulate DO mg/L

        return f"Temp: {self.temp_sensor:.2f} °C | Voltage: {voltage_mv:.2f} mV | DO: {do_mg_per_L:.2f} mg/L"
        

TEMP_COEFF = 0.019  # Temperature coefficient (typical value for EC)
class ECCalibrator:
    def __init__(self):
        self.ec_voltage = None

    def calibrate_ec(self):
        time.sleep(1)  # simulate delay while measuring
        self.temp_sensor = 24.0
        voltage_mv = random.uniform(200, 300)  # simulate sensor mV
        ec_value = 2.5  # simulate EC value in mS/cm

        return f"Temp: {self.temp_sensor:.2f} °C | Voltage: {voltage_mv:.2f} mV | EC: {ec_value:.2f} mS/cm"
