import requests


def resolve_user_repos(obj, info, login):
    try:
        user = requests.get(f"https://api.github.com/users/{login}")
        if user.status_code == 200:
            user_json = user.json()
            repos = requests.get(user_json['repos_url'])
            if repos.status_code == 200:
                repos_json = repos.json()
                payload = {"success": True,
                           "user_repo": {
                               "user": user_json['name'],
                               "login": user_json["login"],
                               "repos": [repo["name"] for repo in repos_json]
                           }
                           }
            else:
                payload = {"success": False, "errors": ["Error when get repos: " + str(repos.status_code)]}
        else:
            payload = {"success": False, "errors": ["Error when get user: " + str(user.status_code)]}
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
