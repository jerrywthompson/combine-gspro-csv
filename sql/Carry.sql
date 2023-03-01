SELECT
	Mfg,
	Club,
	Ball,
	ROUND(AVG(Carry),0) AS AvgCarry,
	ROUND(MAX(Carry),0) AS MaxCarry,
	ROUND(AVG(TotalDistance),0) AS TotalDist,
	ROUND(MAX(TotalDistance),0) AS MaxTotalDist,
	ROUND(AVG(ClubSpeed)) AS ClubSpeed,
	ROUND(MAX(ClubSpeed)) AS MaxClubSpeed,
	ROUND(AVG(BallSpeed)) AS BallSpeed,
	ROUND(Max(BallSpeed)) AS MaxBallSpeed
	
	
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



















