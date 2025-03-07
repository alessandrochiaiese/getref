from django.core.management.base import BaseCommand, CommandError
from django.core.management import get_commands, load_command_class

class Command(BaseCommand):
    help = 'Test email sending'

    def handle(self, *args, **options):        
        from django.core.mail import send_mail
        from django.conf import settings

        send_mail(
            'Test Email',
            'Questo è un test di invio email.',
            settings.EMAIL_HOST_USER,
            ['alessandro.chiaiese@libero.it'],
            fail_silently=False,
        )