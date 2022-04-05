from flask import Flask, render_template,request,redirect
import sqlite3

data= sqlite3.connect("Employee.db",check_same_thread=False)
table=data.execute("select name from sqlite_master where type='table' and name='employeedata'").fetchall()
if table !=[]:
    print("table already created")
else:
    data.execute('''create table employeedata(
    ID integer primary key autoincrement,
    EmpCode integer,
    EmpName text,
    Age integer,
    Address text,
    Email text,
    Designation text,
    Salary integer,
    CompanyName text
);''')
    print("table created")


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def Add():
    if request.method=="POST":
        getEmpcode=request.form["EmployeeCode"]
        getEmpname=request.form["EmployeeName"]
        getAge=request.form["Age"]
        getAddress=request.form["Address"]
        getEmail=request.form["Email"]
        getDesignation=request.form["Designation"]
        getSalary=request.form["Salary"]
        getCompanyName=request.form["CompanyName"]
        print(getEmpcode)
        print(getEmpname)
        print(getAge)
        print(getAddress)
        print(getEmail)
        print(getDesignation)
        print(getSalary)
        print(getCompanyName)
        try:
            query = "insert into employeedata(EmpCode,EmpName,Age,Address,Email,Designation,Salary,CompanyName) \
                                    values(" + getEmpcode + ",'" + getEmpname + "'," + getAge + ",'" + getAddress + "','" + getEmail + "','" + getDesignation + "'," + getSalary + ",'"+getCompanyName+"')"
            print(query)
            data.execute(query)
            data.commit()

            print("data added successfully")
        except Exception as err:
            print("error occured", err)



    return render_template("data.html")

@app.route('/search')
def Search():
    return render_template("search.html")

@app.route('/update')
def Update():
    return render_template("update.html")

@app.route('/delete')
def Delete():
    return render_template("delete.html")

@app.route('/viewemp')
def Viewall():
    cursor = data.cursor()
    count = cursor.execute("select * from employeedata")
    result=cursor.fetchall()
    return render_template("viewemp.html",employeedata=result)


if __name__ == "__main__":
    app.run()





