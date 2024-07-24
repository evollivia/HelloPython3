create table sungjuk(
                        sjno       integer primary key auto_increment,
                        name       varchar(18) not null,
                        korean     int not null,
                        english    int not null,
                        math       int not null,
                        total      int not null,
                        average    float not null,
                        grade      varchar(2) not null,
    -- regdate    datetime default now()
                        regdate    datetime default current_timestamp  -- UTC + 9
);

insert into sungjuk(name, korean, english, math, total, average, grade)
values ('abc123', 99,99,99,297,99.0,'수');

select *
from sungjuk;

drop table sungjuk;