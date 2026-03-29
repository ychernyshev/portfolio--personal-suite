import io
import pandas as pd
from django.http import HttpResponse
from calculator.models import DataEntryLineModel


def data_export(request):
    data_entries = DataEntryLineModel.objects.all().values()
    entries = pd.DataFrame(data_entries)

    output = io.BytesIO()

    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        entries.to_excel(writer, sheet_name='Power_Generation', index=False)

    output.seek(0)

    response = HttpResponse(
        output.read(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="solar_report.xlsx"'

    return response