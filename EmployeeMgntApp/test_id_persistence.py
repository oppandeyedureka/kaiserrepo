import os
import pickle
import sys
import tempfile
import unittest
from unittest.mock import patch

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MODULE_DIR)

import Department
import EmployeeMgntApp


class IdPersistenceTests(unittest.TestCase):
    def test_counters_restart_from_saved_ids(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            data_file = os.path.join(temp_dir, "EmpMgntDetails.dat")
            with patch.object(EmployeeMgntApp, "__file__", os.path.join(temp_dir, "EmployeeMgntApp.py")), \
                 patch.object(Department, "__file__", os.path.join(temp_dir, "Department.py")):
                dept = Department.Department("Sales", "Pune")
                emp = EmployeeMgntApp.Manager("Mgr01", 1000, dept, 100)
                dept.setEmployees({emp})
                with open(data_file, "wb") as file:
                    pickle.dump({dept}, file)

                EmployeeMgntApp.Employee.IDGenerator = 1000
                Department.Department.deptcount = 100

                EmployeeMgntApp.initialize_emp_id_generator()
                Department.initialize_dept_counter()

                self.assertEqual(Department.Department.deptcount, 101)
                self.assertEqual(EmployeeMgntApp.Employee.IDGenerator, 1001)


if __name__ == "__main__":
    unittest.main()
