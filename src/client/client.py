import asyncio
from typing import Optional
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

class MCPClient:
    def __init__(self):
        # Initialize session and client objects
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()

    async def connect_to_server(self, server_script_path: str):
        """Connect to an MCP server

        Args:
            server_script_path: Path to the server script (.py or .js)
        """
        is_python = server_script_path.endswith('.py')
        is_js = server_script_path.endswith('.js')
        if not (is_python or is_js):
            raise ValueError("Server script must be a .py or .js file")

        command = "python" if is_python else "node"
        server_params = StdioServerParameters(
            command=command,
            args=[server_script_path],
            env=None
        )

        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await self.session.initialize()

        # List available tools
        response = await self.session.list_tools()
        tools = response.tools
        print("\nConnected to server with tools:", [tool.name for tool in tools])

    ## 验证project
    async def describe_project(self, project_id: str):
        """验证 DescribeProject tool"""
        messages = {
            "project_id": project_id
        }
        print(f"start to get project_id: {project_id} info")
        response = await self.session.call_tool("describe_project_tool", messages)
        # 处理工具响应并打印结果
        if response.isError:
            print(f"Failed to call describe_project_tool for project {project_id}")
            print("Error:", response.content)
        else:
            print(f"Tool response for describe project info is: {response.content}")

    async def describe_projects(self):
        """验证 DescribeProjects tool"""
        response = await self.session.call_tool("describe_projects_tool")
        # 处理工具响应并打印结果
        if response.isError:
            print(f"Failed to call describe_projects_tool")
            print("Error:", response.content)
        else:
            print(f"Tool response for describe projects info is: {response.content}")

    ## 验证topic
    async def describe_topic(self, topic_id: str):
        """验证 DescribeTopic tool"""
        messages = {
            "topic_id": topic_id
        }
        print(f"start to get topic_id: {topic_id} info")
        response = await self.session.call_tool("describe_topic_tool", messages)
        # 处理工具响应并打印结果
        if response.isError:
            print(f"Failed to call describe_topic_tool for topic {topic_id}")
            print("Error:", response.content)
        else:
            print(f"Tool response for describe topic info is: {response.content}")

    async def describe_topics(self, project_id: str):
        """验证 DescribeTopics tool"""
        messages = {
            "project_id": project_id,
        }
        response = await self.session.call_tool("describe_topics_tool", messages)
        # 处理工具响应并打印结果
        if response.isError:
            print(f"Failed to call describe_topics_tool")
            print("Error:", response.content)
        else:
            print(f"Tool response for describe topics info is: {response.content}")

    async def cleanup(self):
        """Clean up resources"""
        await self.exit_stack.aclose()

async def main():
    if len(sys.argv) < 2:
        print("Usage: uv run python src/client/client.py src/main.py")
        sys.exit(1)

    client = MCPClient()
    try:
        await client.connect_to_server(sys.argv[1])
        # Change it to your project or topic
        await client.describe_project("your-project-info")
        await client.describe_projects()
        await client.describe_topic("your-topic-info")
        await client.describe_topics("your-project-id")
    finally:
        await client.cleanup()

if __name__ == "__main__":
    import sys
    asyncio.run(main())