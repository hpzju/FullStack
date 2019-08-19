CREATE TABLE `users2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text,
  `age` int not null default 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

INSERT INTO `users2` (`age`, `name`) VALUES (1,'Bob'), (5,'Vicky'), (6,'Sue'), (7,'Rich'), (8,'Raj');

show tables;

select * from users2;

drop table if exists users2;

select count(*) from users2;

show tables;

select * from smoke;

select s1.id as id1, s2.question as Q2, s2.id as id2, s1.question as Q1 from smoke as s1 inner join smoke as s2 on s1.id = s2.id;