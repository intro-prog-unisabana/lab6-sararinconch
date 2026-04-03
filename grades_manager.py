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
        print(f"Student {nombre_tit} successfully added to the grades management system.")
    return student_grades

def get_students(student_grades, keys):
    estudiantes = {}
    for estudiante_buscado in keys:
        estudiante_e = False
        for estudiante in student_grades:
            if estudiante_buscado.lower() == estudiante.lower():
                estudiantes[estudiante] = student_grades[estudiante]
                estudiante_e = True
                break
        if not estudiante_e:
            print(f"{estudiante_buscado.title()} not found!")
    return estudiantes

def avg_by_student(student_grades, keys = None):
    if keys == None:
        for key, value in student_grades.items():
            value_s = value.values()
            promedio = sum(value_s)/len(value_s)
            promedio_r = round(promedio, 1)
            print(f"{key}: {promedio_r}")
    else:
        seleccionados = get_students(student_grades, keys)
        for key, value in seleccionados.items():
            value_s = value.values()
            promedio = sum(value_s) / len(value_s)
            promedio_r = round(promedio, 1)
            print(f"{key}: {promedio_r}")





