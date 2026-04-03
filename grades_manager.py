student_grades = {
    "Alice": {
        "Math": 90.5,
        "English": 85.0,
        "Science": 92.0
    },
    "Bob": {
        "Math": 78.0,
        "English": 82.5,
        "History": 88.0
    },
    "Charlie": {
        "Science": 95.0,
        "English": 89.5
    }
}

def initialize_dict(student_name, subject_grades):
    new_dict = {student_name: subject_grades}
    return new_dict

def add_student(student_grades = {}):
    nombre = input("Enter student name:")
    nombre_tit = nombre.title()
    sub_gra = (input("Enter subject and grade (or 'exit' to finish):")).lower().strip()
    estudiante = {}
    while sub_gra != "exit":
        posición_coma = sub_gra.find(",")
        materia = (sub_gra[0:posición_coma]).title()
        nota = float(sub_gra[posición_coma+1:])
        sub_gra = (input("Enter subject and grade (or 'exit' to finish):")).lower().strip()
        estudiante[materia] = nota
        student_grades[nombre_tit] = estudiante
    return student_grades






