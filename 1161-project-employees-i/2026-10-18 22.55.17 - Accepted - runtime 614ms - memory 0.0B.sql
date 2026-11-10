# Write your MySQL query statement below
select project_id, round(avg(experience_years), 2) as average_years
from Project as e1 join Employee as e2 on e1.employee_id = e2.employee_id
group by project_id