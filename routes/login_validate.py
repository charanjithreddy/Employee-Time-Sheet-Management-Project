import models.user_credentials
from routes.db_connect import db_connect
import mysql.connector
class login_validate():
    def validate_user_credentials(self,user):
        #print(user.mailid,"  ; ",user.pwd);
        connection=db_connect().get_connection();
        cursor=connection.cursor();
        query="SELECT EMAIL_ID FROM USER_CREDENTIALS WHERE EMAIL_ID='"+user.mailid+"' AND PASSWORD='"+user.pwd+"'";
        cursor.execute(query);
        print(query);
        rows=cursor.fetchall();
        print(rows);
        print();
        result=False;
        if(len(rows)>0):
            result=True;

        #cursor.close();
        db_connect().close_connection(connection)
        return result;

    def validate_old_pwd(self,user):
        #print(user.mailid,"  ; ",user.pwd);
        connection=db_connect().get_connection();
        cursor=connection.cursor();
        query="SELECT EMAIL_ID FROM USER_CREDENTIALS WHERE EMAIL_ID='"+user.mailid+"' AND PASSWORD='"+user.old_pwd+"'";
        cursor.execute(query);
        #print(query);
        rows=cursor.fetchall();
        #print(rows);
        #print();
        result=False;
        if(len(rows)>0):
            result=True;
        #cursor.close();
        db_connect().close_connection(connection)
        return result;

    def reset_password(self,user):
        connection=db_connect().get_connection();
        cursor=connection.cursor();
        query="UPDATE USER_CREDENTIALS SET PASSWORD='"+user.pwd+"' WHERE EMAIL_ID='"+user.mailid+"'"
        cursor.execute(query);
        print(query);
        print(cursor.rowcount)
        print();
        res=False;
        
        if(cursor.rowcount>0):
            res=True;
            connection.commit()
        db_connect().close_connection(connection)
        return res;