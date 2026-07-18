
from dataclasses import dataclass

@dataclass
class EmployeeAddress:

    employee_dooorno : int
    employee_streetname : str
    employee_city : str
    employee_pincode : int