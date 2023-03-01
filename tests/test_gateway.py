from pybotic.util.gateway import Gateway

f = open(".TOKEN")
token = f.read()[:-1]
f.close()

def test_gateway():
	gateway = Gateway(65277)
	def msg(d):
		print(d)
		if d["content"] == "stop":
			gateway.ws.send("GOOGOGAAGAA")
	gateway.bind("MESSAGE_CREATE",msg)
	gateway.connect(token)
	assert True
