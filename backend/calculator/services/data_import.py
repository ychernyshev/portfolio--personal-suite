import csv
import io
from django.db import transaction
from calculator.models import DataEntryLineModel


def import_data_logic(file):
    if not file:
        return {"error": "No file uploaded"}, 400

    try:
        decoded_file = file.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(decoded_file), delimiter=';')

        entries_to_create = []

        with transaction.atomic():
            for row in reader:
                DataEntryLineModel.objects.update_or_create(
                    date=row['date'],
                    defaults={
                        'power': row['power'],
                        'morning_data_charge': row['morning_data_charge'],
                        'morning_data_price': row['morning_data_price'],
                        'afternoon_data_charge': row['afternoon_data_charge'],
                        'afternoon_data_price': row['afternoon_data_price'],
                        'evening_data_charge': row['evening_data_charge'],
                        'evening_data_price': row['evening_data_price'],
                        'extra_power': row['extra_power'],
                        'full_day_power': row['full_day_power'],
                        'full_day_cost': row['full_day_cost'],
                        'power_tariff': row['power_tariff'],
                    }
                )

        return {"status": "success"}, 201

    except Exception as e:
        return {"error": f"Помилка парсингу: {str(e)}"}, 400