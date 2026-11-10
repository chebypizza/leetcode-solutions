# Write your MySQL query statement below
with preparedData as(
    select id, recordDate, temperature,
    lag(recordDate) over (order by recordDate) as prevDate,
    lag(temperature) over (order by recordDate) as prevTemperature
    from weather
)

select id
from preparedData
where temperature > prevTemperature and datediff(recordDate, prevDate) = 1