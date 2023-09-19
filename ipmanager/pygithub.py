import requests

# 替换为你的 GitHub 用户名和访问令牌
username = "yefengwu"
access_token = "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"

# 获取仓库列表
def get_repos():
    url = f"https://api.github.com/users/{username}/repos"
    headers = {"Authorization": f"Token {access_token}"}
    response = requests.get(url, headers=headers)
    repos = response.json()
    return repos

# 删除仓库
def delete_repo(repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    headers = {"Authorization": f"Token {access_token}"}
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Deleted {repo_name} successfully.")
    elif response.status_code == 403:
        print(f"Permission denied to delete {repo_name}. Please check your access token permissions.")
    else:
        print(f"Failed to delete {repo_name}.")

# 列出所有仓库名
def list_repos():
    repos = get_repos()
    for repo in repos:
        print(repo["name"])

# 删除指定的仓库列表
def delete_repos(repos_to_delete):
    for repo_name in repos_to_delete:
        delete_repo(repo_name)

# 列出所有仓库名
list_repos()

# 输入要删除的仓库列表
repos_to_delete = input("Enter the repositories to delete (separated by comma): ").split(" ")

# 删除指定的仓库列表
delete_repos([repo.strip() for repo in repos_to_delete])
