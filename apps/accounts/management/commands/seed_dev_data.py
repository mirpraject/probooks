from django.core.management.base import BaseCommand
from apps.accounts.models import User
from apps.schools.models import District, School, Class
from apps.gamification.models import Achievement
from apps.gamification.services import ensure_levels


class Command(BaseCommand):
    help = 'Создание тестовых данных для разработки'

    def handle(self, *args, **options):
        district, _ = District.objects.get_or_create(name='Test district')
        school, _ = School.objects.get_or_create(name='Test School 1', district=district)
        
        if not User.objects.filter(login='kxibragimov').exists():
            User.objects.create_superuser(
                login='kxibragimov', password='xx63blk', school=school,
            )
            
        if not User.objects.filter(login='admin1').exists():
            User.objects.create_user(
                login='admin1', password='admin123', role=User.Role.SCHOOL_ADMIN, school=school
            )

        cl, _ = Class.objects.get_or_create(number=1, parallel='A', language='ru', school=school)
        
        if not User.objects.filter(login='student1').exists():
            User.objects.create_user(
                login='student1', password='student123',
                role=User.Role.STUDENT, first_name='Ivan', last_name='Ivanov',
                school=school, grade=cl,
            )
            
        if not User.objects.filter(login='teacher1').exists():
            User.objects.create_user(
                login='teacher1', password='teacher123',
                role=User.Role.TEACHER, first_name='Maria', last_name='Petrova',
                school=school, subject='Math',
            )
            
        ensure_levels()
        self.stdout.write(self.style.SUCCESS(
            'Test data created/verified:\n'
            f'  Superadmin: kxibragimov / xx63blk\n'
            f'  School admin: admin1 / admin123\n'
            f'  Student: student1 / student123\n'
            f'  Teacher: teacher1 / teacher123\n'
            f'  School: {school.name}'
        ))
