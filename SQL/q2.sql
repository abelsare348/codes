-- Find duplicate emails in table

Find the email which occurs more than once in a table 


 id |  email
----+---------
  1 | a@b.com
  2 | c@d.com
  3 | a@b.com


--
queries: -create table person (id int primary key, email varchar);

	 -insert into person values (1,'a@b.com'),(2,'c@d.com'),(3,'a@b.com');
 
tip:  as we get some info , that we need to check whether  table has any dulicates means we need to check count of that column by adding group by cluase.

ans :  select email from person group by email having count(*)>1;

