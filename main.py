import requests


# Первая задача
def max_intelligence(hero_list: list):
    max_int = 0
    hero_name = ''
    for hero in hero_list:
        if hero.intelligence > max_int:
            max_int = hero.intelligence
            hero_name = hero.name
    return hero_name + " " + str(max_int)


class SuperHero:

    def __lt__(self, other):
        return self.intelligence < other.intelligence

    def __init__(self, name):
        self.name = name
        self.data = requests.get('https://superheroapi.com/api/2619421814940190/search/' + name).json()
        self.intelligence = int(self.data['results'][0]['powerstats']['intelligence'])


# Вторая задача
class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resourses/upload'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, disk_file_path: str, filename: str):
        href = self._get_upload_link(disk_file_path=disk_file_path).get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()


if __name__ == '__main__':
    # первая задача
    hulk = SuperHero("Hulk")
    captain = SuperHero('Captain America')
    thanos = SuperHero('Thanos')
    print(f'Самый умный супергерой - {max_intelligence([hulk, captain, thanos])}')

    #     Вторая задача
    path_to_file = 'text.txt'
    token = ' '
    uploader = YaUploader(token)
    uploader.upload('netology/text.txt', path_to_file)
