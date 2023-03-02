from pybotic.types.User import User

f = open(".TOKEN")
token = f.read()[:-1]
f.close()

def test_user():
	user = User.get_self(token)
	print(user.username+"#"+str(user.discriminator))
	assert True
