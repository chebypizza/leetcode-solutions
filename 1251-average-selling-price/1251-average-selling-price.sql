# Write your MySQL query statement below
select e1.product_id, ifnull(round(sum(units * price) / sum(units), 2), 0) as average_price
from Prices e1 left join UnitsSold e2 on e1.product_id = e2.product_id and e2.purchase_date between e1.start_date and e1.end_date
group by e1.product_id