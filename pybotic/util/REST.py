import requests

PATH = "https://discord.com/api/v10"

def GET(path, data, token, headers={}):
	headers = {"token":token,**headers}
	path = PATH+path
	return requests.get(path,json=data,headers=headers).json()

def POST(path, data, token, headers={}):
	headers = {"token":token,**headers}
	path = PATH+path
	return requests.post(path,json=data,headers=headers).json()

