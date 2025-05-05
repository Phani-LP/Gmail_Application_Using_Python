class PythonGmail:
    def __init__(self):
        self.senderEmail = input("sender mail: ")
        self.receiverEmail = input("receiver mail: ")# add no.of receiptents
        self.subject = input("Subject: ")
        self.text = input("Message: ")
        self.message = f"{self.subject}\n\n{self.text}"
    def sendmessage(self):
        try:
            import smtplib
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(self.senderEmail, 'kghv ilil rsta zbcd')
            server.sendmail(self.senderEmail, self.receiverEmail, self.message)
            return "Message sent successfully."
        except Exception as e:
            print("Error: ",e)      
    def attachFiles(self):
        pass
    def encryptionPhase(self):
        pass
obj1 = PythonGmail()
print(obj1.sendmessage())
print(obj1.sendmessage())
