SELECT Users.name, SUM(Transactions.amount) AS balance
FROM Transactions
LEFT JOIN Users
USING(account)
GROUP BY Users.account
HAVING balance >= 10000