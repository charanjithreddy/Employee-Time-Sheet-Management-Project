from flask import Blueprint, render_template, request,session,flash
from routes.db_connect import db_connect
from routes.login_validate import login_validate
from models.user_credentials import user_credentials

home_bp=Blueprint("home_bp",__name__)

@home_bp.route("/home.html",methods=['POST','GET'])
def login():
    from_page = request.args.get("from") or request.form.get("from")
    print("in home_routes: ",from_page)
    if from_page=="employee_login_creation":
        return home_after_employee_login_creation()
    elif(from_page=="login"):
        return home_after_login()
    elif(from_page=="timesheet_entry"):
        return home_after_timesheet_entry()
    else:
        return render_template("login.html")
    
def home_after_timesheet_entry():
    if(request.method=="POST"):
        eid=request.form.get('eid')
        add_date=request.form.get('add_date')
        work_hours=request.form.get('work_hours')
        connection=db_connect().get_connection();
        cursor=connection.cursor();

        query="SELECT EMPLOYEE_ID FROM EMPLOYEE WHERE EMPLOYEE_ID="+str(eid);
        cursor.execute(query);
        
        if(cursor.rowcount==1):
            query="INSERT INTO EMP_TIMESHEET(EMPLOYEE_ID,TS_DATE,WORKED_HOURS,IS_VACATION_Y_N,CREATED_USERID) VALUES(%s,%s,%s,%s,%s)"
            values=(eid,add_date,work_hours,'N',session['user_id'])
            cursor.execute(query,values)
            connection.commit();
            db_connect().close_connection(connection)
            return render_template("home.html");
            
        else:
            flash("Please recheck userid");
            return render_template("timesheet_entry.html");

    else:
        print("wrong method for home after timesheet_entry");
        return render_template("timesheet_entry.html");

def home_after_login():
    if request.method == 'POST':
        un=request.form.get('mail')
        pwd=request.form.get('pwd')
        #print("hi");
        #print(un,"  ",pwd);
        user=user_credentials(un,pwd);
        authenticaton=login_validate().validate_user_credentials(user)
        if(authenticaton):
            session['mailid']=un;
            session['logged_in']=True;
            session['user_id']=1;
            print("seesion created with values  ",session['mailid'],session['logged_in'],session['user_id'])
            return render_template("home.html");
        else:
            flash("Please check username and password",'error');
            return render_template("login.html");
        
    else:
        print("wrong method for home after login");
        return render_template("login.html")

def home_after_employee_login_creation():
    if request.method == 'POST':
        emp_id=request.form.get('emp_id')
        emp_name=request.form.get('emp_name')
        mail=request.form.get('mail')
        dept=request.form.get('dept')
        join_date=request.form.get('join_date')
        connection=db_connect().get_connection();
        cursor1=connection.cursor();
        query1="insert into employee(EMPLOYEE_ID,EMPLOYEE_NAME,DEPT_NAME,JOINING_DATE,CREATED_USERID) values(%s,%s,%s,%s,%s)"
        values1=(emp_id,emp_name,dept,join_date,session['user_id']);

        print(' session user id ',session['user_id']);
        print('curbefore fist',values1);

        cursor1.execute(query1,values1)
        cursor2=connection.cursor();
        query2="insert into USER_CREDENTIALS(EMAIL_ID,PASSWORD,IS_ADMIN_Y_N,CREATED_USERID) values(%s,%s,%s,%s)"
        values2=(mail,emp_id,'N',session['user_id'])
        print('curbefore second ',values2);

        cursor2.execute(query2,values2)
        connection.commit()

        db_connect().close_connection(connection)
        return render_template("home.html")
    else:
        print("Wrong method for home from emp login crtion")
        return render_template("employee_login_creation.html")



