from flask import Blueprint,render_template,session

logout_bp=Blueprint("logout_bp",__name__)

@logout_bp.route("/logout.html",methods=['POST','GET'])
def logout():
    session.clear()
    return render_template("logout.html");