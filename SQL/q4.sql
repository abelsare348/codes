-- Given table 

customer_id, flight_no, origin, destination
1             1         Delhi       Hyderabad
1             2         Hyderabad   Kochi
1             3         Kochi       Mangalore
2             1         Mumbai	    Ayodhya
2             2         Ayodhya     Chennai

o/p:

customer_id origin          ldestination
1           Delhi           Mangalore
2           Mumbai          Chennai

Answer: 
select a.customer_id,a.origin,b.destination from (select f.customer_id,f.flight_no,f.origin,f.destination,t.max,t.min from flight f join (select customer_id,max(flight_no),min(flight_no) from flight group by 1) t on f.customer_id=t.customer_id) a join (select f.customer_id,f.flight_no,f.origin,f.destination,t.max,t.min from flight f join (select customer_id,max(flight_no),min(flight_no) from flight group by 1) t on f.customer_id=t.customer_id) b on a.flight_no!=b.flight_no and a.flight_no=a.min and b.flight_no=b.max and a.max=b.max;
