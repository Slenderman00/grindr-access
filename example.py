from grindr_user import GrindrUser
from xmpp import connect

user = GrindrUser()
mail = input("Email: ")
password = input("Password: ")

user.login(mail, password)
print("------------------- profiles -------------------")
print(user.getProfiles(39.476916, -99.796235))
print("------------------- taps -------------------")
print(user.get_taps())
print("------------------- sessions -------------------")
print(user.sessions(mail))
print("------------------- xmpp -------------------")
connect(user.generate_plain_auth())
