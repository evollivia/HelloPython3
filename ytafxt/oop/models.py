# 성적 클래스
class SungJuk:
    def __init__(self, name, korean, english, math):
        self.sjno = 0
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math
        self.total = 0
        self.average = 0
        self.grade = '가'
        self.regdate = '2024-07-23 17:00:00'

# 사원 클래스
class Employee:
    def __init__(self, empid, fname, lname, email, phone, hdate, jobid, sal, comm, mgrid, deptid):
        self.empid = empid
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone = phone
        self.hdate = hdate
        self.jobid = jobid
        self.sal = sal
        self.comm = comm
        self.mgrid = mgrid
        self.deptid = deptid
