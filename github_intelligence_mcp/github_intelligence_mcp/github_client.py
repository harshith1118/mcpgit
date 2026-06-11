import requests
from typing import Optional, Dict, Any
from .config import GITHUB_TOKEN
from .models import GitHubProfile, RepositoryInfo

class GitHubClient:
    """A client to interact with the GitHub REST API."""
    
    BASE_URL = "https://api.github.com"

    def __init__(self):
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "github-intelligence-mcp-server"
        }
        if GITHUB_TOKEN:
            self.headers["Authorization"] = f"token {GITHUB_TOKEN}"

    def get_profile(self, username: str) -> GitHubProfile:
        """Fetch GitHub user profile."""
        url = f"{self.BASE_URL}/users/{username}"
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code == 404:
                raise ValueError(f"GitHub user '{username}' not found.")
            
            if response.status_code == 403 or response.status_code == 429:
                raise RuntimeError("GitHub API rate limit exceeded. Please try again later or provide a GITHUB_TOKEN.")

            response.raise_for_status()
            data = response.json()
            
            return GitHubProfile(
                username=data["login"],
                name=data.get("name"),
                followers=data["followers"],
                following=data["following"],
                public_repos=data["public_repos"],
                profile_url=data["html_url"]
            )
        except requests.exceptions.Timeout:
            raise RuntimeError("Request to GitHub API timed out.")
        except requests.exceptions.ConnectionError:
            raise RuntimeError("Failed to connect to GitHub API. Check your internet connection.")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"An unexpected error occurred while fetching profile: {str(e)}")

    def get_repository(self, owner: str, repo: str) -> RepositoryInfo:
        """Fetch GitHub repository information."""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}"
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code == 404:
                raise ValueError(f"Repository '{owner}/{repo}' not found.")
            
            if response.status_code == 403 or response.status_code == 429:
                raise RuntimeError("GitHub API rate limit exceeded. Please try again later or provide a GITHUB_TOKEN.")

            response.raise_for_status()
            data = response.json()
            
            return RepositoryInfo.model_validate(data)
        except requests.exceptions.Timeout:
            raise RuntimeError("Request to GitHub API timed out.")
        except requests.exceptions.ConnectionError:
            raise RuntimeError("Failed to connect to GitHub API. Check your internet connection.")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"An unexpected error occurred while fetching repository: {str(e)}")
