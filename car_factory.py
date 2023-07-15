from datetime import date

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class CarFacotory:
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Calliope(last_service_date, current_mileage, last_service_mileage)
    
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Glissade(last_service_date, current_mileage, last_service_mileage)
    
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool):
        return Palindrome(last_service_date, warning_light_on)
    
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Rorschach(last_service_date, current_mileage, last_service_mileage)
    
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Thovex(last_service_date, current_mileage, last_service_mileage)