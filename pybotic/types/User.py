from pybotic.util import REST as api

class User:
	def __init__(self, obj):
		self.id = obj["id"]
		self.username = obj["username"]
		self.discriminator = obj["discriminator"]
		self.avatar = obj["avatar"]

		self.bot = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("bot")("bot")
		self.system = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("system")("system")
		self.mfa = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("mfa_enabled")("mfa_enabled")
		self.banner = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("banner")("banner")
		self.accent = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("accent_color")("accent_color")
		self.locale = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("locale")("locale")
		self.verified = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("verified")("verified")
		self.email = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("email")
		self.flags = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("flags")
		self.premium = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("premium_type")("premium_type")
		self.public_flags = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("public_flags")("public_flags")
	def get_user(id, token):
		return User(api.GET(f"/users/{id}",None,token))
	def get_self(token):
		return User(api.GET(f"/users/@me",None,token))
	def open_dm(recipient, token):
		return api.POST(f"/users/@me/channels",{"recipient_id": recipient}, token)
