SELECT
	Ball,
	Mfg,
	Club,
	ROUND(AVG(Carry),0) AS "Avg Carry",
	ROUND(MAX(Carry),0) AS "Max Carry",
	ROUND(AVG(Total_Distance),0) AS "Avg Total Dist",
	ROUND(MAX(Total_Distance),0) AS "Max Total Dist",
	ROUND(MAX(Back_Spin),0) AS "Avg Back Spin",
	ROUND(MAX(Side_Spin),0) AS "Avg Side Spin",
	ROUND(AVG(Club_Speed),0) AS "Avg Club Speed",
	MAX(Club_Speed) AS "Max Club Speed",
	MAX(Ball_Speed) AS "Max Ball Speed"
	
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
	or 	(Club == 'DR-NS' and Carry > 160)

GROUP By
	Ball, 
	Mfg,
	Club

ORDER By
	MAX("Ball_Speed") DESC,
	Mfg,
	Club



































