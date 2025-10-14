from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings

import pandas as pd
import os

def test_view(request):
    data = {"message": "Hello, your API is working!"}
    return JsonResponse(data)

def csv_table_view(request):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_folder = base_dir  

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
    selected_month = request.GET.get('month', '10')

    # Build CSV file name
    csv_filename = f"{selected_year}-{selected_month}.csv"
    csv_path = os.path.join(data_dir, csv_filename)

    # Read the CSV if it exists
    table_html = "<p class='text-muted'>No data available for this month.</p>"
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        table_html = df.to_html(classes="table table-striped table-bordered", index=False)

    context = {
        "years": years,
        "months": months,
        "selected_year": selected_year,
        "selected_month": selected_month,
        "table_html": table_html,
    }

    return render(request, "dataapi/csv_table.html", context)