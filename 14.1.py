import sqlite3

db = sqlite3.connect('lesson.db')

c = db.cursor()

c.execute("""CREATE TABLE Employees (
   Name VARCHAR(100),
   Position VARCHAR(100),
   Department VARCHAR(100),
   Salary DECIMAL(10, 2)
); """)

c.execute("""
INSERT INTO Employees (Name, Position, Department, Salary) VALUES
('John Doe', 'Software Engineer', 'IT', 6000),
('Jane Smith', 'Manager', 'HR', 7500),
('Alice Johnson', 'Sales Representative', 'Sales', 4500),
('Bob Brown', 'Marketing Coordinator', 'Marketing', 5000),
('Charlie Davis', 'Manager', 'Sales', 8000);
""")

c.execute("""
UPDATE Employees
SET Position = 'Senior Software Engineer'
WHERE Name = 'John Doe';
""")

c.execute("""
ALTER TABLE Employees
ADD HireDate DATE;
""")

c.execute("""
UPDATE Employees
SET HireDate = '2020-01-15' WHERE Name = 'John Doe';

UPDATE Employees
SET HireDate = '2019-03-22' WHERE Name = 'Jane Smith';

UPDATE Employees
SET HireDate = '2021-06-30' WHERE Name = 'Alice Johnson';

UPDATE Employees
SET HireDate = '2022-02-15' WHERE Name = 'Bob Brown';

UPDATE Employees
SET HireDate = '2018-09-01' WHERE Name = 'Charlie Davis';
""")

print("Managers:")
c.execute("SELECT * FROM Employees WHERE Position = 'Manager'")
print(c.fetchall())

print("\nEmployees with salary > 5000:")
c.execute("SELECT * FROM Employees WHERE Salary > 5000")
print(c.fetchall())

print("\nSales Employees:")
c.execute("SELECT * FROM Employees WHERE Department = 'Sales'")
print(c.fetchall())

print("\nAverage Salary:")
c.execute("SELECT AVG(Salary) AS AverageSalary FROM Employees")
average_salary = c.fetchone()
print(average_salary)

print("\nAll Employees:")
c.execute("SELECT * FROM Employees")
print(c.fetchall())

c.execute("DROP TABLE Employees")
db.commit()

db.close()