from flask import Blueprint, render_template, request

timesheet_entry_bp=Blueprint("timesheet_entry_bp",__name__)

@timesheet_entry_bp.route("/timesheet_entry.html",methods=['POST','GET'])
def entry():
    return render_template("timesheet_entry.html");