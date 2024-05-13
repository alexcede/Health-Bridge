from django_seed import Seed
from faker import Faker
from django.contrib.auth.hashers import make_password
from api.models.admin.model import Admin
from api.models.user.model import User
from api.models.doctor.model import Doctor
from api.models.user_support.model import UserSupport
from api.models.assignment.model import Assignment
from api.models.report.model import Report
from api.models.recipeInfo.model import RecipeInfo
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
    'doctor': lambda x: Doctor.objects.order_by('?').first(),
    'user': lambda x: User.objects.order_by('?').first(),
    'active': True
})

# Seed para la tabla Report (Nota: Asegúrate de tener al menos 10 Doctores y 10 Usuarios en la base de datos antes de ejecutar este seeder)
seeder.add_entity(Report, 10, {
    'doctor': lambda x: Doctor.objects.order_by('?').first(),
    'user': lambda x: User.objects.order_by('?').first(),
    'reportName': faker.word(),
    'disease': faker.word(),
    'reportInfo': faker.text(),
})

# Seed para la tabla RecipeInfo
seeder.add_entity(RecipeInfo, 10, {
        'user': lambda x: User.objects.order_by('?').first(),
        'doctor': lambda x: Doctor.objects.order_by('?').first(),
        'report': lambda x: Report.objects.order_by('?').first(),
        'dateFinish': lambda x: faker.date_time_this_year(),
        'active': True
    }
)
# Seed para la tabla Medicine
seeder.add_entity(Medicine, 10, {
        'name': lambda x: faker.word(),
        'dosis': lambda x: faker.random_number(digits=1),
    }
)

seeder.add_entity(Recipe, 10, {
        'recipeInfo': lambda x: lambda x: RecipeInfo.objects.order_by('?').first(),
        'medicine': lambda x: Medicine.objects.order_by('?').first(),
        'morning_dose': lambda x: faker.random_element([1, 0.5, 0]),
        'noon_dose': lambda x: faker.random_element([1, 0.5, 0]),
        'night_dose': lambda x: faker.random_element([1, 0.5, 0]),
        'active': True
    }
)
# Ejecutar los seeders
seeder.execute()
