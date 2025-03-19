from server.server import mcp
from typing import Any, Dict
from ..resources.topic import describe_topic, describe_topics

@mcp.tool()
async def describe_topic_tool(topic_id: str) -> Dict[str, str]:
    """
    通过火山引擎 TLS 获取当前权限下指定主题信息。
    """
    try:
        return await describe_topic(topic_id)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
async def describe_topics_tool(project_id: str) -> Dict[str, Any]:
    """
    通过火山引擎 TLS 获取当前权限下的多个主题信息(限制20个)。
    """
    try:
        return await describe_topics(project_id)
    except Exception as e:
        return {"error": str(e)}