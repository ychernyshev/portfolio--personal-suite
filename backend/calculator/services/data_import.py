import csv
import io
from calculator.models import DataEntryLineModel


def import_data_logic(file):  # Змінили назву, щоб не плутати, і прибрали self/request
    if not file:
        return {"error": "No file uploaded"}, 400

    try:
        decoded_file = file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        reader = csv.DictReader(io_string)

        created_count = 0
        for row in reader:
            DataEntryLineModel.objects.update_or_create(
                date=row['date'],
                defaults={
                    'power': row.get('power', 600),
                    'morning_data_charge': row.get('morning_charge', 0),
                }
            )
            created_count += 1

        return {"count": created_count}, 201
    except Exception as e:
        return {"error": str(e)}, 400