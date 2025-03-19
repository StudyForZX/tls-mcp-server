import logging

from .tls import TlsResource
from config import TLS_CONFIG
from server.server import mcp
from volcengine.tls.tls_exception import TLSException
from volcengine.tls.tls_requests import DescribeProjectRequest, DescribeProjectsRequest
from volcengine.tls.tls_responses import DescribeProjectResponse, DescribeProjectsResponse

logger = logging.getLogger("tls_mcp_project")

class TlsProjectResource(TlsResource):
    """
        火山引擎日志项目资源类
    """
    def describe_project(self, project_id: str) -> DescribeProjectResponse:
        """
        调用 DescribeProject 接口查询日志项目信息。
        api: https://www.volcengine.com/docs/6470/112178
        """
        request = DescribeProjectRequest(project_id)

        return self.client.describe_project(request)


    def describe_projects(self, project_id: str = None, project_name: str = None,
                                page_number: int = 1, page_size: int = 20,
                                is_full_name: bool = False, iam_project_name: str = None) -> DescribeProjectsResponse:
        """
        调用 DescribeProjects 接口查看当前地域下所有日志项目信息。
        api: https://www.volcengine.com/docs/6470/112179
        """
        request: DescribeProjectsRequest = {
            "page_number": page_number,
            "page_size": page_size,
            "is_full_name": is_full_name,
            **({"project_id": project_id} if project_id else {}),
            **({"project_name": project_name} if project_name else {}),
            **({"iam_project_name": iam_project_name} if iam_project_name else {}),
        }

        return self.client.describe_projects(DescribeProjectsRequest(**request))



# 实例化资源
project_resource = TlsProjectResource()

# mcp资源注册
@mcp.resource(TLS_CONFIG.endpoint + "/DescribeProject?ProjectId={project_id}")
async def describe_project(project_id: str) -> dict:
    try:
        result = project_resource.describe_project(project_id)
        return vars(result.get_project())
    except TLSException as e:
        logger.error(f"Describe project error: {e}")
        raise e


@mcp.resource(uri=TLS_CONFIG.endpoint + "/DescribeProjects")
async def describe_projects() -> dict:
    """
    所有 query 参数通过 request.query 获取
    """
    try:
        result = project_resource.describe_projects()
        return {
            "total": result.get_total(),
            "projects": [vars(project_info) for project_info in result.get_projects()]
        }
    except TLSException as e:
        logger.error(f"Describe projects error: {e}")
        raise e