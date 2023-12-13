from rest_framework.throttling import SimpleRateThrottle

class CustomThrottle1(SimpleRateThrottle):
    rate = '5/minute' # The throttle rate period can be minute, second, hour, or day.
    scope = 'limited_scope1'

    def get_cache_key(self, request, view):
        # Implement a unique cache key based on request and view
        # For example, you can use the user's IP address as a key
        return 'custom_throttle1'


class CustomThrottle2(SimpleRateThrottle):
    rate = '10/minute'
    scope = 'premium_users'

    def get_cache_key(self, request, view):
        return 'custom_throttle2'


class RateThrottle(SimpleRateThrottle):
    scope = 'premium_users'
    rate = '10/minute'

    def get_cache_key(self, request, view):
        return 'rate_throttle'
    #     # return super().get_cache_key(request, view)
    #     if request.user.token_expired>0:
    #         ident = request.user.pk
    #     else:
    #         ident = self.get_ident(request)

    #     return self.cache_format % {
    #         'scope': self.scope,
    #         'ident': ident
    #     }
