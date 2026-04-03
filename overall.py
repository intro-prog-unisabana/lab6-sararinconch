students = {
  "s1": {"hw1": 80, "hw2": 90, "hw3": 100},
  "s2": {"hw1": 70, "hw2": 75, "hw3": 85},
  "s3": {"hw1": 95, "hw2": 85, "hw3": 90}
}

def student_averages(students):
    promedio_students = {}
    for key, value in students.items():
        value_s = value.values()
        promedio = round(sum(value_s)/len(value_s))
        promedio_students[key] = promedio
    return promedio_students

def assignment_averages(students):
    promedio_averages = {}
    for assignments in students.values():
        for assignment in assignments.keys():
            suma_prom = 0 
            for student in students.values():
                suma_prom += student[assignment]
            promedio_a = round(suma_prom/len(students))
            promedio_averages[assignment] = promedio_a
        break
    return promedio_averages






