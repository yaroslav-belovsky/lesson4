import requests

respons = requests.get("https://rickandmortyapi.com/api/character")
print(respons)
print("")
print("")
answer = respons.json()
for i in range(20):
    print(answer["results"][i]["name"])
    print(answer["results"][i]["species"])
    print(answer["results"][i]["status"])
print(answer)