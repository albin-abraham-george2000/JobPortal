from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class BadRequestView(TemplateView):
    template_name = 'errors/400.html'
    status = 400

    def render_to_response(self, context, **response_kwargs):
        response_kwargs['status'] = self.status
        return super().render_to_response(context, **response_kwargs)

class PermissionDeniedView(TemplateView):
    template_name = 'errors/403.html'
    status = 403

    def render_to_response(self, context, **response_kwargs):
        response_kwargs['status'] = self.status
        return super().render_to_response(context, **response_kwargs)

class PageNotFoundView(TemplateView):
    template_name = 'errors/404.html'
    status = 404

    def render_to_response(self, context, **response_kwargs):
        response_kwargs['status'] = self.status
        return super().render_to_response(context, **response_kwargs)

class ServerErrorView(TemplateView):
    template_name = 'errors/500.html'
    status = 500

    def render_to_response(self, context, **response_kwargs):
        response_kwargs['status'] = self.status
        return super().render_to_response(context, **response_kwargs)



