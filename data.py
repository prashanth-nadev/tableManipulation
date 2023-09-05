import sqlite3

DATABASE = 'employee.db'


def create_and_insert_employee_data():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee_data (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            department TEXT,
            job_title TEXT,
            salary REAL,
            email TEXT,
            phone_number TEXT
        )
    ''')

    data_list = \
        [
            {
                'first_name': 'Prashanth',
                'last_name': 'N',
                'department': 'Development',
                'job_title': 'Backend Developer',
                'salary': 60000.00,
                'email': 'prashanth23@pinaca.com',
                'phone_number': '9789942415'
            },
            {
                'first_name': 'Abinesh',
                'last_name': 'S',
                'department': 'Development',
                'job_title': 'Full Stack Developer',
                'salary': 55000.00,
                'email': 'abinesh7@pinaca.com',
                'phone_number': '8883906207'
            },
            {
                'first_name': 'Arun',
                'last_name': 'M',
                'department': 'Testing',
                'job_title': 'Automation Tester',
                'salary': 30000.00,
                'email': 'arun23@pinaca.com',
                'phone_number': '9876567898'
            },
            {
                'first_name': 'Shankar',
                'last_name': 'S',
                'department': 'Development',
                'job_title': 'Full Stack Intern',
                'salary': 15000.00,
                'email': 'shankar11@pinaca.com',
                'phone_number': '6367890987'
            },
            {
                'first_name': 'Gowtham',
                'last_name': 'J',
                'department': 'Network',
                'job_title': 'Network Engineer',
                'salary': 50000.00,
                'email': 'gowtham89@pinaca.com',
                'phone_number': '6789321234'
            },
            {
                'first_name': 'Surya',
                'last_name': 'P',
                'department': 'Development',
                'job_title': 'Full Stack Developer',
                'salary': 55000.00,
                'email': 'surya56@pinaca.com',
                'phone_number': '9871236547'
            },
            {
                'first_name': 'Rohith',
                'last_name': 'S',
                'department': 'Network',
                'job_title': 'Network Engineer',
                'salary': 80000.00,
                'email': 'rohith54@pinaca.com',
                'phone_number': '9845321234'
            },
            {
                'first_name': 'Sanjay',
                'last_name': 'A',
                'department': 'Network',
                'job_title': 'Network Engineer Intern',
                'salary': 12500.00,
                'email': 'sanjay11@pinaca.com',
                'phone_number': '9812321232'
            },
            {
                'first_name': 'Manoj',
                'last_name': 'K',
                'department': 'Testing',
                'job_title': 'Manual Tester',
                'salary': 90000.00,
                'email': 'manoj456@pinaca.com',
                'phone_number': '9854345676'
            },
            {
                'first_name': 'Sownder',
                'last_name': 'P',
                'department': 'Development',
                'job_title': 'Front End Developer',
                'salary': 40000.00,
                'email': 'sownder90@pinaca.com',
                'phone_number': '9872123444'
            },
            {
                'first_name': 'Chandru',
                'last_name': 'L',
                'department': 'Testing',
                'job_title': 'Backend Developer',
                'salary': 60000.00,
                'email': 'prashanth23@pinaca.com',
                'phone_number': '8765459898'
            },
            {
                'first_name': 'Lakshin',
                'last_name': 'A',
                'department': 'Testing',
                'job_title': 'Automation Tester',
                'salary': 55000.00,
                'email': 'lakshin21@pinaca.com',
                'phone_number': '7898765434'
            },
            {
                'first_name': 'Chinrasu',
                'last_name': 'G',
                'department': 'Network',
                'job_title': 'Network Engineer',
                'salary': 60000.00,
                'email': 'chinrasu99@pinaca.com',
                'phone_number': '9871245432'
            },
            {
                'first_name': 'Pradeep',
                'last_name': 'S',
                'department': 'Development',
                'job_title': 'Full Stack Developer',
                'salary': 55000.00,
                'email': 'abinesh7@pinaca.com',
                'phone_number': '8876754348'
            },
            {
                'first_name': 'Vignesh',
                'last_name': 'S',
                'department': 'Network',
                'job_title': 'Network Engineer Intern',
                'salary': 20000.00,
                'email': 'vignesh89@pinaca.com',
                'phone_number': '7876567776'
            },
            {
                'first_name': 'Sharan',
                'last_name': 'B',
                'department': 'Development',
                'job_title': 'Full Stack Intern',
                'salary': 35000.00,
                'email': 'sharah69@pinaca.com',
                'phone_number': '9876544567'
            }

        ]

    query = """
        INSERT INTO employee_data (
            first_name, last_name, department, job_title, salary, email, phone_number
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    for data in data_list:
        cursor.execute(query, (
            data['first_name'],
            data['last_name'],
            data['department'],
            data['job_title'],
            data['salary'],
            data['email'],
            data['phone_number']
        ))

    conn.commit()
    conn.close()


create_and_insert_employee_data()
