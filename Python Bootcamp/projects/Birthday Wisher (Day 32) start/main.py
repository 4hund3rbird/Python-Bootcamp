from multiprocessing import connection
import smtplib

my_email="rayanisnotsocool69@gmail.com"
my_password="hahabitch69"
my_yahoo="iamsoocool69@yahoo.com"

connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=my_password)
connection.sendmail(from_addr=my_email,to_addrs=my_yahoo,msg="Helllo world!!!")
connection.close()