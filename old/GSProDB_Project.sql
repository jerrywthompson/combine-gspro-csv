SELECT
	Mfg,
	Club,
	ROUND(AVG(Carry),0) AS Carry,
	ROUND(MAX(Carry),0) AS MaxCarry,
	ROUND(AVG(TotalDistance),0) AS TotalDist,
	ROUND(MAX(TotalDistance),0) AS MaxTotalDist
	
FROM results

WHERE

	    (Club == 'LW' and Carry > 50)
	or 	(Club == 'SW' and Carry > 60)
	or	(Club == 'GW' and Carry > 80)
	or 	(Club == 'PW' and Carry > 90)
	or 	(Club == 'I9' and Carry > 100)
	or 	(Club == 'I8' and Carry > 110)
	or	(Club == 'I7' and Carry > 120)
	or 	(Club == 'I6' and Carry > 130)
	or 	(Club == 'I5' and Carry > 140)
	or 	(Club == 'I4' and Carry > 150)
	or 	(Club == 'I3' and Carry > 160)

GROUP By 
	Mfg,
	Club

ORDER By
	mfg,
	club DESC



































</sql><sql name="Ball_specs.sql">SELECT
	Ball,
	Mfg,
	Club,
	ROUND(AVG(Carry),0) AS AvgCarry,
	ROUND(MAX(Carry),0) AS MaxCarry,
	ROUND(AVG(TotalDistance),0) AS AvgTotalDist,
	ROUND(MAX(TotalDistance),0) AS MaxTotalDist,
	MAX(ClubSpeed) AS MaxClubSpeed,
	MAX(BallSpeed) AS MaxBallSpeed
	
FROM results

WHERE 
		(Club == 'LW' and Carry &gt; 50)
	or 	(Club == 'SW' and Carry &gt; 60)
	or	(Club == 'GW' and Carry &gt; 80)
	or 	(Club == 'PW' and Carry &gt; 90)
	or 	(Club == 'I9' and Carry &gt; 100)
	or 	(Club == 'I8' and Carry &gt; 110)
	or	(Club == 'I7' and Carry &gt; 120)
	or 	(Club == 'I6' and Carry &gt; 130)
	or 	(Club == 'I5' and Carry &gt; 140)
	or 	(Club == 'I4' and Carry &gt; 150)
	or 	(Club == 'I3' and Carry &gt; 160)

GROUP By
	Ball, 
	Mfg,
	Club

ORDER By
	MAX(BallSpeed) DESC,
	Mfg,
	Club



































</sql><sql name="SQL 4">SELECT * From results</sql><sql name="Carry_Max.sql">SELECT
	Mfg,
	Club,
	Ball,
	count(*) AS StrokeCnt,
	ROUND(AVG(Carry),0) AS AvgCarry,
	ROUND(AVG(TotalDistance),0) AS AvgTotalDist,
	ROUND(MAX(TotalDistance),0) AS MaxTotalDist,
	MAX(ClubSpeed) AS MaxClubSpeed,
	MAX(BallSpeed) AS MaxBallSpeed,
	PracticeDtTm AS PracticeDtTm,
	ROUND(MAX(Carry),0) AS MaxCarry
	
FROM results

WHERE 
		(Club == 'LW' and Carry &gt; 50)
	or 	(Club == 'SW' and Carry &gt; 60)
	or	(Club == 'GW' and Carry &gt; 80)
	or 	(Club == 'PW' and Carry &gt; 90)
	or 	(Club == 'I9' and Carry &gt; 100)
	or 	(Club == 'I8' and Carry &gt; 110)
	or	(Club == 'I7' and Carry &gt; 120)
	or 	(Club == 'I6' and Carry &gt; 130)
	or 	(Club == 'I5' and Carry &gt; 140)
	or 	(Club == 'I4' and Carry &gt; 150)
	or 	(Club == 'I3' and Carry &gt; 160)

GROUP By
	Mfg,
	Club,
	Ball

ORDER By
	MAX(Carry) DESC,
	Mfg,
	Club



































</sql><sql name="Carry_Avg.sql">SELECT
	Mfg,
	Club,
	Ball,
	count(*) AS StrokeCnt,
	ROUND(AVG(Carry),0) AS AvgCarry,
	ROUND(MAX(Carry),0) AS MaxCarry,
	ROUND(AVG(TotalDistance),0) AS TotalDist,
	ROUND(MAX(TotalDistance),0) AS MaxTotalDist,
	ROUND(AVG(ClubSpeed)) AS ClubSpeed,
	ROUND(MAX(ClubSpeed)) AS MaxClubSpeed,
	ROUND(AVG(BallSpeed)) AS BallSpeed,
	ROUND(Max(BallSpeed)) AS MaxBallSpeed
	
	
FROM results

WHERE 
	    (Club == 'LW' and Carry &gt; 50)
	or 	(Club == 'SW' and Carry &gt; 60)
	or	(Club == 'GW' and Carry &gt; 80)
	or 	(Club == 'PW' and Carry &gt; 90)
	or 	(Club == 'I9' and Carry &gt; 100)
	or 	(Club == 'I8' and Carry &gt; 110)
	or	(Club == 'I7' and Carry &gt; 120)
	or 	(Club == 'I6' and Carry &gt; 130)
	or 	(Club == 'I5' and Carry &gt; 140)
	or 	(Club == 'I4' and Carry &gt; 150)
	or 	(Club == 'I3' and Carry &gt; 160)

GROUP By 
	Mfg,
	Club,
	Ball
	
ORDER By 
	Mfg,
	Club DESC,
	ROUND(AVG(Carry),0) DESC,
	Ball


</sql><sql name="Carry_Max_by_Ball.sql">SELECT
	Mfg,
	Club,
	Ball,
	ROUND(AVG(Carry),0) AS AvgCarry,
	ROUND(MAX(Carry),0) AS MaxCarry,
	ROUND(AVG(TotalDistance),0) AS AvgTotalDist,
	ROUND(MAX(TotalDistance),0) AS MaxTotalDist,
	MAX(ClubSpeed) AS MaxClubSpeed,
	MAX(BallSpeed) AS MaxBallSpeed
	
FROM results

WHERE 
		(Club == 'LW' and Carry &gt; 50)
	or 	(Club == 'SW' and Carry &gt; 60)
	or	(Club == 'GW' and Carry &gt; 80)
	or 	(Club == 'PW' and Carry &gt; 90)
	or 	(Club == 'I9' and Carry &gt; 100)
	or 	(Club == 'I8' and Carry &gt; 110)
	or	(Club == 'I7' and Carry &gt; 120)
	or 	(Club == 'I6' and Carry &gt; 130)
	or 	(Club == 'I5' and Carry &gt; 140)
	or 	(Club == 'I4' and Carry &gt; 150)
	or 	(Club == 'I3' and Carry &gt; 160)

GROUP By
	Mfg,
	Club

-- ORDER By
-- 	MAX(C) DESC,
-- 	Mfg,
-- 	Club



































</sql><sql name="PGX_Chart.sql">SELECT
	Mfg,
	Club,
	ROUND(AVG(Carry),0) AS AvgCarry,
	ROUND(MAX(Carry),0) AS MaxCarry,
	ROUND(AVG(TotalDistance),0) AS TotalDist,
	ROUND(MAX(TotalDistance),0) AS MaxTotalDist
	
FROM results

WHERE 
		Mfg = &quot;PGX One Length&quot;
	AND ((Club == 'LW' and Carry &gt; 50)
	or 	(Club == 'SW' and Carry &gt; 60)
	or	(Club == 'GW' and Carry &gt; 80)
	or 	(Club == 'PW' and Carry &gt; 90)
	or 	(Club == 'I9' and Carry &gt; 100)
	or 	(Club == 'I8' and Carry &gt; 110)
	or	(Club == 'I7' and Carry &gt; 120)
	or 	(Club == 'I6' and Carry &gt; 130)
	or 	(Club == 'I5' and Carry &gt; 140)
	or 	(Club == 'I4' and Carry &gt; 150)
	or 	(Club == 'I3' and Carry &gt; 160))

GROUP By 
	Mfg,
	Club

ORDER By
	mfg,
	club DESC



































</sql><current_tab id="6"/></tab_sql></sqlb_project>
