import requests

PATH = "https://discord.com/api/v10"

def GET(path, data, token, headers={}):
	headers = {"Authorization":"Bot "+token,**headers}
	path = PATH+path
	return requests.get(path,json=data,headers=headers).json()

def POST(path, data, token, headers={}):
	headers = {"Authorization":"Bot "+token,**headers}
	path = PATH+path
	return requests.post(path,json=data,headers=headers).json()

def DELETE(path, token, headers={}):
	headers = {"Authorization":"Bot "+token,**headers}
	path = PATH+path
	requests.delete(path,headers=headers)

def PATCH(path, data, token, headers={}):
	headers = {"Authorization":"Bot "+token,**headers}
	path = PATH+path
	requests.patch(path,json=data,headers=headers).json()

def PUT(path, data, token, headers={}):
	headers = {"Authorization":"Bot "+token,**headers}
	path = PATH+path
	requests.put(path, json=data,headers=headers)
