from bs4 import BeautifulSoup

html = ""


soup = BeautifulSoup(html, 'html.parser')
student_names_table = soup.find_all('table', class_=grades)
student_names = {}

for student_name in student_names:
    name = student_names_table.find('tr', td_=student)
    grade = student_names_table.find('tr', td_=student)

    student = { 'student': student, 'grade': grade}

    print(student)
