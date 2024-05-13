from django_seed import Seed
from faker import Faker
from django.contrib.auth.hashers import make_password
from api.models.admin.model import Admin
from api.models.user.model import User
from api.models.doctor.model import Doctor
from api.models.user_support.model import UserSupport
from api.models.assignment.model import Assignment
from api.models.report.model import Report
from api.models.recipe.model import Recipe
from api.models.medicine.model import Medicine

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
    'reportName': faker.word(),
    'disease': faker.word(),
    'reportInfo': faker.text(),
})

# Seed para la tabla Recipe
seeder.add_entity(Recipe, 10, {
    'doctorId': lambda x: Doctor.objects.order_by('?').first(),
    'userId': lambda x: User.objects.order_by('?').first(),
    'reportId': lambda x: Report.objects.order_by('?').first(),
    'medicineIds': [Medicine.objects.order_by('?').first().id for _ in range(seeder.faker.random_int(min=1, max=5))],  # Lista de IDs de medicamentos aleatorios
    'dateFinish': seeder.faker.date_time_between(start_date='-30d', end_date='+30d'),
    'active': True
})

# Seed para la tabla Medicine
seeder.add_entity(Medicine, 10, {
    'name': 'Nombre del medicamento',
    'morningDosis': faker.random_element(elements=(1, 0.5, 0)),
    'noonDosis': faker.random_element(elements=(1, 0.5, 0)),
    'nightDosis': faker.random_element(elements=(1, 0.5, 0)),
    'recipes': lambda x: [Recipe.objects.order_by('?').first() for _ in range(faker.random_int(min=1, max=5))],
})

# Ejecutar los seeders
seeder.execute()
