-- SELECT * FROM companydb.dept;

Insert into companydb.employees (empid, empname, salary, deptid, emptype, perks, commission, overtime, street, city, pincode) 
values(1008, 'Devesh', 131233, 103, 'Clerk', 0, 0, 123123, 'Wakad', 'Pune','2342434');


SELECT * FROM companydb.employees;

-- Select empid, empname, salary from companydb.employees;

-- Select empid, empname, deptid from companydb.employees where deptid=101;

-- Select empid, empname, deptid from companydb.employees where deptid=101 and empid>1001;

-- Update companydb.employees Set salary = 565566 where empid=1001;

-- Select empid, empname, salary from companydb.employees order by salary asc;

-- Select deptid, sum(salary) as deptsal from companydb.employees 
-- group by deptid order by deptsal desc;

-- Select deptid, sum(salary) as deptsal from companydb.employees 
-- group by deptid having deptsal > 131500

-- Select distinct city, street from companydb.employees order by city; 
Select empname from companydb.employees where empname like 'D%';

Select * from companydb.dept where deptname in ('HR','SW');


Select empid, empname, salary, deptid, avg(salary) 
over(partition by deptid) as total_compsal 
from companydb.employees;

Select cust.customername, acc.accountid, acc.accountype, acc.balance, sum(acc.balance)
over(partition by acc.customerid order by acc.accountid) as custbal
from bankingdb.accounts as acc
join bankingdb.customers as cust
on acc.customerid = cust.customerid;

Select customerid, accountid, accountype, balance,
rank() over(order by balance desc) as custrank
from bankingdb.accounts;

Select customerid, accountid, accountype, balance,
dense_rank() over(order by balance desc) as custdenserank
from bankingdb.accounts;

Select customerid, accountid, accountype, balance,
row_number() over(order by balance desc) as rownumber
from bankingdb.accounts;
