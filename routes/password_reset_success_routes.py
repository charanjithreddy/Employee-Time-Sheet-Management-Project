from flask import Blueprint,render_template, request,flash,session
from models.user_credentials import user_credentials
from routes.login_validate import login_validate

password_reset_succes_bp=Blueprint("password_reset_success_bp",__name__)

@password_reset_succes_bp.route("/password_reset_success.html",methods=['POST','GET'])
def successful_pwd_reset():
    old_pwd=request.form.get('old_pwd')
    new_pwd=request.form.get('new_pwd')
    re_enter_pwd=request.form.get('re_enter_pwd')
    

    user=user_credentials(session['mailid'],new_pwd,old_pwd);
    is_old_pwd_right=login_validate().validate_old_pwd(user);
    if(is_old_pwd_right):
        if(new_pwd==re_enter_pwd):
            reset_pwd_status=login_validate().reset_password(user);

            if(reset_pwd_status):
                return render_template("password_reset_success.html");
            else:
                flash("Please try resetting again");
                return render_template("password_reset.html");
        else:
            flash("New password and confirm password must be the same.",'error');
            return render_template("password_reset.html");
    else:
        flash("Please enter the correct password",'error');
        return render_template("password_reset.html");