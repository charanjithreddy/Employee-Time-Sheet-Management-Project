from flask import Blueprint, render_template, request,flash
from routes.db_connect import db_connect

timesheet_entry_bp=Blueprint("timesheet_entry_bp",__name__)

@timesheet_entry_bp.route("/timesheet_entry.html",methods=['POST','GET'])
def entry():
    from_page = request.args.get("from") or request.form.get("from")
    print("in timesheet_entry_routes: ",from_page)
    if(from_page=="timesheet_entry"):
        return retrieve_timesheet()
    else:
        return render_template("timesheet_entry.html")

def retrieve_timesheet():
    if(request.method=="POST"):
        emp_id=request.form.get('emp_id')
        from_date=request.form.get('from_date')
        to_date=request.form.get('to_date');
        connection=db_connect().get_connection();
        cursor=connection.cursor();
        query=" SELECT e.EMPLOYEE_NAME, t.TS_DATE, t.WORKED_HOURS, t.IS_VACATION_Y_N FROM EMP_TIMESHEET t JOIN EMPLOYEE e ON t.EMPLOYEE_ID = e.ID WHERE e.EMPLOYEE_ID = %s AND t.TS_DATE BETWEEN %s AND %s ORDER BY t.TS_DATE"
        values=(emp_id, from_date, to_date)
        cursor.execute(query,values)
        records=cursor.fetchall();
        db_connect().close_connection(connection)
        if(not records):
            flash("No timesheet records found for given dates.", "info");
            return render_template("timesheet_entry.html");
        else:
            return render_template("timesheet_entry.html", records=records, emp_id=emp_id, from_date=from_date, to_date=to_date)
        
    else:
        return render_template("timesheet_entry.html");