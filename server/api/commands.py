import csv
import click
import random
from flask.cli import with_appcontext
from .extensions import db, guard
from .models.user import User
from .models.job import Job
from tqdm import tqdm  # progress bar


def csv_row_count(file, tsv):
    csv.field_size_limit(100000000)
    if tsv:
        return len(list(csv.reader(open(file, 'r'), delimiter='\t', quoting=csv.QUOTE_ALL))) - 1
    else:
        return len(list(csv.reader(open(file, 'r'), quoting=csv.QUOTE_ALL))) - 1  # minus 1 for header row


@click.command(name='import_users')
@with_appcontext
def import_users():
    file = '/home/kieran/Dev/Python/AI/Project_testing/competition_data/data/users.tsv'

    password_hash = guard.hash_password('test')

    admin = User(username='Kieran',
                 password=password_hash,
                 email='kieran@test.com',
                 first_name='Kieran',
                 last_name='Dee',
                 gender='male',
                 role='employer')

    db.session.add(admin)
    db.session.commit()

    row_count = csv_row_count(file, True)
    with open(file,
              newline='\n') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in tqdm(reader, total=row_count, desc='Importing Users'):
            user = User(id=row['UserID'],
                        username='test' + row['UserID'],
                        password=password_hash,
                        email='test' + row['UserID'] + '@email.com',
                        first_name='test' + row['UserID'],
                        last_name='test' + row['UserID'],
                        gender=random.choice(['male', 'female', 'other']),
                        role='candidate',
                        city=row['City'],
                        state=row['State'],
                        country=row['Country'],
                        zipcode=row['ZipCode'],
                        degree_type=row['DegreeType'],
                        major=row['Major'],
                        graduation_date=None if row['GraduationDate'] == '' else row['GraduationDate'],
                        work_history_count=row['WorkHistoryCount'],
                        work_history_years_experience=None if row['TotalYearsExperience'] == '' else row[
                            'TotalYearsExperience'],
                        employed=True if row['CurrentlyEmployed'] == 'Yes' else False,
                        managed_others=True if row['ManagedOthers'] == 'Yes' else False,
                        managed_how_many=row['ManagedHowMany'])
            db.session.add(user)
            db.session.commit()


@click.command(name='import_jobs')
@with_appcontext
def import_jobs():
    file = '/home/kieran/Dev/Python/AI/Project_testing/competition_data/data/jobs.tsv'

    failed_count = 0
    row_count = csv_row_count(file, True)

    with open(file,
              newline='\n') as file:
        reader = csv.DictReader(file, delimiter='\t', quoting=csv.QUOTE_ALL)
        for row in tqdm(reader, total=row_count, desc='Importing Jobs'):
            try:
                job = Job(id=row['JobID'],
                          job_title=row['Title'],
                          job_description=row['Description'],
                          requirements=row['Requirements'],
                          city=row['City'],
                          state=row['State'],
                          country=row['Country'],
                          zipcode=row['Zip5'],
                          start_date=row['StartDate'],
                          end_date=row['EndDate'])  # yyyy-mm-dd
                db.session.add(job)
                db.session.commit()
            except Exception:  # I know this is bad practise but I can't open the tsv to edit 3 lines out of 1 million
                failed_count += 1
                db.session.rollback() # rollback failed commit
    print(f'{failed_count} jobs failed to import')


@click.command(name='import_apps')
@with_appcontext
def import_apps():
    file = '/home/kieran/Dev/Python/AI/Project_testing/competition_data/data/apps.tsv'

    failed_count = 0

    row_count = csv_row_count(file, True)

    with open(file,
              newline='\n') as file:
        reader = csv.DictReader(file, delimiter='\t', quoting=csv.QUOTE_ALL)
        for row in tqdm(reader, total=row_count, desc='Importing Applications'):
            try:
                u = User.query.get(row['UserID'])
                job = Job.query.get(row['JobID'])
                u.applications.append(job)
                db.session.commit()
            except Exception:
                # Again bad practise but there's a lot of apps and I don't want to run it for 9/10 hours
                # and have it potentially error out near the end for an unknown reason
                failed_count += 1
                db.session.rollback() # rollback failed commit
    print(f'{failed_count} apps failed to import')
