select name_of_film from film_name where id = 6;
select name, surname from directors where id = 2;
select 1994;
select actor_1, actor_2, actor_3, actor_4, actor_5, actor_6, actor_7 from casting where id_film =6;

truncate table films;

alter sequence films_id_seq restart;

update films set id = DEFAULT;

insert into films(name_of_film, director, year, cast_film) values ( 
(select name_of_film from film_name where id = 6),
(select id from directors where name = 'Frank' and surname = 'Darabont'),
(1994),
(select id_film from casting where id_film = 6)
);

insert into films(name_of_film, director, year, cast_film) values (
(select name_of_film from film_name where id = 5),
(select id from directors where name = 'Frank' and surname = 'Darabont'),
(1999),
(select id_film from casting where id_film = 5)
);

insert into films(name_of_film, director, year, cast_film) values (
(select name_of_film from film_name where id = 1),
(select id from directors where name = 'Robert' and surname = 'Zemeckis'),
(1994),
(select id_film from casting where id_film = 1)
);

insert into films(name_of_film, director, year, cast_film) values (
(select name_of_film from film_name where id = 4),
(select id from directors where name = 'Steven' and surname='Spilberg'),
(1993),
(select id_film from casting where id_film = 4)
);

insert into films(name_of_film, director, year, cast_film) values (
(select name_of_film from film_name where id = 2),
(select id from directors where name = 'Christopher' and surname = 'Nolan'),
(2010),
(select id_film from casting where id_film = 2)
);


insert into films(name_of_film, director, year, cast_film) values (
(select name_of_film from film_name where id = 3),
(select id from directors where name = 'Luc' and surname = 'Besson'),
(1994),
(select id_film from casting where id_film = 3)
);

insert into films(name_of_film, director, year, cast_film) values (
(select name_of_film from film_name where id = 7),
(select id from directors where name = 'Christopher' and surname = 'Nolan'),
(1994),
(select id_film from casting where id_film = 7)
);

insert into films(name_of_film, director, year, cast_film) values (
(select name_of_film from film_name where id = 8),
(select id from directors where name = 'Luc' and surname = 'Besson'),
(1994),
(select id_film from casting where id_film = 8)
);

insert into films(name_of_film, director, year, cast_film) values (
(select name_of_film from film_name where id = 9),
(select id from directors where name = 'Steven' and surname='Spilberg'),
(2002),
(select id_film from casting where id_film = 9)
);

insert into films(name_of_film, director, year, cast_film) values (
(select name_of_film from film_name where id = 10),
(select id from directors where name = 'Steven' and surname='Spilberg'),
(1998),
(select id_film from casting where id_film = 10)
);



copy (select name_of_film, director, year, cast_film from films) to 'D:/Python/Git/Database/Output.txt';


-- output defines most popular names around actors.
select name, count(*) from actors group by name having count(*) > 1 order by 2;

-- How many films has been shooted by Steven  Spielberg from 1995 till 2009?

select name_of_film from films where director = (select id from directors where name = 'Steven' and surname='Spilberg') and
year >= 1995 and year <= 2009;

--Which is director made the most films?

select name , surname from directors where id = (select director from films group by director order by 1 DESC limit 1);

-- Did the actors of the same name act in one film?;

