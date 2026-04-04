from grades_manager import *

print("Welcome to the Student Grades Manager!")
print()
my_grades = {}

while True:
    menú_principal = input("Select an option:\n1. Add a student\n2. Print student grade averages\n3. Exit\n")
    if menú_principal == "1":
        add_student(my_grades)
    elif menú_principal == "2":
        opciones = input("Select an option:\na. Display all students\nb. Display selected students\n")
        while True:
            if opciones == "a":
                avg_by_student(my_grades)
            elif opciones == "b":
                nombres = input("Enter student names (comma-separated):\n")
                lista = []
                nombre = ""
                for letra in nombres:
                    if letra != ",":
                        nombre += letra
                    else:
                        lista.append(nombre.strip())
                        nombre = ""
                lista.append(nombre.strip())
                avg_by_student(my_grades, lista)
            else: 
                print("Invalid option selected!")
                opciones = input("Select an option:\na. Display all students\nb. Display selected students\n")
            break
    else:
        print("Goodbye!")
    
