from django.core.management.base import BaseCommand
from dashboard.models import Sector

class Command(BaseCommand):
    help = 'Populate the Sector table with predefined choices'

    def get_english_sectors(self):
        return [
            ('lawn_care', 'Lawn Care'),
            ('disinfestations', 'Disinfestations'),
            ('swimming_pools', 'Company specializing in swimming pools'),
            ('electrician', 'Electrician'),
            ('carpentry', 'Carpentry'),
            ('foundation', 'Foundation'),
            ('roofing', 'Roof installation and repair'),
            ('home_inspection', 'Home inspection'),
            ('plumbing', 'Plumbing work'),
            ('landscaping', 'Landscaping'),
            ('floors', 'Floors'),
            ('garage_doors', 'Garage Doors'),
            ('window_cleaning', 'Window Cleaning'),
            ('carpet_cleaning', 'Carpet cleaning'),
            ('pool_cleaning', 'Swimming pool cleaning'),
            ('house_cleaning', 'House cleaning'),
            ('fences', 'Fences'),
            ('appliance_repairs', 'Household appliance repairs'),
            ('hvac', 'Heating and Air Conditioning'),
            ('coatings', 'Coatings'),
            ('worktop_installation', 'Worktop installation services'),
            ('snow_removal', 'Snow removal services'),
            ('tree_services', 'Tree Services'),
            ('water_damage', 'Water damage services'),
            ('window_services', 'Window services'),
            ('procurement', 'Procurement service'),
            ('waste_disposal', 'Waste disposal'),
            ('removals', 'Removals'),
            ('handyman', 'Handyman'),
        ]
    
    def get_italian_sectors(self):
        return [
            ('cura_prato', 'Cura del prato'),
            ('disinfestazioni', 'Disinfestazioni'),
            ('piscine', 'Azienda specializzata in piscine'),
            ('elettricista', 'Elettricista'),
            ('carpenteria', 'Carpenteria'),
            ('fondamenta', 'Fondamenta'),
            ('coperture', 'Installazione e riparazione tetti'),
            ('ispezione_casa', 'Ispezione della casa'),
            ('idraulica', 'Lavori di idraulica'),
            ('paesaggistica', 'Paesaggistica'),
            ('pavimenti', 'Pavimenti'),
            ('porte_garage', 'Porte del garage'),
            ('pulizia_finestre', 'Pulizia finestre'),
            ('pulizia_tappeti', 'Pulizia tappeti'),
            ('pulizia_piscine', 'Pulizia piscine'),
            ('pulizia_casa', 'Pulizia casa'),
            ('recinzioni', 'Recinzioni'),
            ('riparazione_elettrodomestici', 'Riparazioni elettrodomestici'),
            ('riscaldamento_condizionamento', 'Riscaldamento e aria condizionata'),
            ('rivestimenti', 'Rivestimenti'),
            ('installazione_piani', 'Servizi di installazione piani di lavoro'),
            ('rimozione_neve', 'Servizi di rimozione neve'),
            ('servizi_alberi', 'Servizi per alberi'),
            ('danni_acqua', 'Servizi per danni causati dall\'acqua'),
            ('servizi_finestre', 'Servizi per finestre'),
            ('approvvigionamento', 'Servizi di approvvigionamento'),
            ('smaltimento_rifiuti', 'Smaltimento rifiuti'),
            ('traslochi', 'Traslochi'),
            ('tuttofare', 'Tuttofare')
        ]
    
    def handle(self, *args, **kwargs):
        sectors = self.get_italian_sectors()

        for key, name in sectors:
            Sector.objects.get_or_create(name=key)
            self.stdout.write(f"Added sector: {name}")
