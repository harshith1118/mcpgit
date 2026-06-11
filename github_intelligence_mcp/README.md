# GitHub Intelligence MCP Server

A professional-grade Model Context Protocol (MCP) server built with Python and FastMCP to provide deep insights into GitHub users and repositories.

## 🚀 Overview

The GitHub Intelligence MCP Server acts as a high-performance bridge between AI agents (such as Claude Desktop, Cursor, or IDE extensions) and the GitHub REST API. It delivers sanitized, structured, and validated data, enabling AI assistants to perform repository audits, user profile analysis, and community health checks with precision.

---

## 🤖 AI-Assisted Development

### AI Tools Used

This project was developed with assistance from:

- Gemini CLI

### How Gemini CLI Accelerated Development

Gemini CLI was used throughout the development process to speed up:

#### 1. Architecture Planning
- Designed the MCP server structure
- Planned separation between:
  - MCP interface layer
  - GitHub API client
  - Response models
  - Configuration handling

#### 2. Code Generation
- Generated the initial FastMCP implementation
- Created MCP tool definitions
- Assisted with GitHub REST API integration

#### 3. Debugging & Improvements
- Helped identify and fix:
  - MCP response serialization issues
  - JSON formatting improvements
  - Input sanitization problems

#### 4. Documentation
- Assisted in creating:
  - Setup instructions
  - Usage examples
  - MCP testing workflow

All generated code was reviewed, tested using MCP Inspector, and refined manually.

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
