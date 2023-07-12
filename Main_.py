import requests
from datetime import datetime


PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_param={
    "token":"alhamdulillah",
    "username":"jawadsaleem",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}


# response = requests.post(PIXELA_ENDPOINT,json=user_param)
# print(response)
# print(response)
# print(response.text)

#Creating a Graph Endpoint

graph_endpoint = f"{PIXELA_ENDPOINT}/jawadsaleem/graphs/graph1"

graph_config = {
    "id":"graph1",
    "name":"Swimming Graph",
    "unit":"m",
    "type":"float",
    "color":"ajisai",
}

headers = {
    "X-USER-TOKEN":"alhamdulillah"
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)


#Posting a Pixel


pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/mohammedjawad/graphs/"

today = datetime.now()
print(today.strftime("%Y%m%d"))

pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"15200",
}
# response = requests.post(f"{PIXELA_ENDPOINT}/jawadsaleem/graphs/usual", json=pixel_data, headers=headers)

#Put

#Yesterday I Didnt Swim so make it to 0

updateData = {
    "quantity":"0"
}


# pixelUpdate = f"{PIXELA_ENDPOINT}/jawadsaleem/graphs/usual/20230630"
#
# response = requests.put(pixelUpdate,json=updateData,headers=headers)
# print(response.text)


# response = requests.post(f"{PIXELA_ENDPOINT}/jawadsaleem/graphs/usual",json=pixel_data,headers=headers)
# print(response.status_code)


pixelDelete = f"{PIXELA_ENDPOINT}/jawadsaleem/graphs/usual/20230712"

response = requests.delete(pixelDelete,json=updateData,headers=headers)
print(response.text)