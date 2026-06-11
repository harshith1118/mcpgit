# GitHub Intelligence MCP Server

A professional-grade Model Context Protocol (MCP) server built with Python and FastMCP to provide deep insights into GitHub users and repositories.

## 🚀 Overview

The GitHub Intelligence MCP Server acts as a high-performance bridge between AI agents (such as Claude Desktop, Cursor, or IDE extensions) and the GitHub REST API. It delivers sanitized, structured, and validated data, enabling AI assistants to perform repository audits, user profile analysis, and community health checks with precision.

### Key Features

-   **Profile Analysis**: Comprehensive statistics for any GitHub user, including follower counts and repository metrics.
-   **Repository Insights**: Deep-dive data on stars, forks, language distribution, and issue counts.
-   **Input Sanitization**: Automatic handling of whitespace and newline characters in tool inputs.
-   **Robust Error Handling**: Graceful management of GitHub API rate limits, 404 errors, and network timeouts.
-   **Structured JSON Responses**: Native Python dictionary returns ensure perfect integration with MCP clients.
-   **AI-Ready Resources**: Built-in analysis rules and a senior-level repository review prompt.

---

## 🛠 Installation

### Prerequisites
- Python 3.10+
- A GitHub Personal Access Token (optional, but recommended to avoid rate limits)

### Setup

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd github_intelligence_mcp
    ```

2.  **Create a virtual environment**:
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment**:
    Create a `.env` file in the root directory:
    ```env
    GITHUB_TOKEN=your_github_token_here
    ```

---

## 📖 Usage

### Running the Server
Start the server directly using:
```bash
python -m github_intelligence_mcp.server
```

### Available MCP Tools

#### 1. `get_github_profile`
Fetches detailed profile information for a GitHub user. Inputs are automatically stripped of whitespace.

**Parameters:**
- `username` (string): The GitHub login handle.

**Example Response:**
```json
{
  "success": true,
  "data": {
    "username": "torvalds",
    "name": "Linus Torvalds",
    "followers": 210000,
    "following": 0,
    "public_repos": 7,
    "profile_url": "https://github.com/torvalds"
  },
  "error": null
}
```

#### 2. `analyze_repository`
Provides a snapshot of a repository's health and activity.

**Parameters:**
- `owner` (string): The user or organization.
- `repository` (string): The name of the repository.

**Example Response:**
```json
{
  "success": true,
  "data": {
    "name": "react",
    "description": "The library for web and native user interfaces.",
    "stars": 230000,
    "forks": 46000,
    "language": "JavaScript",
    "open_issues": 1600,
    "created_at": "2013-05-24T16:15:54Z"
  },
  "error": null
}
```

### Resources & Prompts

-   **Resource**: `github://analysis-rules`  
    Provides the LLM with a framework for evaluating repository quality based on community metrics.
-   **Prompt**: `repository_review_prompt`  
    A specialized persona that guides the AI to analyze a repository like a senior software engineer.

---

## 🧪 Testing with MCP Inspector

You can verify the server's functionality using the MCP Inspector:

```bash
npx @modelcontextprotocol/inspector python -m github_intelligence_mcp.server
```

Once the inspector is running, you can test input sanitization and error handling by providing malformed inputs (e.g., `" facebook "`) and observing the sanitized API calls.

---

## 🛡 License

This project is licensed under the MIT License - see the LICENSE file for details.
