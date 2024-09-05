Given a table of Facebook posts, for each user who posted at least twice in 2021, write a query to find the number of days between each user’s first post of the year and last post of the year in the year 2021. Output the user and number of the days between each users first and last post.

p.s. If youve read the Ace the Data Science Interview and liked it, consider writing us a review?

posts Table:
Column Name	Type
user_id	integer
post_id	integer
post_date	timestamp
post_content	text
posts Example Input:
user_id	post_id	post_date	post_content
151652	599415	07/10/2021 12:00:00	Need a hug
661093	624356	07/29/2021 13:00:00	Bed. Class 8-12. Work 12-3. Gym 3-5 or 6. Then class 6-10. Another day thats gonna fly by. I miss my girlfriend
004239	784254	07/04/2021 11:00:00	Happy 4th of July!
661093	442560	07/08/2021 14:00:00	Just going to cry myself to sleep after watching Marley and Me.
151652	111766	07/12/2021 19:00:00	Im so done with covid - need travelling ASAP!
Example Output:
user_id	days_between
151652	2
661093	21

The catch here was they mentioned 2021 in the question and in the database there were only 2021 data which blocked our view on other data that 
we might can have the data for other years too..

solution:

SELECT 
	user_id, 
    MAX(post_date::DATE) - MIN(post_date::DATE) AS days_between
FROM posts
WHERE DATE_PART('year', post_date::DATE) = 2021 
GROUP BY user_id
HAVING COUNT(post_id)>1;

My solution:

SELECT user_id,Extract (day from (max(post_date)- min(post_date))) days_between FROM posts 
where extract(year from post_date)=2021 group by user_id having count(*)>1;
