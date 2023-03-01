from .Pybotic import REST as rest

class BaseChannel:
	def __init__(self, id, type

class TextChannel(BaseChannel):
	pass

class DMChannel(BaseChannel):
	pass

class VoiceChannel(BaseChannel):
	pass

class GroupChannel(BaseChannel):
	pass

class CategoryChannel(BaseChannel):
	pass

class AnnouncementChannel(BaseChannel):
	pass

class AnnouncementThread(BaseChannel):
	pass

class PublicThread(BaseChannel):
	pass

class PrivateThread(BaseChannel):
	pass

class StageChannel(BaseChannel):
	pass

class ForumChannel(BaseChannel):
	pass

# hub support is gonna be implemented in the near future
