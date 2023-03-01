SELECT
	Ball,
	Mfg,
	Club,
	ROUND(AVG(Carry),0) AS AvgCarry,
	ROUND(MAX(Carry),0) AS MaxCarry,
	ROUND(AVG(TotalDistance),0) AS AvgTotalDist,
	ROUND(MAX(TotalDistance),0) AS MaxTotalDist,
	ROUND(AVG(ClubSpeed),0) AS AVGClubSpeed,
	MAX(ClubSpeed) AS MaxClubSpeed,
	MAX(BallSpeed) AS MaxBallSpeed
	
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
	Ball, 
	Mfg,
	Club

ORDER By
	MAX(BallSpeed) DESC,
	Mfg,
	Club



































