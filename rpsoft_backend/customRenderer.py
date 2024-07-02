from rest_framework import renderers

class CustomRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        statusCode = renderer_context['response'].status_code
        print("Error details", data, renderer_context)
        message=data['message']
        results=data['results']
        if data['statusCode'] is not None:
            statusCode=data['statusCode']
        response_data ={"statusCode":statusCode, "message":message, "data": { 'results': results}}
        return super().render(response_data, accepted_media_type, renderer_context)