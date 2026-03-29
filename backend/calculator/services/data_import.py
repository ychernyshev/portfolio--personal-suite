import csv
import io
from rest_framework.decorators import action
from rest_framework.response import Response
from calculator.models import DataEntryLineModel

# У твій EntryViewSet додай:
@action(detail=False, methods=['post'], url_path='import-csv')
def data_import(self, request):
    file = request.FILES.get('file')
    if not file:
        return Response({"error": "No file uploaded"}, status=400)

    decoded_file = file.read().decode('utf-8')
    io_string = io.StringIO(decoded_file)
    reader = csv.DictReader(io_string)

    created_count = 0
    for row in reader:
        # row — це словник, де ключі це назви колонок у CSV
        DataEntryLineModel.objects.update_or_create(
            date=row['date'],
            defaults={
                'power': row.get('power', 600),
                'morning_data_charge': row.get('morning_charge', 0),
                # додавай інші поля згідно зі своєю моделлю
            }
        )
        created_count += 1

    return Response({"status": f"Successfully imported {created_count} entries"})