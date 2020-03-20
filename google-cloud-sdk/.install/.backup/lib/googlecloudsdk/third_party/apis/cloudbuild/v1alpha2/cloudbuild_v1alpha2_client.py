"""Generated client library for cloudbuild version v1alpha2."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.cloudbuild.v1alpha2 import cloudbuild_v1alpha2_messages as messages


class CloudbuildV1alpha2(base_api.BaseApiClient):
  """Generated client library for service cloudbuild version v1alpha2."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://cloudbuild.googleapis.com/'
  MTLS_BASE_URL = u'https://cloudbuild.mtls.googleapis.com/'

  _PACKAGE = u'cloudbuild'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1alpha2'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'CloudbuildV1alpha2'
  _URL_VERSION = u'v1alpha2'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new cloudbuild handle."""
    url = url or self.BASE_URL
    super(CloudbuildV1alpha2, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_workerPools = self.ProjectsWorkerPoolsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsWorkerPoolsService(base_api.BaseApiService):
    """Service class for the projects_workerPools resource."""

    _NAME = u'projects_workerPools'

    def __init__(self, client):
      super(CloudbuildV1alpha2.ProjectsWorkerPoolsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a `WorkerPool` to run the builds, and returns the new worker pool.

      Args:
        request: (CloudbuildProjectsWorkerPoolsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (WorkerPool) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha2/projects/{projectsId}/workerPools',
        http_method=u'POST',
        method_id=u'cloudbuild.projects.workerPools.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'workerPoolId'],
        relative_path=u'v1alpha2/{+parent}/workerPools',
        request_field=u'workerPool',
        request_type_name=u'CloudbuildProjectsWorkerPoolsCreateRequest',
        response_type_name=u'WorkerPool',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a `WorkerPool`.

      Args:
        request: (CloudbuildProjectsWorkerPoolsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha2/projects/{projectsId}/workerPools/{workerPoolsId}',
        http_method=u'DELETE',
        method_id=u'cloudbuild.projects.workerPools.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha2/{+name}',
        request_field='',
        request_type_name=u'CloudbuildProjectsWorkerPoolsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Returns details of a `WorkerPool`.

      Args:
        request: (CloudbuildProjectsWorkerPoolsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (WorkerPool) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha2/projects/{projectsId}/workerPools/{workerPoolsId}',
        http_method=u'GET',
        method_id=u'cloudbuild.projects.workerPools.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha2/{+name}',
        request_field='',
        request_type_name=u'CloudbuildProjectsWorkerPoolsGetRequest',
        response_type_name=u'WorkerPool',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists `WorkerPool`s by project.

      Args:
        request: (CloudbuildProjectsWorkerPoolsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListWorkerPoolsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha2/projects/{projectsId}/workerPools',
        http_method=u'GET',
        method_id=u'cloudbuild.projects.workerPools.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha2/{+parent}/workerPools',
        request_field='',
        request_type_name=u'CloudbuildProjectsWorkerPoolsListRequest',
        response_type_name=u'ListWorkerPoolsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a `WorkerPool`.

      Args:
        request: (CloudbuildProjectsWorkerPoolsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (WorkerPool) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha2/projects/{projectsId}/workerPools/{workerPoolsId}',
        http_method=u'PATCH',
        method_id=u'cloudbuild.projects.workerPools.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1alpha2/{+name}',
        request_field=u'workerPool',
        request_type_name=u'CloudbuildProjectsWorkerPoolsPatchRequest',
        response_type_name=u'WorkerPool',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(CloudbuildV1alpha2.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
