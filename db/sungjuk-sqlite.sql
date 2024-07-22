drop table sungjuk;

-- 성적 테이블 생성
create table sungjuk(
                        sjno       integer primary key autoincrement,
                        name       varchar(18) not null,
                        korean     int not null,
                        english    int not null,
                        math       int not null,
                        total      int not null,
                        average    float not null,
                        grade      varchar(2) not null,
    --regdate    datetime default (datetime('now'))   -- UTC
                        regdate    datetime default (datetime('now', 'localtime'))   -- UTC + 9
);

-- 성적 데이터 추가
insert into sungjuk(name, korean, english, math, total, average, grade)
values ('abc123', 99,99,99,297,99.0,'수');

-- 성적 데이터 전체 조회
select *
from sungjuk;

-- 성적 데이터 중 이름, 국어, 영어, 수학만 조회
select name, korean, english, math
from sungjuk;

-- 성적 데이터 중 학생번호, 이름, 국어, 영어, 수학 , 등록일만 조회
select sjno, name, korean, english, math, substr(regdate,0,11) regdate
from sungjuk;

-- 성적 데이터 중 이름이 abc123인 학생 조회
select *
from sungjuk
where name = 'abc123';

-- 성적 데이터 중 학생번호가 1인 학생 조회
select *
from sungjuk
where sjno = 1;

-- 성적 데이터 총 갯수 조회
select count(sjno) toal from sungjuk;
-- select count(*) toal from sungjuk;
-- select count(name) toal from sungjuk;