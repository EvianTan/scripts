import json
import requests

def queryTitle(substr):
	results = []

	pagenum = 1
	reachLast = False

	while reachLast == False:
		baseurl= "https://jsonmock.hackerrank.com/api/movies/search/?Title="
		url = baseurl+substr+"&page="+str(pagenum)

		response =  requests.get(url)
		infos = json.loads(response.text)
		pages = infos["total_pages"]

		movies = infos["data"]
		length = len(movies)
		for i in range(length):
			if substr in movies[i]["Title"].lower().split():
				results.append(movies[i]["Title"])
		pagenum += 1
		if pagenum == pages+1:
			reachLast = True

	for i in results:
		print i

queryTitle("waterworld")
