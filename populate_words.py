from django.core.management.base import BaseCommand
from dictionary_app.models import Word

class Command(BaseCommand):
    help = 'Populate the database with sample words for each letter from a to z'

    def handle(self, *args, **options):
        letters = 'abcdefghijklmnopqrstuvwxyz'

        for letter in letters:
            words = [f'{letter}{i}' for i in range(1, 6)]  # Example words for each letter
            for word in words:
                Word.objects.create(word=word)

        self.stdout.write(self.style.SUCCESS('Words have been added to the database'))
