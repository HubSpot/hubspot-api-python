import requests
import json
from urllib.parse import urlencode

from hubspot.utils.requests.http_auth import Auth


class Request:
    def __init__(self, config: dict, options: dict = None):
        self.base_url = config.get("base_url", "https://api.hubapi.com")
        self.headers = {}
        self.body = None
        self.default_json = options.get("default_json", True) if options else True
        self.options = options or {}
        self.method = self.options.get("method", "GET").upper()
        self.config = config

        self.init_headers()
        self.apply_auth()
        self.url = self.generate_url()
        self.set_body()

    def get_url(self) -> str:
        return self.url

    def get_method(self) -> str:
        return self.method

    def get_options_for_sending(self) -> dict:
        options = {}
        if self.headers:
            options["headers"] = self.headers
        if self.body:
            options["data"] = self.body
        return options

    def apply_auth(self):
        auth = Auth.choose_auth(self.config, self.options)

        if auth["auth_type"]:
            if auth["auth_type"] == "api_key":
                self.options["qs"] = self.options.get("qs", {})
                self.options["qs"]["hapikey"] = self.config.get(auth["auth_type"])

            if auth["auth_type"] == "access_token":
                self.headers["Authorization"] = f"Bearer {self.config.get(auth['auth_type'])}"

    def init_headers(self):
        if self.default_json:
            self.headers["Content-Type"] = "application/json"
        self.headers.update(self.get_default_headers())
        if "headers" in self.options:
            self.headers.update(self.options["headers"])

    def get_default_headers(self) -> dict:
        headers = {
            "User-Agent": self.config.get("user_agent", "custom-python-client/1.0")
        }
        if self.default_json:
            headers["Accept"] = "application/json, */*;q=0.8"
        return headers

    def generate_url(self) -> str:
        url = self.options.get("base_url", self.base_url)
        path = self.options.get("path", "")
        url = f"{url}{path}"

        qs = self.options.get("qs")
        if qs:
            query_string = urlencode(qs, doseq=True)
            delimiter = "&" if "?" in url else "?"
            url += f"{delimiter}{query_string}"

        return url

    def set_body(self):
        if "body" in self.options:
            self.body = self.options["body"]
            if self.default_json and isinstance(self.body, (dict, list)):
                self.body = json.dumps(self.body)

    def send(self) -> requests.Response:
        try:
            method_func = getattr(requests, self.method.lower(), requests.get)
            response = method_func(self.get_url(), **self.get_options_for_sending())
            return response
        except requests.exceptions.RequestException as e:
            print(f"HTTP error occurred: {e}")
            raise
