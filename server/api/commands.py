import csv
import json
import click
from flask.cli import with_appcontext
from .extensions import guard
from .models import *


@click.command(name='import_data')
@with_appcontext
def import_data():
    import_users()
    import_jobs()
    import_work_experience()
    import_skill()
    import_related_skills()


def import_users():
    print('Importing Users')
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
    print('Importing Jobs')
    failed_count = 0
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
                failed_count += 1
                pass
    print(f'{failed_count} jobs failed to import')


def import_work_experience():
    print('Importing Work Experience')
    user_id = 2  # admin/employer is 1, candidates start from 2 based on import
    old_id = None

    with open('/home/kieran/Dev/Python/Flask/project_react_flask/server/data/work_experience/Experience.csv',
              newline='\n') as file:
        reader = csv.DictReader(file)
        for row in reader:
            work = WorkExperience(employer_name=row['Employer.Name'],
                                  position_name=row['Position.Name'],
                                  job_description=row['Job.Description'],
                                  city=row['City'],
                                  county=row['State.Name'],
                                  postcode=row['State.Code'],
                                  salary=row['Salary'],
                                  created_at=row['Created.At'],
                                  updated_at=row['Updated.At'],
                                  user_id=user_id)
            if row['Start.Date'] != '' and row['Start.Date'] != 'NA':
                work.start_date = row['Start.Date']
            if row['End.Date'] != '' and row['End.Date'] != 'NA':
                work.end_date = row['End.Date']

            if old_id is None:
                old_id = row['Applicant.ID']  # remember the old user id
            if old_id != row['Applicant.ID']:
                user_id += 1
                old_id = None  # reset if not the same

            db.session.add(work)
            db.session.commit()


def import_skill():
    print('Importing Skils')
    with open('/home/kieran/Dev/Python/Flask/project_react_flask/server/data/skils/cleaned_related_skills.json') as json_file:
        for line in json_file:
            data = json.loads(line)
            skill = Skill(name=data['name'])
            db.session.add(skill)
            db.session.commit()


def import_related_skills():
    print('Importing Related Skils')
    failed_count = 0
    with open('/home/kieran/Dev/Python/Flask/project_react_flask/server/data/skils/cleaned_related_skills.json') as json_file:
        for line in json_file:
            data = json.loads(line)
            try:
                skill = Skill.query.filter_by(name=data['name']).one_or_none()
                for i in range(1, 10):
                    related_skill_obj = Skill.query.filter_by(name=data['related_' + str(i)]).one_or_none()
                    related_skill = RelatedSkills(skill_id=skill.id, related_skill_id=related_skill_obj.id)
                    db.session.add(related_skill)
                    db.session.commit()
            except AttributeError:
                failed_count += 1
                pass
    print(f'{failed_count} related skills blank')


