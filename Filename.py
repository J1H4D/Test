username = raw_input("masukkan username : ")
password = raw_input("masukkan password : ")
username_from_db = "J106"
password_from_db = "J1H4D"
if username == username_from_db :
 if password == password_from_db :
    print "Username dan password cocok "
 else:
    print "Password salah "
else:
 print "User tidak terdaftar"