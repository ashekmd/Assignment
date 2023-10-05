post_data = [
{
"userId": "Alex Gates",
"id": 1,
"title": " sunt aut facere repellat provident",
"body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
},
{
"userId": "Alex Gates",
"id": 2,
"title": " qui est esse ",
"body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
},
{
"userId": "Alex Gates",
"id": 3,
"title": " ea molestias quasi exercitationem ",
"body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
},
{
"userId": "Alex Gates",
"id": 4,
"title": " eum et est occaecati ",
"body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
},
{
"userId": "Alex Gates",
"id": 5,
"title": " nesciunt quas odio",
"body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque"
}]

def pd_url(string):
    stripped_string = string.rstrip()
    lower_case = stripped_string.lower()
    url = lower_case.replace(' ','-')
    return url

if "slug" not in post_data[0]:
    post_data[0]["slug"] = pd_url(str(post_data[0]['title']))
if "slug" not in post_data[1]:
    post_data[1]["slug"] = pd_url(str(post_data[1]['title']))
if "slug" not in post_data[2]:
    post_data[2]["slug"] = pd_url(str(post_data[2]['title']))
if "slug" not in post_data[3]:
    post_data[3]["slug"] = pd_url(str(post_data[3]['title']))
if "slug" not in post_data[4]:
    post_data[4]["slug"] = pd_url(str(post_data[4]['title']))


i = 0
while i < len(post_data):
    print(post_data[i])
    i = i + 1

print('\n')

for data in post_data:
    print(data)

