# SPDX-License-Identifier: AGPL-3.0-or-later

import math

from calculator.models import PanelsArrayModel

class PanelPowerCalculationService:
    def calculate_array_production(self, array, radiation_data, calibration_factor):
        efficiency = array.efficiency
        if efficiency > 1.0:
            efficiency = efficiency / 100.0

        array_factor = array.area * efficiency * 0.85 * calibration_factor
        tilt_factor = math.cos(math.radians(abs(array.angle - 30)))

        production = [round(rad * array_factor * tilt_factor, 2) for rad in radiation_data]

        return production
        # return [round(rad * array_factor, 2) for rad in radiation_data]

    def get_total_forecast(self, radiation_data, calibration_factor, user):
        if user:
            arrays = PanelsArrayModel.objects.filter(user=user)
        else:
            arrays = PanelsArrayModel.objects.all()

        total_hourly_wh = [0.0] * len(radiation_data)
        detailed_reports = []

        for array in arrays:
            production = self.calculate_array_production(array, radiation_data, calibration_factor)
            detailed_reports.append({
                "name": array.name,
                "hourly_wh": production,
                "peak_power": max(production) if production else 0
            })
            for i in range(len(total_hourly_wh)):
                total_hourly_wh[i] += production[i]

        return total_hourly_wh, detailed_reports