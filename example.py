from grindrUser import grindrUser

user = grindrUser()
mail = input("Email: ")
password = input("Password: ")

user.login(mail, password)
print(user.getProfiles(39.476916, -99.796235))
