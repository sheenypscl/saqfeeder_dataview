from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from .ph_sensor import PHCalibrator, DOCalibrator, ECCalibrator
# from gpiozero import OutputDevice

import pandas as pd
import os, io, sys

def test_view(request):
    data = {"message": "Hello, your API is working!"}
    return JsonResponse(data)

def csv_table_view(request):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # data_folder = base_dir  

    data_dir = os.path.join(settings.BASE_DIR, 'data')

    # Static list of years
    years = ['2025', '2026', '2027', '2028', '2029']
    months = [
    ('01', 'January'),
    ('02', 'February'),
    ('03', 'March'),
    ('04', 'April'),
    ('05', 'May'),
    ('06', 'June'),
    ('07', 'July'),
    ('08', 'August'),
    ('09', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
]

    # Get selected year and month from URL query
    selected_year = request.GET.get('year', '2025')
    selected_month = request.GET.get('month', '01')

    # Build CSV file name
    csv_filename = f"{selected_year}-{selected_month}.csv"
    csv_path = os.path.join(settings.CSV_DIR, csv_filename)

    # Read the CSV if it exists
    table_html = "<p class='text-muted'>No data available for this month.</p>"
    
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)

        if "SensorID" in df.columns:
            df = df.sort_values(by="SensorID", ascending=False)

        # Add "View Image" button column
        df["Image"] = df["SensorID"].apply(
            lambda sid: (
                f"<button type='button' class='btn btn-link p-0 view-image-btn' "
                f"data-toggle='modal' data-target='#imageModal' data-sensorid='{sid}'"
                f"data-image='/static/dataapi/images/{sid}.JPG'>"
                f"View image</button>"
            )
        )

        table_html = df.to_html(
            classes="table table-striped table-bordered text-center align-middle", 
            index=False, 
            escape=False,
            table_id="data-table"
            )
        
        # table_html = table_html.replace('<table ', '<table id="data-table" ')

    context = {
        "years": years,
        "months": months,
        "selected_year": selected_year,
        "selected_month": selected_month,
        "table_html": table_html,
    }

    return render(request, "dataapi/csv_table.html", context)



def run_calibration(calibrator_class):
    buffer = io.StringIO()
    sys_stdout = sys.stdout
    sys.stdout = buffer

    try:
        calibrator = calibrator_class()
        calibrator.main()
    except Exception as e:
        sys.stdout = sys_stdout
        return JsonResponse({"error": str(e)})
    finally:
        sys.stdout = sys_stdout

    output = buffer.getvalue()
    return JsonResponse({"result": output})


def calibration_acid_view(request):
    return run_calibration(PHCalibrator)


def calibration_do_view(request):
    return run_calibration(DOCalibrator)


def calibration_ec_view(request):
    return run_calibration(ECCalibrator)



#for pH value GPIO 17
# pin17 = OutputDevice(17)
# def ph_calib(request):
#     state = request.GET.get("state")
#     if state == "on":
#         pin17.on()
#     elif state == "off":
#         pin17.off()

#     return JsonResponse({"pin": 17, "state": state})

def calibration_page(request):
    return render(request, "dataapi/calibration.html")

# # ph sensor
# def calibrate_acid_view(request):
#     calibrator = PHCalibrator()
#     result = calibrator.calibrate_acid()
#     return JsonResponse({"message": result})

# # DO sensor
# def calibrate_do_view(request):
#     calibrator = DOCalibrator()
#     result = calibrator.calibrate_do()
#     return JsonResponse({"message": result})

# # EC sensor
# def calibrate_ec_view(request):
#     calibrator = ECCalibrator()
#     result = calibrator.calibrate_ec()
#     return JsonResponse({"message": result})
