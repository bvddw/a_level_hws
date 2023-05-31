task 1) 
create table people (id serial, name varchar(255), pwd varchar(255), email varchar(255), gender varchar(1));
insert into people
(name, pwd, email, gender)
values
('Vasya', '21341234qwfsdf', 'mmm@mmail.com', 'm'),
('Alex', '21341234', 'mmm@gmail.com', 'm'),
('Alexey', 'qq21341234Q', 'alexey@gmail.com', 'm'),
('Helen', 'MarryMeeee', 'hell@gmail.com', 'f'),
('Jenny', 'SmakeMyb', 'eachup@gmail.com', 'f'),
('Lora', 'burn23', 'tpicks@gmail.com', 'f');
INSERT 0 6

select * from people;
 id |  name  |      pwd       |      email       | gender
----+--------+----------------+------------------+--------
  1 | Vasya  | 21341234qwfsdf | mmm@mmail.com    | m
  2 | Alex   | 21341234       | mmm@gmail.com    | m
  3 | Alexey | qq21341234Q    | alexey@gmail.com | m
  4 | Helen  | MarryMeeee     | hell@gmail.com   | f
  5 | Jenny  | SmakeMyb       | eachup@gmail.com | f
  6 | Lora   | burn23         | tpicks@gmail.com | f
(6 rows)

task 2 (without UNION)) 
select concat ('This is ', name, ', ',
	case gender
		when 'f' then 'she'
		else 'he'
	end,
	' has email ', email) as "info"
from 
	people;
                     info
-----------------------------------------------
 This is Vasya, he has email mmm@mmail.com
 This is Alex, he has email mmm@gmail.com
 This is Alexey, he has email alexey@gmail.com
 This is Helen, she has email hell@gmail.com
 This is Jenny, she has email eachup@gmail.com
 This is Lora, she has email tpicks@gmail.com
(6 rows)

task 3)
select
	concat ('We have ', 
		count(case when gender = 'm' then 1 end), 
	' boys!') as "Gender information" 
from 
	people
union
select
	concat ('We have ', 
		count(case when gender = 'f' then 1 end),
	' girls!') as "Gender information" 
from 
	people;
 Gender information
--------------------
 We have 3 boys!
 We have 3 girls!
(2 rows)

task 4)
select 
	name, count(word) as words 
from 
	vocabulary 
inner join 
	word on (vocabulary.id = word.vocabulary_id) 
group by 
	vocabulary.name 
order by 
	case 
		when name = 'animals' then 1 
		when name = 'school' then 2 
		when name = 'nature' then 3 
		when name = 'human' then 4 
		when name = 'SF' then 5 
	end;
  name   | words
---------+-------
 animals |    10
 school  |    10
 nature  |    10
 human   |    10
 SF      |    10
(5 rows)
