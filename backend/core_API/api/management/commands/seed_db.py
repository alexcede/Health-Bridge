from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Seed the database with initial data'
    name = 'seed_db'

    def handle(self, *args, **options):
        from django_seed import Seed
        from faker import Faker
        from django.contrib.auth.hashers import make_password
        from api.models import Admin, Doctor, User, UserSupport, Assignment, Report, Recipe

        seeder = Seed.seeder(locale='es_ES')
        faker = Faker('es_ES')

        # Seed para la tabla Admin
        seeder.add_entity(Admin, 3, {
            'email': lambda x: faker.unique.email(),
            'password': make_password('admin'),
            'active': True
        })

        # Seed para la tabla Doctor
        seeder.add_entity(Doctor, 10, {
            'email': lambda x: faker.unique.email(),
            'password': make_password('doctor'),
            'dni': lambda x: faker.unique.numerify(text='##########'), 
            'photo': faker.image_url(),
            'name': faker.first_name(),
            'firstSurname': faker.last_name(),
            'secondSurname': faker.last_name(),
            'phoneNumber': lambda x: faker.unique.phone_number(),
            'active': True
        })

        # Seed para la tabla User
        seeder.add_entity(User, 10, {
            'email': lambda x: faker.unique.email(),
            'password': make_password('user'),
            'photo': faker.image_url(),
            'name': faker.first_name(),
            'firstSurname': faker.last_name(),
            'secondSurname': faker.last_name(),
            'phoneNumber': lambda x: faker.unique.phone_number(),
            'healthCardCode': lambda x: faker.unique.random_number(digits=10),
            'birthDate': faker.date_of_birth(),
            'gender': faker.random_element(elements=('F', 'M')),
            'dni': lambda x: faker.unique.numerify(text='##########'), 
            'address': faker.address(),
            'postalCode': faker.postcode(),
            'active': True
        })

        # Seed para la tabla UserSupport
        seeder.add_entity(UserSupport, 10, {
            'email': lambda x: faker.unique.email(),
            'password': make_password('usersupport'),
            'name': faker.first_name(),
            'firstSurname': faker.last_name(),
            'secondSurname': faker.last_name(),
            'phoneNumber': lambda x: faker.unique.phone_number(),
            'active': True
        })

        # Seed para la tabla Assignment
        seeder.add_entity(Assignment, 10, {
            'doctorId': lambda x: Doctor.objects.order_by('?').first(),
            'userId': lambda x: User.objects.order_by('?').first(),
            'dateCreated': faker.date_time_this_year()
        })

        # Seed para la tabla Report
        seeder.add_entity(Report, 10, {
            'doctorId': lambda x: Doctor.objects.order_by('?').first(),
            'userId': lambda x: User.objects.order_by('?').first(),
            'reportInfo': faker.text(),
            'dateCreated': faker.date_time_this_year()
        })

        # Seed para la tabla Recipe 
        seeder.add_entity(Recipe, 10, {
            'doctorId': lambda x: Doctor.objects.order_by('?').first(),
            'userId': lambda x: User.objects.order_by('?').first(),
            'reportId': lambda x: Report.objects.order_by('?').first(),
            'medicine': faker.word(),
            'dateCreated': faker.date_time_this_year()
        })

        # Ejecutar los seeders
        seeder.execute()
