from datetime import timedelta
from battery.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self,  last_service_date, current_date):
        last_service_date = last_service_date
        current_date = current_date

    def needs_service(self):
        service_interval = timedelta(days=365 * 2)  # Service interval of 2 years
        time_difference = self.current_date - self.last_service_date

        if time_difference >= service_interval:
            return True
        else:
            return False