--1070: Product Sales Analysis 3
select product_id, year as first_year, quantity, price
from Sales 
where (product_id, year) in (
    select product_id, MIN(year) 
    from Sales 
    group by product_id 
)
;
