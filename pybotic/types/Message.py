from pybotic.util import REST as api
from pybotic.types.Emoji import Emoji
from pybotic.types.User import User
from urllib.parse import quote as encode

class Message:
	token = ""
	def __init__(self,obj, partial=False):
		self.id = obj["id"]
		self.type = obj["type"] # Maybe also different classes for each type of message
		self.channel_id = obj["channel_id"] # and this too
		self.author = User(obj["author"]) # convert
		self.content = obj["content"]
		self.timestamp = obj["timestamp"]
		self.edited_timestamp = obj["edited_timestamp"]
		self.tts = obj["tts"]
		self.mention_everyone = obj["mention_everyone"]
		self.mentions = obj["mentions"] #convert these aswell
		self.mentions_roles = obj["mention_roles"] # and these
		self.attachments = obj["attachments"] # also these
		self.embeds = obj["embeds"] # and this one
		self.pinned = obj["pinned"]
		
		self.mentions_roles = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("mention_roles")("mention_roles") # gonna trigger all the programmers, convertttttt
		self.nonce = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("nonce")("nonce") # animal abuse
		self.webhook_id = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("webhook_id")("webhook_id")
		self.activity = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("activity")("activity") # the reason why i do it this god awful way
		self.application = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("application")("application") # is cuz i liek 1 line :D, convert btw
		self.application_id = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("application_id")("application_id")
		self.message_reference = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("message_reference")("message_reference") # also has to be converted
		self.interaction = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("interaction")("interaction") # this aswell
		self.thread = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("thread")("thread") # this too
		self.components = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("components")("components") # convert this too
		self.sticker_items = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("sticker_items")("stickeritems") # convert
		self.stickers = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("stickers")("stickers") # co n v e r t
		self.position = (lambda x: {True:(lambda y: obj[y]),False:(lambda z:None)}[x in obj])("position")("position") # convert
		
		self.reactions = None
		if "reactions" in obj:
			self.reactions = {}
			for r in obj["reactions"]:
				self.reactions[r["count"]] = Emoji(r["emoji"])
		# insert converting the arrays hereeee
	def refresh(self):
		self.__init__(api.GET(f"/channels/{self.channel_id}/messages/{self.id}",None,self.token))
	def delete(self):
		api.DELETE(f"/channels/{self.channel_id}/messages/{self.id}",self.token)
		del self
	def edit(self, content, embeds={}, flags=None,files=None,payload=None,attachments=None):
		api.PATCH(f"/channels/{self.channel_id}/messages/{self.id}",{"content": content,"embeds": embeds,"flags": flags,"files": files,"payload_json": payload, "attachments": attachments},self.token)
		self.__init__(api.GET(f"/channels/{self.channel_id}/messages/{self.id}",None,self.token))
	def react(self,emoji):
		api.PUT(f"/channels/{self.channel_id}/messages/{self.id}/reactions/{encode(emoji)}/@me",None,self.token)
	def reply(self, content, embeds={}, files=None, tts=False, payload=None, attachments=None, sticker_ids=[], components=[], flags=None):
		reference = {"message_id": self.id, "channel_id": self.channel_id}
		obj = {
			"content": content,
			"embeds": embeds,
			"files": files,
			"tts": tts,
			"payload_json": payload,
			"attachments": attachments,
			"sticker_ids": sticker_ids,
			"components": components,
			"flags": flags,
			"message_reference": reference
		}
		#print("le refern")
		resp = api.POST(f"/channels/{self.channel_id}/messages",obj,self.token)
		msg = Message(resp)
		msg.token = self.token
		return msg
	def get_reactions(self):
		reactions = {}
		for r in self.reactions:
			reactions[r["count"]] = Emoji(r["emoji"])
		return reactions

