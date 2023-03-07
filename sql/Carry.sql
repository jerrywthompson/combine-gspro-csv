SELECT
	Mfg,
	Club,
	Ball,
	ROUND(AVG(Carry),0) AS "Avg Carry",
	ROUND(MAX(Carry),0) AS "Max Carry",
	ROUND(AVG(Total_Distance),0) AS "Total Dist",
	ROUND(MAX(Total_Distance),0) AS "Max Total Dist",
	ROUND(AVG(Club_Speed)) AS "Club Speed",
	ROUND(MAX(Club_Speed)) AS "Max Club Speed",
	ROUND(AVG(Ball_Speed)) AS "Ball Speed",
	ROUND(Max(Ball_Speed)) AS "Max Ball Speed"
	
	
FROM results

GROUP By 
	Mfg,
	Club,
	Ball
	
ORDER By 
	Mfg,
	Club DESC,
	ROUND(AVG(Carry),0) DESC,
	Ball



















