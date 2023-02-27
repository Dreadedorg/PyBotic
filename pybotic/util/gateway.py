
import websocket, time, json, threading, random

class Gateway:
	URI = "wss://gateway.discord.gg/?v=10&encoding=json"
	tokenbuffer = None
	interval = None
	heartbeat = None
	evs =  {}
	ws = None
	def __init__(self, intents):
		self.intents = intents
	def connect(self, token):
		self.tokenbuffer = token
		self.ws = websocket.WebSocketApp(self.URI, on_open=self.open,on_message=self.message,on_close=self.close,on_error=self.error)
		self.ws.run_forever()
	def heartbeatfunc(self):
		while True:
			self.ws.send(json.dumps({"op":1,"d":None}))
			wait = self.interval*random.random()
			time.sleep(wait/1000)
	def open(self,ws):
		pass
	def close(self,ws, status, msg):
		print(status, msg)
	def message(self,ws,msg):
		msg = json.loads(msg)
		if msg["op"] == 10:
			self.interval = msg["d"]["heartbeat_interval"]
			self.heartbeat = threading.Thread(target=self.heartbeatfunc,daemon=True)
			self.heartbeat.start()
			ws.send(json.dumps({
				"op": 2,
				"d": {
					"token": self.tokenbuffer,
					"properties": {
						"os": "UDN Systems",
						"browser": "PyBotic ICEFOX AUTOMATION",
						"device": "PyBotic"
					},
					"intents": self.intents
				}
			}))
			del self.tokenbuffer
		elif msg['op'] == 0:
			if msg["t"] in self.evs:
				self.evs[msg["t"]](msg["d"])
	def error(self,ws,err):
		raise err

	def bind(self, eventname, eventfunc):
		self.evs[eventname] = eventfunc
