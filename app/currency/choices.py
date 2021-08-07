RATE_TYPE_USD = 10
RATE_TYPE_EUR = 11

RATE_TYPE_CHOICES = (
    (RATE_TYPE_USD, 'Dollar'),
    (RATE_TYPE_EUR, 'Euro'),
)


REQUEST_METHOD_GET = 10
REQUEST_METHOD_POST = 11
REQUEST_METHOD_PUT = 12
REQUEST_METHOD_PATCH = 13
REQUEST_METHOD_DELETE = 14

REQUEST_METHOD_CHOICES = (
    (REQUEST_METHOD_GET, 'GET'),
    (REQUEST_METHOD_POST, 'POST'),
    (REQUEST_METHOD_PUT, 'PUT'),
    (REQUEST_METHOD_PATCH, 'PATCH'),
    (REQUEST_METHOD_DELETE, 'DELETE'),
)

REQUEST_METHOD_CHOICES_MAPPER = {value[1]: value[0] for value in REQUEST_METHOD_CHOICES}
