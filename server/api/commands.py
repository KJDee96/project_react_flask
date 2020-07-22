import csv
import datetime
import click
from flask.cli import with_appcontext
from .extensions import guard, db
from .models import User, Job, Application, SavedJob, WorkExperience, Skill, RelatedSkills, WorkExperienceSkills, \
    JobSkills


@click.command(name='import_data')
@with_appcontext
def import_data():
    import_users()
    import_jobs()


def import_users():
    print("Importing Users")
    admin = User(username='Kieran',
                 password=guard.hash_password('test'),
                 email='kieran@test.com',
                 first_name='Kieran',
                 last_name='Dee',
                 gender='male',
                 role='employer')

    db.session.add(admin)
    db.session.commit()

    with open('/home/kieran/Dev/Python/Flask/project_react_flask/server/data/users/users_merged.csv',
              newline='\n') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user = User(username=row['username'],
                        password=guard.hash_password('test'),
                        email=row['email'],
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                        gender=row['gender'].lower(),
                        role='candidate')
            db.session.add(user)
            db.session.commit()


def import_jobs():
    print("Importing Jobs")
    failed = 0
    with open('/home/kieran/Dev/Python/Flask/project_react_flask/server/data/jobs/emed_40k_new.csv',
              newline='\n') as file:
        reader = csv.DictReader(file, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            try:
                job = Job(category=row['category'],
                          company_name=row['company_name'],
                          job_description=row['job_description'],
                          job_title=row['job_title'],
                          job_type=row['job_type'].lower().replace("/", "_").replace("-", "_"),
                          location=row['location'],
                          post_date=row['post_date'],  # yyyy-mm-dd
                          salary_offered=row['salary_offered'])
                db.session.add(job)
                db.session.commit()
            except AttributeError:
                failed += 1
                pass
    print(f'{failed} jobs failed to import')
