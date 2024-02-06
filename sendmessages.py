import smtplib
#simple mail transfer protocal

#creating a server, because we are 
# sending gmail from a 3rd party application(means not from gmail) 
# so we need a connectin to the server

#gmail service server address, and port number
server = smtplib.SMTP('smtp.gmail.com', 587) 
server.starttls()
server.login('n1@gmail.com','kghv yhei ttgo sqld')

server.sendmail('n1@gmail.com','n2@gmail.com',"We made it oooohhhoo!!")
print("Mail sent successfully")
