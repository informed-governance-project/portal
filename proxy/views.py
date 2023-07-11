from revproxy.views import ProxyView

from portal.models import ExternalToken


class DefaultProxyView(ProxyView):
    # upstream = "http://127.0.0.1:5000/"

    def get_proxy_request_headers(self, request):
        # print(self.upstream)
        # print(request.user)
        headers = super().get_proxy_request_headers(request)

        module_path = request.path.strip("/")
        try:
            external_token = ExternalToken.objects.get(
                user=request.user, module__path=module_path
            )
        except ExternalToken.DoesNotExist:
            # return the headers without the authentication token
            # users should be blockes by the proxified module
            return headers

        headers["Proxy-Token"] = external_token.token
        return headers
