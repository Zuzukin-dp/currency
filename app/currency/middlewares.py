from currency import choices
from currency.models import Analytics

from django.db.models import F


class AnalyticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # numerator = Analytics.objects.filter(request_method=request_method, path=request.path,
        #                                      status=self.get_response(request).status_code).last()
        # if numerator:
        #     numerator.counter += 1
        #     numerator.save()
        # else:
        #     Analytics.objects.create(request_method=request_method, path=request.path,
        #                              counter=1, status=self.get_response(request).status_code)

        response = self.get_response(request)
        request_method = choices.REQUEST_METHOD_CHOICES_MAPPER[request.method]

        obj, created = Analytics.objects.get_or_create(
            request_method=request_method, path=request.path, status=response.status_code,
            defaults={'counter': 1}
        )
        if not created:
            Analytics.objects.filter(pk=obj.pk).update(counter=F('counter') + 1)
        # breakpoint()

        return response
