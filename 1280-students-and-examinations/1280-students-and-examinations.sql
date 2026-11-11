# Write your MySQL query statement below
select e1.student_id, e1.student_name, e3.subject_name, count(e2.student_id) as attended_exams
from Students as e1 cross join Subjects as e3 left join Examinations as e2 on e1.student_id = e2.student_id and e2.subject_name = e3.subject_name
group by e1.student_id, e1.student_name, e3.subject_name
order by e1.student_id, e1.student_name, e3.subject_name