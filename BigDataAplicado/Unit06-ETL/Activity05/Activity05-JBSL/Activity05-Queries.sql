-- Obtener la lista de clientes junto con la cantidad total de compras y el monto total gastado.
SELECT Clients.Id, Clients.Name, SUM(Sales.Quantity) as SumQuantity, SUM(Sales.AmountTotal) as SumAmountTotal
FROM Clients
         JOIN Sales ON Clients.Id = Sales.ClientId
GROUP BY Clients.Id, Clients.Name;


-- Identificar los productos más vendidos en términos de cantidad y monto total de ventas.
SELECT Products.Id, Products.Name, SUM(Sales.Quantity) AS SumQuantity
FROM Products
         JOIN Sales ON Products.Id = Sales.ProductId
GROUP BY Products.Id, Products.Name
ORDER BY SumQuantity DESC

SELECT Products.Id, Products.Name, SUM(Sales.AmountTotal) AS SumAmountTotal
FROM Products
         JOIN Sales ON Products.Id = Sales.ProductId
GROUP BY Products.Id, Products.Name
ORDER BY SumAmountTotal DESC


-- Analizar la rentabilidad de cada producto en base a la diferencia entre el precio de venta y el costo.
SELECT Products.Id,
       Products.Name,
       (SUM(Sales.AmountTotal) - SUM(Sales.AmountBenefit)) / SUM(Sales.Quantity) AS CostPerUnit
FROM Products
         JOIN Sales ON Products.Id = Sales.ProductId
GROUP BY Products.Id, Products.Name
ORDER BY CostPerUnit DESC


-- Obtener un registro de las acciones realizadas por cada usuario en la plataforma.
SELECT Id, Name, Action, Date
FROM Employees
    JOIN Logs
ON Employees.Id = Logs.EmployeeId
WHERE Name = 'Stacey Mcintyre'
ORDER BY Id, Date


-- Recuperar las ventas que ocurrieron en el último año.
SELECT *
FROM Sales
WHERE Date LIKE CONCAT((SELECT YEAR (MAX (Date)) - 1 FROM Sales), '%')


-- Número de ventas por hora trabajada.
SELECT Employees.Id,
       Employees.Name,
       COUNT(Sales.EmployeeId) / (SUM(Shifts.`ShiftDuration`) / 3600) AS SalesPerHour
FROM Employees
         JOIN Sales ON Employees.Id = Sales.EmployeeId
         JOIN Shifts ON Employees.Id = Shifts.EmployeeId
GROUP BY Employees.Id, Employees.Name
ORDER BY SalesPerHour DESC;
