from pybotic.types.Emoji import Emoji

def test():
	examp1 = {"id": 574328959723, "name":"LOLOL"}
	examp2 = {"id": None, "name": "🔥"}
	emoji1 = Emoji(examp1)
	emoji2 = Emoji(examp2)
	assert emoji1.__class__ == Emoji.__class__
	assert emoji2.__class__ == str
