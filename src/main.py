from server.server import mcp
from server.tools.project import *
from server.tools.topic import *

def main():

    print("Starting TLS MCP Server...")

    print("Loaded Resources:")
    for key, handler in mcp._mcp_server.request_handlers.items():
        print(f"{key} -> {handler}")

    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()