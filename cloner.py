import requests
import os
TOKEN = ""
HEADERS = {
    "Authorization": f"token {TOKEN}",
    "AAccept": "application/vnd.github.v3+json",
}
def get_all_repositories():
       repos = []
       page = 1
       while True:
          response = requests.get(f"https://api.github.com/user/repos?page={pag>
          if response.status_code != 200:
              break
          current_repos = response.json()
          if not current_repos:
              break
          repos.extend(current_repos)
          page += 1
       return repos
def clone_repositories(repositories, token):
     for repo in repositories:
        modified_url = repo['clone_url'].replace("https://",f"https://{token}@">
        os.system(f"git clone {modified_url}")
if __name__ == "__main__":
    repositories = get_all_repositories()
    clone_repositories(repositories, TOKEN)
