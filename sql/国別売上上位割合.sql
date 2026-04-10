SELECT 
	SUM(CASE WHEN Country = 'United Kingdom' THEN Quantity * UnitPrice ELSE 0 END) * 100 /
	SUM(Quantity * UnitPrice) AS UK_rate
FROM online_retail
WHERE Quantity > 0 AND UnitPrice > 0;