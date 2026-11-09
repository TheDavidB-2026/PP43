# სავარჯიშო 1. პირველ ხაზზევე დამიერორა
# import requests
#
# def get_user(user_id):
#     url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         return response.json()
#     elif response.status_code == 404:
#         return None
#     else:
#         response.raise_for_status()
#
# for uid in [1, 2, 999]:
#     user = get_user(uid)
#     if user:
#         name = user.get("name")
#         email = user.get("email")
#         city = user["address"]["city"]
#         print(f"{name} | {email} | {city}")
#     else:
#         print(f"მომხმარებელი {uid} ვერ მოიძებნა")

#სავარჯიშო 2, ესეც პირველ ხაზზევე დამიერორა
# import requests
#
# def crud_tour():
#     base_url = "https://jsonplaceholder.typicode.com/posts"
#
#     create_res = requests.post(base_url, json={"title": "ახალი პოსტი", "body": "ტექსტი", "userId": 1})
#     new_id = create_res.json().get("id")
#     print(f"CREATE: {create_res.status_code}, id={new_id}")
#
#     read_res = requests.get(f"{base_url}/{new_id}")
#     print(f"READ {new_id}: {read_res.status_code}")
#
#     put_res = requests.put(f"{base_url}/1",
#                            json={"id": 1, "title": "სრულად შეცვლილი", "body": "ახალი ტექსტი", "userId": 1})
#     print(f"UPDATE (PUT): {put_res.status_code}, title={put_res.json().get('title')}")
#
#     patch_res = requests.patch(f"{base_url}/1", json={"title": "ნაწილობრივ შეცვლილი"})
#     print(f"UPDATE (PATCH): {patch_res.status_code}, title={patch_res.json().get('title')}")
#
#     delete_res = requests.delete(f"{base_url}/1")
#     print(f"DELETE: {delete_res.status_code}, {delete_res.json()}")
#
# crud_tour()