from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from faker import Faker


class Command(BaseCommand):
    command_help = 'Generates bulk users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='The number of users to generate')

    def handle(self, *args, **options):
        count = options['count']

        if count < 1 or count > 10:
            raise CommandError("Count must be from 1 to 10")

        faker = Faker()
        users = []
        for i in range(count):
            username = faker.user_name()
            email = faker.ascii_email()
            password = faker.password()
            user = User(username=username, email=email)
            user.set_password(password)
            users.append(user)

        User.objects.bulk_create(users)

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {count} users!'))
