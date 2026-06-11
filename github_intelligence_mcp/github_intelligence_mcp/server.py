from typing import Any, Dict, Union
from mcp.server.fastmcp import FastMCP
from .github_client import GitHubClient
from .models import ServerResponse, GitHubProfile, RepositoryInfo
from .config import APP_NAME

# Initialize FastMCP server
mcp = FastMCP(APP_NAME)
client = GitHubClient()

@mcp.tool()
def get_github_profile(username: str) -> Dict[str, Any]:
    """
    Fetch GitHub user information.
    
    Args:
        username: The GitHub username to look up.
    """
    # Sanitize and validate input
    username = username.strip() if username else ""
    if not username:
        return ServerResponse(
            success=False,
            error="Username is required and cannot be empty."
        ).model_dump()

    try:
        profile = client.get_profile(username)
        return ServerResponse[GitHubProfile](
            success=True,
            data=profile
        ).model_dump()
    except Exception as e:
        return ServerResponse(
            success=False,
            error=str(e)
        ).model_dump()

@mcp.tool()
def analyze_repository(owner: str, repository: str) -> Dict[str, Any]:
    """
    Analyze GitHub repository information.
    
    Args:
        owner: The owner of the repository (user or organization).
        repository: The name of the repository.
    """
    # Sanitize inputs
    owner = owner.strip() if owner else ""
    repository = repository.strip() if repository else ""
    
    # Validate inputs
    if not owner or not repository:
        return ServerResponse(
            success=False,
            error="Both owner and repository name are required."
        ).model_dump()

    try:
        repo_info = client.get_repository(owner, repository)
        return ServerResponse[RepositoryInfo](
            success=True,
            data=repo_info
        ).model_dump()
    except Exception as e:
        return ServerResponse(
            success=False,
            error=str(e)
        ).model_dump()

@mcp.resource("github://analysis-rules")
def get_analysis_rules() -> Dict[str, Any]:
    """Provide context to the LLM about repository quality."""
    return ServerResponse(
        success=True,
        data={
            "quality_metrics": [
                "stars",
                "activity",
                "issues",
                "forks",
                "community adoption"
            ],
            "description": "Rules used when analyzing repository health"
        }
    ).model_dump()

@mcp.prompt("repository_review_prompt")
def repository_review_prompt() -> str:
    """Reusable prompt for AI repository analysis."""
    return """Analyze this GitHub repository like a senior software engineer.

Evaluate:
- popularity
- maintainability
- technology stack
- community activity

Give clear recommendations."""

if __name__ == "__main__":
    mcp.run()
