-- 1661 - Average time of process per machine
select st.machine_id, round(avg(en.timestamp-st.timestamp), 3) as processing_time
from Activity st join Activity en
on st.machine_id=en.machine_id and st.process_id=en.process_id and st.activity_type='start' and en.activity_type='end'
group by st.machine_id
;
