def new_student(student_info:list):
    student_data = {}
    
    if len(student_info) != 5:
        print("ERROR: student_ info의 요소 수가 5가 아닙니다.")
        return {}
    
    name = student_info[0]
    
    if type(name) != str:
        print("ERROR: 이름이  str이 아닙니다.")
        return {}
    
    student_data["이름"] = name
    
    school = student_info[1]
    if type(school) != str:
        print("ERROR: 학교이름이  str이 아닙니다.")
        return {}
    if school[-2:] != "학교":
        print("ERROR: 학교이름이 학교로 끝나지 않습니다.")
        return {}
    student_data["학교"] = school
    
    grade = student_info[2]
    if type(grade) != int:
        print("ERROR: 학년이  int가 아닙니다.")
        return {}
    if not (0 < grade < 7):
        print("ERROR: 학년이 7보다 작은 자연수가 아닙니다.")
        return {}
    student_data["학년"] = grade
    
    tele = student_info[3]
    if type(tele) != str:
        print("ERROR: 연락처가   str이 아닙니다.")
        return {}
    if len(tele) != 11:
        print("ERROR: 연락처가 11자리가  아닙니다.")
        return {}
    student_data["연락처"] = tele
    
    course = student_info[4]
    if type(course) != list:
        print("ERROR: 수업이 list가 아닙니다.")
        return {}
    course_list = ["Python","Java","C","C++"]
    for c in course:
        if not(c in course_list):
            print("ERROR: 수업이 목록에 없습니다.")
            return {}
    
    student_data["수업"] = course
    
    print(f"새로운 학생의 정보를 완성했습니다.\n{student_data}\n")
    return student_data
    


def get_student(student_list, key_value_list):
    candidate = []
    for student in student_list:
        match = True
        for info in key_value_list:
            if student[info[0]]!=info[1]:
                match=False
                break
        if match:
            candidate.append(student)
    
    return candidate

def edit_student(stduent_db , key_value_list, edit_list):
    candidate_students = get_student(stduent_db,key_value_list)
    print("candidate_students:" ,candidate_students)
    for st in candidate_students:
        for info in edit_list:
            st[info[0]] = info[1]
    print("candidate_students:" ,candidate_students)
    
    
#####학생데이터
student_infos = [
    ["한넙죽", '한국중학교',1,'01012342345',['Python','C']],
    ["김거위", '오리초등학교',5,'01012342345',['Python']],
    ["로사", '한국중학교',2,'01012342345',['C++','Java']],
    ["리사", '한국초등학교',6,'01012342345',['C','C++']],
    ["이철수", '대한초등학교',5,'01012342345',['C','Python']],
    ["남영희", '대한중학교',1,'01012342345',['Python','Java']],
]


student_database = []
for student in student_infos:
    newbe = new_student(student)
    student_database.append(newbe)


print(get_student(student_database,[('이름','로사'),('학교','한국중학교')]))
edit_student(student_database,[('이름','로사'),('학교','한국중학교')],[("이름","빠")] )

print(student_database)
