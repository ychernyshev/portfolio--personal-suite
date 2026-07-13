import csv
from django.http import HttpResponse
from calculator.models import DataEntryLineModel


def export_data_logic(request):
    entries = DataEntryLineModel.objects.all().order_by('date')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="solar_full_export.csv"'

    writer = csv.writer(response, delimiter=';')

    writer.writerow([
        'date', 'power', 'morning_data_charge', 'morning_data_price',
        'afternoon_data_charge', 'afternoon_data_price', 'evening_data_charge',
        'evening_data_price', 'extra_power', 'full_day_power', 'full_day_cost', 'power_tariff'
    ])

    for entry in entries:
        writer.writerow([
            entry.date,
            entry.power,
            entry.morning_data_charge,
            entry.morning_data_price,
            entry.afternoon_data_charge,
            entry.afternoon_data_price,
            entry.evening_data_charge,
            entry.evening_data_price,
            entry.extra_power,
            entry.full_day_power,
            entry.full_day_cost,
            entry.power_tariff
        ])

    return response