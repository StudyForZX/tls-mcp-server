from server.server import mcp
from typing import Any, Dict
from ..resources.project import describe_project, describe_projects

@mcp.tool()
async def describe_project_tool(project_id: str) -> Dict[str, str]:
    """
    通过火山引擎 TLS 获取当前权限下指定项目信息。
    """
    try:
        return await describe_project(project_id)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
async def describe_projects_tool() -> Dict[str, Any]:
    """
    通过火山引擎 TLS 获取当前权限下的多个项目信息(限制20个)。
    """
    try:
        return await describe_projects()
    except Exception as e:
        return {"error": str(e)}
