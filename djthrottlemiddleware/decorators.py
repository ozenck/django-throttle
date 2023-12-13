from rest_framework import status
from rest_framework.response import Response

def check_throttle(throttle_class):
    def decorator(view_func):
        def _wrapped_view(self, request, *args, **kwargs):
            print(throttle_class)
            throttle_instance = throttle_class()
            if throttle_instance.allow_request(request, self):
                return view_func(self, request, *args, **kwargs)
            else:
                return Response({"message": "Throttled request, Please try again later."}, status=status.HTTP_429_TOO_MANY_REQUESTS)

        return _wrapped_view

    return decorator
