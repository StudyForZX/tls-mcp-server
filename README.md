# Volcengine TLS Model Context Protocol Server

An MCP server implementation for retrieving data from TLS.

## structure

The structure is as follows:
```
mcp-server-tls/
├── src/
│   ├── __init__.py
│   ├── main.py                 # Main entry point
│   ├── config.py               # Configuration
│   ├── server/                 # Server-related files
│   │   ├── __init__.py
│   │   ├── server.py           # MCP server initialization
│   │   ├── resources/          # Resources (API, data models)
│   │   │    ├── __init__.py
│   │   │    ├── project.py     # Project resource (e.g., DescribeProject, etc.)
│   │   │    ├── tls.py         # TLS base resource
│   │   │    ├── topic.py       # Topic resource (e.g., DescribeTopic, etc.)
│   │   └── tools/              # Tools (business logic, tasks, or operations)
│   │        ├── __init__.py
│   │        ├── project.py     # Project tool (e.g., DescribeProjectTool)
│   │        └── topic.py       # Topic tool (e.g., DescribeTopicTool)
│   └── client/                 # Client-related files (optional)
│       ├── __init__.py
│       └── client.py           # mcp client
├── tests/                      # Test directory
│   └── __init__.py
├── .env_example                # env param smaple
├── .gitignore
├── .python-version
├── LICENSE
├── pyproject.toml
├── README.md
└── uv.lock
```

## Configuration

Obtain volcengine access key ID, secret access key, and region from the volcengine Management Console and configure credentials files using Default profile

Refer to the .env.example file to configure your volcengine credentials

```
mv .env_example .env
```

## usage

To use this server, you'll need to:

Install the required dependencies:

[If not already installed] https://docs.astral.sh/uv/

```
uv venv

source .venv/bin/activate

uv sync
```

Run the server:

```
uv run python src/main.py
```

Run the client:
```
uv run python src/client/client.py src/main.py
```

## MCP setting

```json
{
  "mcpServers": {
    "tls": {
        "command": "uv",
        "args": [
            "--directory",
            "/ABSOLUTE/PATH/TO/PARENT/FOLDER/src",
            "run",
            "main.py"
        ]
    }
  }
}
```

## Already supported resources

1. DescribeProject
2. DescribeProjects
3. DescribeTopic
3. DescribeTopics

## Security
See [SECURITY](https://github.com/modelcontextprotocol/servers/blob/main/SECURITY.md) for more information.

## License
This library is licensed under the MIT License. See the LICENSE file for details.