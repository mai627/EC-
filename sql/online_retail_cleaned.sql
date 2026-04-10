SELECT 
	*,
	UnitPrice * Quantity AS TotalSales
FROM online_retail 
WHERE 
	Quantity > 0
	AND UnitPrice > 0
	AND Description IS NOT NULL
	AND CustomerID IS NOT NULL;
