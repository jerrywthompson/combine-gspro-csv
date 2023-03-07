SELECT PracticeDtTm,Ball_Speed, Side_Spin, Back_Spin, count(*)
from results a

GROUP BY PracticeDtTm, Ball_Speed, Side_Spin, Back_Spin
HAVING count(*) > 1

-- ON a.PracticeDtTm = b.PracticeDtTm 
-- AND a.Ball_Speed = b.Ball_Speed
-- AND a.Side_Spin = b.Side_Spin

-- ORDER BY a.PracticeDtTm



