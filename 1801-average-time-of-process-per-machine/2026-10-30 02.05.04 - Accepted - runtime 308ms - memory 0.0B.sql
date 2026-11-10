# Write your MySQL query statement below
select e1.machine_id, round(avg(e2.timestamp - e1.timestamp), 3) as processing_time
from Activity as e1 join Activity as e2 
on e1.process_id = e2.process_id and e1.machine_id = e2.machine_id
where e1.activity_type = 'start' and e2.activity_type = 'end'
group by machine_id