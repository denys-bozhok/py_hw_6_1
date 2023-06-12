teachers = [
    {
        "name": "Emy",
        "age": 23,
        "direction": ("PHP")
    },

    {
        "name": "Lee",
        "age": 23,
        "direction": ("JS")
    },

    {
        "name": "Duke",
        "age": 23,
        "direction": ("HTML", "Python")
    },

    {
        "name": "Peace",
        "age": 23,
        "direction": ("CSS" , "PHP")
    },
]

students = [
    {
        "name" : "John",
        "age" : 23 ,
        "skills" : [
            "HTML" , "CSS" , "JS"
        ]
    },

    {
        "name": "Bob",
        "age": 13,
        "skills": [
            "HTML", "CSS"
        ]
    },

    {
        "name": "Jack",
        "age": 34,
        "skills": [
            "HTML", "CSS", "JS" ,"PHP"
        ]
    },

    {
        "name": "Martin",
        "age": 90,
        "skills": [
            "HTML", "CSS", "JS", "PHP", "Python"
        ]
    },

    {
        "name": "Corey",
        "age": 90,
        "skills": [
            "JS"
        ]
    },
]


def deor_filtred_list(new_students: list):

    i = 1
    for st in new_students:
        for key, value in st.items():
            if key == "name":
                print(f"{i}) {value.upper()}")
                i += 1

# ---------------------------- 1 ---------------------------------





def filter_student_by_age(students: list, age: int) -> list:
    age = int(input("\nEnter student age, what you want to filter\n"))

    print(f"\nThis students have {age}+ (ooohhhh maaayyy) years old:")

    new_students = list(filter(lambda student: student["age"] >= age, students))

    deor_filtred_list(new_students)

    return new_students


# filter_student_by_age(students, age)


# --------------------------- 2 ---------------------------------
new_students = []


def filter_student_by_js(students: list, new_students: list):
    new_skill = input("\nEnter skill for filter\n")
    print(f"This students know {new_skill.upper()}:")

    for st in students:
        for key, value in st.items():
            if key == "skills":
                for v in value:
                    if v.lower() == new_skill.lower():
                        new_students.append(st)

    deor_filtred_list(new_students)

    return new_students


# filter_student_by_js(students, new_skill, new_students)


# --------------------------- 3 ---------------------------------

def students_to_teacher():
    s_skill = input("\nEnter skill of student fot add to teacher\n")
    t_skill = []

    for st in students:
        for key, value in st.items():
            if key == "skills":
                for v in value:
                    if v.lower() == s_skill.lower():
                        new_students.append(st)

    for teacher in teachers:
        for key_t, value_t in teacher.items():
            if key_t == "direction":
                t_skill.append(value_t)


# А ДАЛЬШЕ ЧЕТ ВАЩЕ НЕ ПОЛУЧАЕТСЯ


students_to_teacher()


# students_arr = []
# students_arr += "Carl", "Ban"
#
# for teacher in teachers:
#     teacher["students"] = students_arr
#
