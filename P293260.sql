select
fish_count,
cast(month as unsigned) as month
from (select
count(*) as fish_count,
date_format(time, '%m') as month
from fish_info
group by date_format(time, '%m')
order by 2) x