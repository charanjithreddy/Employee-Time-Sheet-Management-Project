#initial code written in app.py before adding blueprints

"""
@app.route("/")
def home():
    return render_template("index.html")  # your form page

@app.route("/login.html", methods=['POST','GET'])
def submit():
    #print("Entered login.html");
    return render_template("login.html")

@app.route("/home.html",methods=['POST','GET'])
def login():
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
            return render_template("home.html");
        else:
            flash("Please check username and password",'error');
            return render_template("login.html");
        
    else:
        #print("wrong method");
        return render_template("login.html")

@app.route("/timesheet_entry.html",methods=['POST','GET'])
def entry():
    return render_template("timesheet_entry.html");

@app.route("/employee_login_creation.html",methods=['POST','GET'])
def create_employee():
    return render_template("employee_login_creation.html");

@app.route("/password_reset.html",methods=['POST','GET'])
def password_reset():
    return render_template("password_reset.html");

@app.route("/logout.html",methods=['POST','GET'])
def logout():
    session.clear()
    return render_template("logout.html");

@app.route("/password_reset_success.html",methods=['POST','GET'])
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
"""