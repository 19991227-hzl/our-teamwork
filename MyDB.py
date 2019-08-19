import pymysql
class MyDBHelper:
# -*-coding:utf-8 -*-


    def CreateDatabase(self,sql):
            db = pymysql.connect(
                host="localhost",
                port=3306,
                password="200152523",
                user="root",
            )
            cursor = db.cursor()
            cursor.execute(sql)
            print("成功")
            db.close()

    def CreateTable(self,databasename):
            db=pymysql.connect(
                host="localhost",
                port=3306,
                password="200152523",
                user="root",
                db=databasename
            )

    def  addcar(self,args):
                conn = pymysql.connect(
                    host="localhost",
                    port=3306,
                    db="carproject",
                    user="root",
                    password="200152523",
                    charset="utf8"
                     )
                cs=conn.cursor()
                sql="INSERT INTO cardata values (null,%s) "
                row=cs.execute(sql,args)
                conn.commit()
                return row
    def  adduser(self,args):
        # 1.建立连接
        conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            db="carproject",
            user="root",
            password="200152523",
            charset="utf8"
        )
        # 2.创建游标
        cs = conn.cursor()
        # 3.执行sql语句
        print(args)
        row = cs.execute("INSERT INTO userdata  values(null,%s,%s,%s)",args)
        conn.commit()
        return  row

    def delete(self, id):
            try:
                conn = pymysql.connect(
                    host="127.0.0.1",
                    port=3306,
                    db="db",
                    user="root",
                    password="root",
                    charset="utf8"
                )
                cs = conn.cursor()
                row = cs.execute("delete from myuser where uid=%s", [id])
                print(row)
                conn.commit()
            except Exception as e:
                print(e)
            finally:
                if conn is not None:
                    conn.close()