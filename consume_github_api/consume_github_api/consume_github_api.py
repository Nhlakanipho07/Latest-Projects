import requests
import os
from datetime import datetime, date
from dotenv import load_dotenv


params = {
    "state": "all",
    "sort": "created",
    "direction": "asc",
    "per_page": 100,
    "page": 1,
}

base_url = "https://api.github.com"


def validate_string(value):
    if not isinstance(value, str):
        raise TypeError(f"{value} must be a string")


def validate_date(date):
    datetime.strptime(date, "%Y-%m-%d")


def get_auth_headers(token_env_var):
    load_dotenv()
    github_token = os.getenv(token_env_var)

    if not github_token:
        raise ValueError(f"No {token_env_var} found in environment variables.")
    return {"Authorization": f"token {github_token}"}


def get_request(url):
    return requests.get(
        url,
        headers=get_auth_headers("GITHUB_TOKEN"),
        params=params,
    )


def check_owner_exists(owner):
    response = get_request(f"{base_url}/users/{owner}")

    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        raise ValueError(f"Repository owner {owner} not found")


def check_repo_exists(owner, repository_name):
    response = get_request(f"{base_url}/repos/{owner}/{repository_name}")

    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        raise ValueError(
            f"The repository {repository_name} owned by {owner} does not exist"
        )


def convert_to_date(date_string):
    if "T" in date_string:
        return datetime.strptime(
            date_string[: date_string.index("T")], "%Y-%m-%d"
        ).date()
    else:
        return datetime.strptime(date_string, "%Y-%m-%d").date()


def filter_pull_requests(start_date, end_date, pull_requests, filtered_pull_requests):

    for pr in pull_requests:
        if start_date <= convert_to_date(pr["created_at"]) <= end_date:
            filtered_pull_requests.append(pr)
        elif (
            pr["updated_at"]
            and start_date <= convert_to_date(pr["updated_at"]) <= end_date
        ):
            filtered_pull_requests.append(pr)
        elif (
            pr["closed_at"]
            and start_date <= convert_to_date(pr["closed_at"]) <= end_date
        ):
            filtered_pull_requests.append(pr)
        elif (
            pr["merged_at"]
            and start_date <= convert_to_date(pr["merged_at"]) <= end_date
        ):
            filtered_pull_requests.append(pr)


def customize_pull_requests(filtered_pull_requests):
    custom_pull_requests = []
    filtered_pull_requests.reverse()

    for pr in filtered_pull_requests:
        custom_pr = {}
        for key in ["id", "user", "title", "state", "created_at"]:
            if key == "user":
                custom_pr[key] = pr[key]["login"]
            elif key == "created_at":
                custom_pr[key] = pr[key][: pr[key].index("T")]
            else:
                custom_pr[key] = pr[key]
        custom_pull_requests.append(custom_pr)
    return custom_pull_requests


def get_pull_requests(owner, repo, start_date, end_date):

    for argument in [owner, repo, start_date, end_date]:
        validate_string(argument)

    for date_ in [start_date, end_date]:
        validate_date(date_)

    check_owner_exists(owner)
    check_repo_exists(owner, repo)
    start_date = convert_to_date(start_date)
    end_date = convert_to_date(end_date)
    pr_date_limit = date.min
    filtered_pull_requests = []

    while pr_date_limit < end_date:
        pull_requests = get_request(f"{base_url}/repos/{owner}/{repo}/pulls").json()

        if pull_requests:
            filter_pull_requests(
                start_date, end_date, pull_requests, filtered_pull_requests
            )
            pr_date_limit = convert_to_date(pull_requests[0]["created_at"])
            params["page"] += 1

        else:
            return pull_requests
    return customize_pull_requests(filtered_pull_requests)
