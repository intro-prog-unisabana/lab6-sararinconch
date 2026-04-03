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

