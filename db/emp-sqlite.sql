create table Employees(
    empid       integer primary key,
    fname       varchar(30) not null,
    lname       varchar(30) not null,
    email       varchar(100) not null,
    phone       varchar(25) not null,
    hdate       data        not null,
    jobid       varchar(10) not null,
    sal         integer     not null,
    comm        decimal(5, 2),
    mgrid       integer,
    deptid      integer
);

insert into Employees (empid, fname, lname, email, phone, hdate, jobid, sal, comm, mgrid, deptid)
VALUES (100,'Steven','King','SKING','515.123.4567','2003-06-17','AD_PRES',24000,null,null,90);

-- 데이터 조회1 - 리스트
select empid, fname, email, jobid, deptid
from Employees;

-- 데이터 조회2 - 상세
select *
from Employees
where empid = 100;


drop table Employees;