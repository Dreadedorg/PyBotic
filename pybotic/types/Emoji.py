class Emoji:
	def __new__(cls, obj):
		if obj["id"] == None:
			return obj["name"]
		else:
			return cls
	def __init__(self, obj):
		self.id = obj["id"]
		self.name = obj["name"]
	
		self.roles = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("roles")("roles")
		self.user = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("user")("user")
		self.req_colons = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("require_colons")("require_ colons")
		self.managed = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("managed")("managed")
		self.animated = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("animated")("animated")
		self.available = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("available")("available")
		# lol get pissed off xdddzs

