import requests
from datetime import datetime

USER = "wafgh"
TOKEN = "ghk"
url = "https://pixe.la/v1/users"
data = {
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
 }
#step1
# response = requests.post(url=url, json=data)
# print(response.text)

graph_config = {
    "id":"graph1",
    "name":"cycling_graph",
    "unit":"km",
    "type":"float",
    "color":"sora"
}
head = {
    "X-USER-TOKEN": TOKEN
}


#Step2

graph_endpoint = f"{url}/{USER}/graphs"

# res= requests.post(url=graph_endpoint, json=graph_config, headers=head)
# print(res.text)

#Step3

today = datetime.now().date()

data_graph_config = {
    "date":today.strftime("%Y%m%d"),
    "quantity": "11.2",
}
head = {
    "X-USER-TOKEN": TOKEN
}

print(data_graph_config)

data_graph_endpoint = f"{url}/{USER}/graphs/graph1"
#
# data_res = requests.post(url=data_graph_endpoint, json=data_graph_config, headers=head)
# print(data_res.text)

#put

update_end_point = f"{url}/{USER}/graphs/graph1/{today.strftime('%Y%m%d')}"

new_data = {
    "quantity": "4.5"
}

put_res = requests.put(url=update_end_point, json=new_data, headers=head)
print(put_res.text)


#delete


delete_end_point = f"{url}/{USER}/graphs/graph1/{today.strftime('%Y%m%d')}"

put_res = requests.delete(url=update_end_point, headers=head)
print(put_res.text)