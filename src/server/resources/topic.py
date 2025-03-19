import logging

from .tls import TlsResource
from config import TLS_CONFIG
from server.server import mcp
from volcengine.tls.tls_exception import TLSException
from volcengine.tls.tls_requests import DescribeTopicRequest, DescribeTopicsRequest
from volcengine.tls.tls_responses import DescribeTopicResponse, DescribeTopicsResponse

logger = logging.getLogger("tls_mcp_topic")

class TlsTopicResource(TlsResource):
    """
        火山引擎日志主题资源类
    """
    def describe_topic(self, topic_id: str) -> DescribeTopicResponse:
        """
        调用 DescribeTopic 接口获取日志主题基本信息。
        https://www.volcengine.com/docs/6470/112184
        """
        request = DescribeTopicRequest(topic_id)

        return self.client.describe_topic(request)

    def describe_topics(self, project_id: str, project_name: str = None,
                              topic_id: str = None, topic_name: str = None,
                              page_number: int = 1, page_size: int = 20,
                              tags: str = None) -> DescribeTopicsResponse:
        """
        调用 DescribeTopics 接口获取日志项目的所有日志主题信息。
        api: https://www.volcengine.com/docs/6470/112185
        """
        request = {
            "page_number": page_number,
            "page_size": page_size,
            "project_id": project_id,
            **({ "project_name": project_name } if project_name else {}),
            **({ "topic_id": topic_id } if topic_id else {}),
            **({ "topic_name": topic_name } if topic_name else {}),
            **({ "tags": tags } if tags else {}),
        }

        return self.client.describe_topics(DescribeTopicsRequest(**request))

# 实例化资源
topic_resource = TlsTopicResource()

# mcp资源注册
@mcp.resource(uri=TLS_CONFIG.endpoint + "/DescribeTopic?TopicId={topic_id}")
async def describe_topic(topic_id: str) -> dict:
    try:
        result: DescribeTopicResponse = topic_resource.describe_topic(topic_id)
        return vars(result.get_topic())
    except TLSException as e:
        logger.error(f"Describe topic error: {e}")
        raise e


@mcp.resource(uri=TLS_CONFIG.endpoint + "/DescribeTopics/ProjectId={project_id}")
async def describe_topics(project_id: str) -> dict:
    try:
        result: DescribeTopicsResponse = topic_resource.describe_topics(project_id)
        return {
            "total": result.get_total(),
            "topics": [vars(topic_info) for topic_info in result.get_topics()]
        }
    except TLSException as e:
        logger.error(f"Describe topics error: {e}")
        raise e