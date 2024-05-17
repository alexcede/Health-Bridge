from django.core.management.base import BaseCommand
from django_seed import Seed
from faker import Faker

from django.contrib.auth.hashers import make_password
from django.utils import timezone
import random
import string

from api.models.admin.model import Admin
from api.models.doctor.model import Doctor
from api.models.user.model import User
from api.models.user_support.model import UserSupport
from api.models.assignment.model import Assignment
from api.models.report.model import Report
from api.models.recipeInfo.model import RecipeInfo
from api.models.medicine.model import Medicine
from api.models.recipe.model import Recipe

class Command(BaseCommand):
    help = 'Seed the database with initial data'
    name = 'seed_db'

    def handle(self, *args, **options):
        seeder = Seed.seeder(locale='es_ES')
        faker = Faker('es_ES')

        def generate_phone_number():
            """Generate a phone number starting with 6 or 7 followed by 8 to 14 random digits"""
            return random.choice(['6', '7']) + ''.join(random.choices(string.digits, k=random.randint(9, 9)))

        def generate_timezone_aware_datetime():
            """Generate a timezone-aware datetime for the future"""
            naive_datetime = faker.date_time_between(start_date=timezone.now(), end_date="+30d")
            return timezone.make_aware(naive_datetime, timezone.get_current_timezone())

        # Seed para la tabla Admin
        seeder.add_entity(Admin, 3, {
            'email': lambda x: faker.unique.email(),
            'password': lambda x: make_password('admin'),
        })

        # Seed para la tabla Doctor
        seeder.add_entity(Doctor, 10, {
            'email': lambda x: faker.unique.email(),
            'password': lambda x: make_password('doctor'),
            'dni': lambda x: faker.unique.numerify(text='########') + random.choice(string.ascii_uppercase),
            'photo': lambda x: faker.image_url(),
            'name': lambda x: faker.first_name(),
            'firstSurname': lambda x: faker.last_name(),
            'secondSurname': lambda x: faker.last_name(),
            'phoneNumber': lambda x: generate_phone_number(),
        })

        # Seed para la tabla User
        seeder.add_entity(User, 10, {
            'email': lambda x: faker.unique.email(),
            'password': lambda x: make_password('user'),
            'photo': lambda x: faker.image_url(),
            'name': lambda x: faker.first_name(),
            'firstSurname': lambda x: faker.last_name(),
            'secondSurname': lambda x: faker.last_name(),
            'phoneNumber': lambda x: generate_phone_number(),
            'healthCardCode': lambda x: faker.unique.random_number(digits=10),
            'birthDate': lambda x: faker.date_of_birth(),
            'gender': lambda x: faker.random_element(elements=('F', 'M')),
            'dni': lambda x: faker.unique.numerify(text='########') + random.choice(string.ascii_uppercase),
            'address': lambda x: faker.address(),
            'postalCode': lambda x: faker.postcode(),
        })

        # Seed para la tabla UserSupport
        seeder.add_entity(UserSupport, 10, {
            'email': lambda x: faker.unique.email(),
            'password': lambda x: make_password('usersupport'),
            'name': lambda x: faker.first_name(),
            'firstSurname': lambda x: faker.last_name(),
            'secondSurname': lambda x: faker.last_name(),
            'phoneNumber': lambda x: generate_phone_number(),
            'active': True
        })

        # Seed para la tabla Assignment
        seeder.add_entity(Assignment, 10, {
            'doctor': lambda x: Doctor.objects.order_by('?').first(),
            'user': lambda x: User.objects.order_by('?').first(),
            'dateCreated': lambda x: timezone.now()
        })

        # Seed para la tabla Report
        seeder.add_entity(Report, 10, {
            'doctor': lambda x: Doctor.objects.order_by('?').first(),
            'user': lambda x: User.objects.order_by('?').first(),
            'reportName': lambda x: faker.word(),
            'disease': lambda x: faker.word(),
            'reportInfo': lambda x: faker.text(),
            'dateCreated': lambda x: timezone.now()
        })

        # Seed para la tabla Recipe
        seeder.add_entity(Recipe, 10, {
            'report': lambda x: Report.objects.order_by('?').first(),
            'dateFinish': lambda x: generate_timezone_aware_datetime(),
        })

        # Seed para la tabla Medicine
        seeder.add_entity(Medicine, 10, {
            'name': lambda x: faker.unique.word(),
            'dosis': lambda x: faker.random_number(digits=1),
        })

        # Seed para la tabla RecipeInfo
        seeder.add_entity(RecipeInfo, 10, {
            'recipe': lambda x: Recipe.objects.order_by('?').first(),
            'medicine': lambda x: Medicine.objects.order_by('?').first(),
            'morning_dose': lambda x: faker.random_element(elements=[1, 0.5, 0]),
            'noon_dose': lambda x: faker.random_element(elements=[1, 0.5, 0]),
            'night_dose': lambda x: faker.random_element(elements=[1, 0.5, 0]),
        })

        # Ejecutar los seeders
        seeder.execute()
