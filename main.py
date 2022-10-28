from datetime import date

from application.salary import calculate_salary
from application.db.people import get_employees
from application.generator import generate


if __name__ == '__main__':
    print(f'Текущая дата - {date.today()}')
    generate()
    calculate_salary()
    get_employees()
