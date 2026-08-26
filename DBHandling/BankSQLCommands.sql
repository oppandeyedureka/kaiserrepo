-- Create Customer Records
-- Insert into bankingdb.customers (customerid, customername, street, city, pincode) 
-- values (101,'Ganesh', 'Hinjewadi', 'Pune', 400068);
-- Insert into bankingdb.customers (customerid, customername, street, city, pincode) 
-- values (102,'Mahesh', 'Hinjewadi', 'Pune', 400068);
-- Insert into bankingdb.customers (customerid, customername, street, city, pincode) 
-- values (103,'Dinesh', 'Borivli', 'Mumbai', 400068);

-- Create Account Records
Insert into bankingdb.accounts (accountid, customerid, balance, accountype, minbal, overdraft) 
values (1006,102, 12356.56, 'Current', 1234, 0);

Insert into bankingdb.accounts (accountid, customerid, balance, accountype, minbal, overdraft) 
values (1005,102, 123456.56, 'Current', 0,1234.45);

select * from bankingdb.customers;

select * from bankingdb.accounts;

-- Self transfer - Cust 101
Insert into bankingdb.transactions (custid, accountid, transtype, amount, transdate)
values (101, 1001, 'Debit', 10000, '2026-08-25');

Insert into bankingdb.transactions (custid, accountid, transtype, amount, transdate)
values (101, 1002, 'Credit', 10000, '2026-08-25');

Select customerid, count(*) as totalaccts, sum(balance) as custbalance 
from bankingdb.accounts group by customerid;

Select cust.customername as Name, sum(acc.balance) as CustBalance, 
count(*) as TotalAccts
from bankingdb.customers as cust
join bankingdb.accounts as acc
on cust.customerid = acc.customerid
group by acc.customerid;

Select * from bankingdb.transactions;

Select cust.customername, trans.accountid, trans.transtype, 
trans.amount, trans.transdate
from bankingdb.customers as cust
join bankingdb.transactions as trans
on cust.customerid = trans.custid; 

Select max(accountid) from bankingdb.accounts;


Select * from bankingdb.accounts;

-- Windowing Functions
-- SELECT accountid, AVG(balance) AS Avg_Salary FROM bankingdb.accounts; -- Error no group by

SELECT accountid, balance, AVG(balance) OVER (PARTITION BY customerid) AS AVG_BAL FROM bankingdb.accounts;

SELECT empname, deptid, salary,
       RANK() OVER(PARTITION BY deptid ORDER BY salary DESC) AS emp_rank
FROM companydb.employees;

SELECT empname, deptid, salary,
       DENSE_RANK() OVER(PARTITION BY deptid ORDER BY salary DESC) AS emp_dense_rank
FROM companydb.employees;

SELECT empname, deptid, salary,
       percent_rank() OVER(PARTITION BY deptid ORDER BY salary DESC) AS emp_dense_rank
FROM companydb.employees;

SELECT empname, deptid, salary,
       row_number() OVER(PARTITION BY deptid ORDER BY salary DESC) AS emp_rowno
FROM companydb.employees;

SELECT empname, deptid, salary,
  SUM(salary) OVER () as total_salary FROM companydb.employees;