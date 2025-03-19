from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP(
    "TLS MCP Server",
    dependencies=[
        "env",
        "volcengine"
    ],
)
