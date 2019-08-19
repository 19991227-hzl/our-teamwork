# -*- coding: UTF-8 -*-
from flask import Flask,render_template,request,flash,send_file
from MyDB import MyDBHelper
import os
app = Flask(__name__)

@app.route("/")
def show():
    return render_template( "Index.html")

@app.route('/create')
def create():
    db = MyDBHelper()
    #只执行一次
    #db.CreateDatabase("create database carproject")
    db.add(["车牌号"])
    db.add(["京B"])
   # print("影响的行数", row)
@app.route('/Register') #页面链接该路由名称
def f_register():
    return render_template("register.html")
@app.route('/login') #页面链接该路由名称
def f_login():
    return render_template("login.html")

@app.route("/doregister")
def doregister():
   name = request.args.get("uname")
   pwd = request.args.get("upwd")
   sex=request.args.get("title")
   print(name,pwd,sex)
   db = MyDBHelper()
   args=[name,pwd,sex]
   row =db.adduser(args)
   print("影响的行数",row)
   if row>0:
       allUser=((1,"tom"),(2,"jack"))
       return render_template("Index.html", u=name, all=allUser)
   else:
       flash("register fail")
       return  render_template("register.html")
# @app.route("/doregister")
# def doregister():
#    name = request.args.get("uname")
#    pwd = request.args.get("upwd")
#    sex=request.args.get("sex")
#    print(name,pwd,sex)
#    db = MyDBHelper()
#    args=[name,pwd,sex]
#    row =db.adduser(args)
#    print("影响的行数",row)
#    if row>0:
#        allUser=((1,"tom"),(2,"jack"))
#        return render_template("index.html", u=name, all=allUser)
#    else:
#        flash("register fail")
#        return  render_template("register.html")

if __name__ == '__main__':
    app.run()
