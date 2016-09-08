create table Sailors(
        sid int PRIMARY KEY,
        sname varchar(30),
        rating int,
        age int
        );

create table Reserves(
        sid int,
        bid int,
	day date,
	PRIMARY KEY (sid, bid, day)
        );

create table Boats(
        bid int PRIMARY KEY,
	bname char(20),
	color char(10)
        );


insert into Sailors values (22,'dusting',7,45.0);
insert into Sailors values (29,'brutus',1,33.0);
insert into Sailors values (31,'lubber',8,55.5);
insert into Sailors values (32,'andy',8,25.5);
insert into Sailors values (58,'rusty',10,35);
insert into Sailors values (64,'horatio',7,16);
insert into Sailors values (71,'zorba',10,35);
insert into Sailors values (74,'horatio',9,25.5);
insert into Sailors values (85,'art',3,25.5);
insert into Sailors values (95,'bob',3,63.5);

insert into Reserves values (22,101,'1998/10/10');
insert into Reserves values (22,102,'1998/10/10');
insert into Reserves values (22,103,'1998/8/10');
insert into Reserves values (22,104,'1998/7/10');
insert into Reserves values (31,102,'1998/11/10');
insert into Reserves values (31,103,'1998/11/6');
insert into Reserves values (31,104,'1998/11/12');
insert into Reserves values (64,101,'1998/9/5');
insert into Reserves values (64,102,'1998/9/8');
insert into Reserves values (74,103,'1998/9/8');

insert into Boats values (101,'Interlake','blue');
insert into Boats values (102,'Interlake','red');
insert into Boats values (103,'Clipper','green');
insert into Boats values (104,'Marine','red');

