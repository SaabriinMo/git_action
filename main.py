import requests


URL = "https://genshin.jmp.blue/"
HEADER = {'Accept': 'application/json'}
# status_code = requests.get("https://genshin.jmp.blue/", headers={'Accept': 'application/json'})

# print(status_code.json())

def getting_status_code(url):
    return requests.get(url)


def get_genshin_data():
    response = requests.get(URL, headers={'Accept': 'application/json'})
    if response:
        return response.json()
    return None

def get_character_data():
    response = requests.get(URL+"characters", headers={'Accept': 'application/json'})
    if response:
        return response.json()
    return None


if __name__ == "__main__":
    character_data = get_character_data()
    print(character_data)