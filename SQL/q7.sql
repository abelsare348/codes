--learning : we can apply filter condition in column selection when we derive column using agregate function.

This is the same question as problem #3 in the SQL Chapter of Ace the Data Science Interview!

Assume youre given the table on user viewership categorised by device type where the three types are laptop, tablet, and phone.

Write a query that calculates the total viewership for laptops and mobile devices where mobile is defined as the sum of tablet and phone viewership. Output the total viewership for laptops as laptop_reviews and the total viewership for mobile devices as mobile_views.

Effective 15 April 2023, the solution has been updated with a more concise and easy-to-understand approach.

viewership Table
Column Name	Type
user_id	integer
device_type	string ('laptop', 'tablet', 'phone')
view_time	timestamp
viewership Example Input
user_id	device_type	view_time
123	tablet	01/02/2022 00:00:00
125	laptop	01/07/2022 00:00:00
128	laptop	02/09/2022 00:00:00
129	phone	02/09/2022 00:00:00
145	tablet	02/24/2022 00:00:00
Example Output
laptop_views	mobile_views
2	3

Answer: 
--solution 1 using filter in agregate: -
 SELECT 
  COUNT(*) FILTER (WHERE device_type = 'laptop') AS laptop_views,
  COUNT(*) FILTER (WHERE device_type IN ('tablet', 'phone'))  AS mobile_views 
FROM viewership;

--solution 2 normal solution

select sum(case when device_type='laptop' then 1 else 0 end ) laptop_views,
      sum(case when device_type in ('tablet','phone') then 1 else 0 end ) mobile_views from viewership

--solution 3 that wasnt a feasible solution.

select sum(laptop_views) laptop_views,sum(mobile_views) from
 (select case when device_type='laptop' then cnt end as laptop_views,case when device_type='tablet' or device_type='phone' then sum(cnt) end as mobile_views
  from (select device_type,count(1) as cnt from viewership GROUP BY 1) as t group by device_type,cnt) as f