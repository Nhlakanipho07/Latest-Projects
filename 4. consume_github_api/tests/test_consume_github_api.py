import os
import unittest
from datetime import datetime, date
from unittest.mock import patch, Mock


from consume_github_api.consume_github_api import (
    validate_string,
    validate_date,
    get_auth_headers,
    get_request,
    check_owner_exists,
    check_repo_exists,
    convert_to_date,
    filter_pull_requests,
    customize_pull_requests,
    get_pull_requests,
)


class TestConsumeGithubAPI(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.base_url = "https://api.github.com"
        self.headers = {"Authorization": f"token {os.getenv('GITHUB_TOKEN')}"}
        self.params = {
            "state": "all",
            "sort": "created",
            "direction": "asc",
            "per_page": 100,
            "page": 1,
        }

    def test_validate_string(self):
        invalid_string = 123
        with self.assertRaises(TypeError) as error_msg:
            validate_string(invalid_string)
        self.assertEqual(str(error_msg.exception), "123 must be a string")

    def test_validate_date(self):
        invalid_date = "invalid-date"
        with self.assertRaises(ValueError) as error_msg:
            validate_date(invalid_date)
        self.assertEqual(
            str(error_msg.exception),
            "time data 'invalid-date' does not match format '%Y-%m-%d'",
        )

    @patch("consume_github_api.consume_github_api.os.getenv")
    def test_get_auth_headers_with_token(self, mock_getenv):
        mock_getenv.return_value = "fake_token"
        headers = get_auth_headers("fake_token")
        mock_getenv.assert_called_with("fake_token")
        self.assertEqual(headers, {"Authorization": "token fake_token"})

    @patch("consume_github_api.consume_github_api.os.getenv")
    def test_get_auth_headers_without_token(self, mock_getenv):
        mock_getenv.return_value = None
        with self.assertRaises(ValueError) as error_msg:
            get_auth_headers("GITHUB_TOKEN")
        self.assertEqual(
            str(error_msg.exception), "No GITHUB_TOKEN found in environment variables."
        )

    @patch("consume_github_api.consume_github_api.requests.get")
    def test_get_request(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        with patch.dict(
            "consume_github_api.consume_github_api.params",
            self.params,
            clear=True,
        ):
            user_data = get_request(self.base_url)

            mock_get.assert_called_with(
                self.base_url,
                headers=self.headers,
                params=self.params,
            )
            self.assertEqual(user_data.status_code, 200)

    @patch("consume_github_api.consume_github_api.get_request")
    def test_check_owner_exists(self, mock_get_request):
        mock_get_request.return_value.status_code = 200
        self.assertTrue(check_owner_exists("owner"))

        mock_get_request.return_value.status_code = 404
        with self.assertRaises(ValueError) as error_msg:
            check_owner_exists("owner")
        self.assertEqual(str(error_msg.exception), "Repository owner owner not found")

    @patch("consume_github_api.consume_github_api.get_request")
    def test_check_repo_exists(self, mock_get_request):
        mock_get_request.return_value.status_code = 200
        self.assertTrue(check_repo_exists("owner", "repo"))

        mock_get_request.return_value.status_code = 404
        with self.assertRaises(ValueError) as error_msg:
            check_repo_exists("owner", "repo")
        self.assertEqual(
            str(error_msg.exception),
            "The repository repo owned by owner does not exist",
        )

    def test_convert_to_date(self):
        date_string = "2023-01-01T00:00:00Z"
        self.assertEqual(str(convert_to_date(date_string)), "2023-01-01")
        date_string = "2023-01-01"
        self.assertEqual(str(convert_to_date(date_string)), "2023-01-01")

    def test_filter_pull_requests(self):
        start_date = datetime.strptime("2023-01-01", "%Y-%m-%d").date()
        end_date = datetime.strptime("2023-12-31", "%Y-%m-%d").date()
        pull_requests = [
            {
                "created_at": "2023-01-01T00:00:00Z",
                "updated_at": None,
                "closed_at": None,
                "merged_at": None,
            },
            {
                "created_at": "2022-01-01T00:00:00Z",
                "updated_at": None,
                "closed_at": "2022-01-11T00:00:00Z",
                "merged_at": "2022-01-11T00:00:00Z",
            },
            {
                "created_at": "2020-10-06T11:10:08Z",
                "updated_at": "2020-10-10T13:07:27Z",
                "closed_at": "2020-10-08T12:27:24Z",
                "merged_at": "2020-10-08T12:27:24Z",
            },
        ]
        filtered_pull_requests = []
        filter_pull_requests(
            start_date, end_date, pull_requests, filtered_pull_requests
        )
        self.assertEqual(len(filtered_pull_requests), 1)

    def test_customize_pull_requests(self):
        filtered_pull_request = [
            {
                "url": "https://api.github.com/repos/Umuzi-org/ACN-syllabus/pulls/26",
                "id": 498457149,
                "node_id": "MDExOlB1bGxSZXF1ZXN0NDk4NDU3MTQ5",
                "issue_url": "https://api.github.com/repos/Umuzi-org/ACN-syllabus/issues/26",
                "number": 26,
                "state": "closed",
                "locked": False,
                "title": "agile recap workshop deleted",
                "user": {
                    "login": "Babalwa01",
                    "id": 52567054,
                    "node_id": "MDQ6VXNlcjUyNTY3MDU0",
                    "type": "User",
                    "user_view_type": "public",
                    "site_admin": False,
                },
                "body": "Related issues: [please specify]\r\n\r\n## Description:\r\n\r\nWhat are you up to? Fill us in :)\r\n\r\n## I solemnly swear that:\r\n\r\n- [x] I ran the hugo server and looked at my changed in the browser with my own eyes\r\n- [x] I ran the linter and there were no errors\r\n- [x] My code follows the style guidelines of this project\r\n- [x] I have performed a self-review of my own code\r\n",
                "created_at": "2020-10-06T11:10:08Z",
                "updated_at": "2020-10-10T13:07:27Z",
                "closed_at": "2020-10-08T12:27:24Z",
                "merged_at": "2020-10-08T12:27:24Z",
            }
        ]

        custom_pull_request = customize_pull_requests(filtered_pull_request)
        excepted_custom_pull_request = [
            {
                "id": 498457149,
                "user": "Babalwa01",
                "title": "agile recap workshop deleted",
                "state": "closed",
                "created_at": "2020-10-06",
            }
        ]
        self.assertEqual(custom_pull_request, excepted_custom_pull_request)

    @patch("consume_github_api.consume_github_api.get_request")
    def test_get_pull_requests(self, mock_get_request):
        mock_get_request.return_value.status_code = 200
        mock_get_request.return_value.json.return_value = [
            {
                "id": 876359209,
                "user": {"login": "FaithMo"},
                "title": "added data sci and eng info",
                "state": "closed",
                "created_at": "2022-03-10T00:00:00Z",
                "updated_at": "2022-03-15T00:00:00Z",
                "closed_at": "2022-03-12T00:00:00Z",
                "merged_at": "2022-03-12T00:00:00Z",
            },
            {
                "id": 874927260,
                "user": {"login": "Ryan-oc"},
                "title": "update sololearn python and all contentlinks etc",
                "state": "closed",
                "created_at": "2022-03-09T00:00:00Z",
                "updated_at": "2022-03-08T00:00:00Z",
                "closed_at": "2022-03-19T00:00:00Z",
                "merged_at": "2022-03-19T00:00:00Z",
            },
            {
                "id": 872630389,
                "user": {"login": "Andy-Nkumane"},
                "title": "added clarity on python error raising",
                "state": "closed",
                "created_at": "2022-03-07T00:00:00Z",
                "updated_at": "2022-03-09T00:00:00Z",
                "closed_at": "2022-03-09T00:00:00Z",
                "merged_at": "2022-03-09T00:00:00Z",
            },
            {
                "id": 872484561,
                "user": {"login": "Kate-bit-dev"},
                "title": "Update _index.md",
                "state": "closed",
                "created_at": "2022-03-06T00:00:00Z",
                "updated_at": "2022-03-12T00:00:00Z",
                "closed_at": "2022-03-13T00:00:00Z",
                "merged_at": "2022-03-13T00:00:00Z",
            },
        ]

        with patch.dict(
            "consume_github_api.consume_github_api.params",
            self.params,
            clear=True,
        ):

            retrieved_pull_requests = get_pull_requests(
                "Owner", "Repo", "2022-03-08", "2022-03-09"
            )
            expected_pull_requests = [
                {
                    "id": 872630389,
                    "user": "Andy-Nkumane",
                    "title": "added clarity on python error raising",
                    "state": "closed",
                    "created_at": "2022-03-07",
                },
                {
                    "id": 874927260,
                    "user": "Ryan-oc",
                    "title": "update sololearn python and all contentlinks etc",
                    "state": "closed",
                    "created_at": "2022-03-09",
                },
            ]

            self.assertEqual(retrieved_pull_requests, expected_pull_requests)


if __name__ == "__main__":
    unittest.main()
