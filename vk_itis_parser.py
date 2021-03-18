import vk_api

with open("data/acc.txt", "r") as file:
    login = str(file.readline()).rstrip()
    password = str(file.readline()).rstrip()

vk_session = vk_api.VkApi(login, password)
vk_session.auth()

vk = vk_session.get_api()


def write_to_file(posts):
    with open("data/output_with_repost.txt", "a", encoding='utf-8') as file:
        for post in posts['items']:
            file.write(post["text"])
            try:
                for copy_post in post['copy_history']:
                    file.write(copy_post['text'])
            except Exception:
                continue
            finally:
                file.write("\n ---- ---- \n")


posts100 = vk.wall.get(owner_id="-35488145", filter="owner", count=100, offset=0)
posts200 = vk.wall.get(owner_id="-35488145", filter="owner", count=100, offset=100)

write_to_file(posts100)
write_to_file(posts200)