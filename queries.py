import requests


def resolve_user_repos(obj, info, login):
    """
    Resolver for field user_repo. Perform get request to GitHub API to get information about user.
    :param obj: return value of parent resolver.
    :param info: the instance of a GraphQLResolveInfo object specific for this field and query.
    :param login: login of github user.
    :return: Dictionary with parameters {
        success: Boolean,
        errors: List[String]
        user_repo: {
            user: String,
            login: String,
            repos: List[String]
        }
    }
    """
    try:
        user = requests.get(f"https://api.github.com/users/{login}")
        if user.status_code == 200:
            user_json = user.json()
            repos = requests.get(user_json['repos_url'])
            repos_json = repos.json()
            payload = {"success": True,
                       "user_repo": {
                           "user": user_json['name'],
                           "login": user_json["login"],
                           "repos": [repo["name"] for repo in repos_json]
                       }
                       }
        else:
            payload = {"success": False, "errors": ["Error when get user: " + str(user.status_code)]}
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
