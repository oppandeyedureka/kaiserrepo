-- SELECT * FROM companydb.dept;

-- Insert into companydb.employees (empid, empname, salary, deptid, emptype, perks, commission, overtime, street, city, pincode) 
-- values(1004, 'Dinesh', 131233, 102, 'Clerk', 0, 0, 123123, 'Borivli', 'Mumbai','2342434');


-- SELECT * FROM companydb.employees;

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

Select * from companydb.dept where deptname in ('HR','SW')