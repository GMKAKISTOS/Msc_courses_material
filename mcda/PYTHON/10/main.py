# pandas-new.py
#
# For other python-oracledb DataFrame examples, see https://github.com/oracle/python-oracledb/tree/main/samples

import pyarrow
import oracledb

un = 'hr2'
pw = 'hr2'
cs = 'localhost:1521/freepdb1'

connection = oracledb.connect(user=un, password=pw, dsn=cs)

#-------------------------------------------------------------------------------

sql = """select employee_id, department_id as dept_id, salary
         from employees
         where department_id < :id
         order by department_id"""

# The new, fast way to get a DataFrame
odf = connection.fetch_df_all(
    statement=sql,
    parameters=[80],
    arraysize=1000
)
# Use PyArrow to do zero-copy conversion to our chosen package's DataFrame
df = pyarrow.table(odf).to_pandas()

#-------------------------------------------------------------------------------

print()

# Sum of salaries in each department
#deptsum = df.groupby('DEPT_ID').sum()
deptsum = df.groupby("DEPT_ID").agg(
    EMPLOYEE_COUNT = ("EMPLOYEE_ID", "sum"),
    TOTAL_SALARY = ("SALARY", "sum")
)

print(deptsum)

print()