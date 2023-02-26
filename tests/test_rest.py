from pybotic.util import REST as rest
from urllib.parse import quote
import time

f = open(".TOKEN")
TOKEN = f.read()[:-1]
f.close()

def test():
	id = rest.POST("/channels/1079354145577893938/messages",{"content":"test!"},TOKEN)['id']
	rest.PUT(f"/channels/1079354145577893938/messages/{id}/reactions/{quote('🔥')}/@me",None,TOKEN)
	print(rest.GET("f/channels/1079354145577893938/messages/{id}",None,TOKEN))
	time.sleep(2)
	rest.PATCH(f"/channels/1079354145577893938/messages/{id}",{"content": "test! (edited)"},TOKEN)
	time.sleep(5)
	rest.DELETE(f"/channels/1079354145577893938/messages/{id}",TOKEN)
	assert True
