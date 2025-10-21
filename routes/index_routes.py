from flask import Blueprint, render_template, request

index_bp=Blueprint("index_bp",__name__)

@index_bp.route("/",methods=['POST','GET'])
def home():
    return render_template("index.html")