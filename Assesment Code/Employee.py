import sqlite3

con = sqlite3.connect("employee.db")
cursor = con.cursor()

sqlite_query = '''CREATE TABLE employee(
                    empcode INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    phone INTEGER(15) NOT NULL,
                    email TEXT NOT NULL,
                    designation TEXT NOT NULL,
                    salary INTEGER NOT NULL,
                    company_name TEXT NOT NULL);'''

cursor.execute(sqlite_query)

dataList = [(101,'Yash',7350965600,'yash@gmail.com','Software Developer',80000,'Harman'),
            (102,'Piyush',9850908357,'piyush@gmail.com','Software Developer',75000,'Harman'),
            (103,'Mihir',9881796534,'mihir@gmail.com','Software Developer',50000,'Harman'),
            (104,'Savi',9850214568,'savi@gmail.com','Sales',40000,'Harman'),
            (105,'Sakshi',9657485213,'sakshi@gmail.com','Software Developer',65000,'Harman'),
            (106,'Anuj',9654123578,'anuj@gmail.com','Tester',45000,'Harman'),
            (107,'Sooraj',9632587412,'sooraj@gmail.com','Tester',40000,'Harman'),
            (108,'Dheeraj',9147852369,'dheeraj@gmail.com','Sales',30000,'Harman'),
            (109,'Shravani',9665535211,'shravani@gmail.com','Developer',80000,'Harman'),
            (110,'Akash',9655874412,'akash@gmail.com','Developer',65000,'Harman')]

sql_add = "INSERT INTO Employee VALUES(?,?,?,?,?,?,?)"
cursor.executemany(sql_add, dataList)

def viewemp():

    sql_view = "Select * from employee"
    cursor.execute(sql_view)

    records = cursor.fetchall()

    for item in records:
        print(item)

def search():

    name = input("Enter the name you want to search : ")
    sql_search = "Select * from employee where name = ?"
    cursor.execute(sql_search, (name,))

    records = cursor.fetchone()
    print(records)

def update():

    id = int(input("Enter the id you want to update : "))
    sql_search = "Select * from employee where empcode = ?"
    cursor.execute(sql_search, (id,))

    records = cursor.fetchone()
    print(records)

    id = int(input("Enter the Empcode : "))
    name = input("Enter the name you want to update : ")
    phone = int(input("Enter the Phone Number : "))
    email = input("Enter the Email-ID : ")
    sql_update = "UPDATE Employee " \
                 "SET name = ?, phone = ?, email = ? " \
                 "WHERE empcode = ?"
    cursor.execute(sql_update, (name,phone,email, id,))

    viewemp()

def delete():

    id = int(input("Enter the Empcode you want to delete : "))
    sql_delete = "DELETE from Employee where empcode = ?"
    cursor.execute(sql_delete, (id,))

    viewemp()

def display_salary():

    sql_display_salary = "SELECT * from Employee WHERE salary > 50000"
    cursor.execute(sql_display_salary)

    records = cursor.fetchall()

    print("Salary above Rs 50000 are : ")
    for item in records:
        print(item)

def count():

    sql_count = "SELECT COUNT(empcode) FROM Employee "
    cursor.execute(sql_count)

    records = cursor.fetchone()

    for i in records:
        print("Count of employees are : ", i)

def display_alpha():

    sql_display_alpha = "SELECT * from Employee " \
                        "WHERE salary BETWEEN 30000 AND 70000 " \
                        "ORDER BY name "
    cursor.execute(sql_display_alpha)
    records = cursor.fetchall()
    print("Displaying Employee Details in Alphabetical Order and salary range from 30000 to 70000 :  ")
    for item in records:
        print(item)

def displaylessthanaverage():

    sql_average = "SELECT AVG(salary) from Employee"
    cursor.execute(sql_average)
    records = cursor.fetchone()

    for i in records:
        print("Average Salary is : ", i)

    sql_displaylessthanaverage = "SELECT * FROM Employee WHERE salary < (SELECT AVG(salary) from Employee)"
    cursor.execute(sql_displaylessthanaverage)
    records = cursor.fetchall()
    print("Displaying employee data whose salary is less than average salary :  ")
    for item in records:
        print(item)


while(True):
    print('''
        1. View Employees
        2. Search
        3. Update
        4. Delete
        5. Display Salary > 50000
        6. Display Count
        7. Display Employee in Alphabetical order and salary in range 30000 to 70000 
        8. Display salary < average salary
        ''')
    choice = int(input("Enter your choice : "))
    functions = [viewemp,search,update,delete,display_salary,count,display_alpha,displaylessthanaverage]

    a = functions[choice - 1]()
    ch = input("\n Press enter to continue OR press N to discontinue!")
    if(ch=="n" or ch == "N"):
        break
    else:
        pass

