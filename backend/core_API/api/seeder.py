from django_seed import Seed
from faker import Faker
from django.contrib.auth.hashers import make_password
from api.models import Admin, Doctor, User, UserSupport, Assignment, Report, Recipe

seeder = Seed.seeder(locale='es_ES')
faker = Faker(locale='es_ES')

# Seed para la tabla Admin
seeder.add_entity(Admin, 1, {
    'email': 'admin',
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

# Seed para la tabla Assignment (Nota: Asegúrate de tener al menos 10 Doctores y 10 Usuarios en la base de datos antes de ejecutar este seeder)
seeder.add_entity(Assignment, 10, {
    'doctorId': lambda x: Doctor.objects.order_by('?').first(),
    'userId': lambda x: User.objects.order_by('?').first(),
    'active': True
})

# Seed para la tabla Report (Nota: Asegúrate de tener al menos 10 Doctores y 10 Usuarios en la base de datos antes de ejecutar este seeder)
seeder.add_entity(Report, 10, {
    'doctorId': lambda x: Doctor.objects.order_by('?').first(),
    'userId': lambda x: User.objects.order_by('?').first(),
    'reportInfo': faker.text(),
})

# Seed para la tabla Recipe (Nota: Asegúrate de tener al menos 10 Doctores, 10 Usuarios y 10 Reports en la base de datos antes de ejecutar este seeder)
seeder.add_entity(Recipe, 10, {
    'doctorId': lambda x: Doctor.objects.order_by('?').first(),
    'userId': lambda x: User.objects.order_by('?').first(),
    'reportId': lambda x: Report.objects.order_by('?').first(),
    'medicine': faker.word(),
    'active': True
})

# Ejecutar los seeders
seeder.execute()
