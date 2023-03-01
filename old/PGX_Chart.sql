SELECT
	Mfg,
	Club,
	ROUND(AVG(Carry),0) AS AvgCarry,
	ROUND(MAX(Carry),0) AS MaxCarry,
	ROUND(AVG(TotalDistance),0) AS TotalDist,
	ROUND(MAX(TotalDistance),0) AS MaxTotalDist
	
FROM results

WHERE 
		Mfg = "PGX One Length"
	AND ((Club == 'LW' and Carry > 50)
	or 	(Club == 'SW' and Carry > 60)
	or	(Club == 'GW' and Carry > 80)
	or 	(Club == 'PW' and Carry > 90)
	or 	(Club == 'I9' and Carry > 100)
	or 	(Club == 'I8' and Carry > 110)
	or	(Club == 'I7' and Carry > 120)
	or 	(Club == 'I6' and Carry > 130)
	or 	(Club == 'I5' and Carry > 140)
	or 	(Club == 'I4' and Carry > 150)
	or 	(Club == 'I3' and Carry > 160))

GROUP By 
	Mfg,
	Club

ORDER By
	mfg,
	club DESC
