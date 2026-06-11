from typing import TypeVar, Generic, Optional, Any
from pydantic import BaseModel, Field

T = TypeVar("T")

class ServerResponse(BaseModel, Generic[T]):
    """Standardized response format for all MCP tools."""
    success: bool
    data: Optional[T] = None
    error: Optional[str] = None

class GitHubProfile(BaseModel):
    """GitHub user profile data."""
    username: str
    name: Optional[str] = None
    followers: int
    following: int
    public_repos: int
    profile_url: str

class RepositoryInfo(BaseModel):
    """GitHub repository information."""
    name: str
    description: Optional[str] = None
    stars: int = Field(alias="stargazers_count")
    forks: int = Field(alias="forks_count")
    language: Optional[str] = None
    open_issues: int = Field(alias="open_issues_count")
    created_at: str

    class Config:
        populate_by_name = True
