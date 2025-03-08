from django.core.management.base import BaseCommand, CommandError
from django.core.management import get_commands, load_command_class

from dashboard.models.enterprise import Business

class Command(BaseCommand):
    help = 'Crea i gruppi base'

    def handle(self, *args, **options):   
        from django.contrib.auth.models import Group, Permission
        from django.contrib.contenttypes.models import ContentType

        # Creazione dei gruppi
        influencer_group, created = Group.objects.get_or_create(name='Influenzer')
        enterprise_group, created = Group.objects.get_or_create(name='Enterprise')

        # Creazione di permessi specifici per ogni gruppo (esempio)
        # Aggiungi qui i permessi che desideri per ogni gruppo
        # esempio: 'can_publish', 'can_manage_business'

        # Supponiamo che tu abbia un modello chiamato 'Business' e voglia assegnargli permessi
        # per la gestione del business:
        content_type = ContentType.objects.get_for_model(Business)
        can_change_business = Permission.objects.create(
            codename='can_change_business',
            name='Can Change Business',
            content_type=content_type
        )
        content_types = ContentType.objects.all()
        for content_type in content_types:
            permissions = Permission.objects.filter(content_type=content_type)
            for permission in permissions:
                if permission: # edit conditions
                    # Aggiungi permessi ai gruppi
                    influencer_group.permissions.add(can_change_business)  # Aggiungi permessi all'influencer
                    enterprise_group.permissions.add(can_change_business)  # Aggiungi permessi all'enterprise