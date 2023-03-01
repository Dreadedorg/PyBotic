from pybotic.types.Message import Message
from pybotic.util import REST as api
from time import sleep

f = open(".TOKEN")
token = f.read()[:-1]
f.close()

def test():
	msg = Message(api.POST("/channels/1079354145577893938/messages",{"content": "test number 2!!!"}, token))
	msg.token = token
	msg.edit("test number 2.1!!!")
	r = msg.reply("React!!!")
	sleep(3)
	r.delete()
	msg.react("🔥")
	#assert False
