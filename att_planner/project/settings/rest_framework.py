from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=365),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'SIGNING_KEY': '9ba0ef42d0bdf1f6bd89c63fe176a944827191d63843bb80e7ce9aa8b79b5c60',
    'UPDATE_LAST_LOGIN': True,
    'USER_ID_FIELD': 'account_number',
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),
    'DEFAULT_PARSER_CLASSES': ('rest_framework.parsers.JSONParser',),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

# REST_FRAMEWORK = {
#     'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
#     'DEFAULT_PARSER_CLASSES': (
#         'rest_framework_json_api.parsers.JSONParser',
#     ),
#     'DEFAULT_RENDERER_CLASSES': (
#         'rest_framework_json_api.renderers.JSONRenderer',
#         'rest_framework.renderers.BrowsableAPIRenderer'
#     ),
#     'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
#     'DEFAULT_FILTER_BACKENDS': (
#         'rest_framework_json_api.filters.QueryParameterValidationFilter',
#         'rest_framework_json_api.filters.OrderingFilter',
#         'rest_framework_json_api.django_filters.DjangoFilterBackend',
#         'rest_framework.filters.SearchFilter',
#     ),
#     'SEARCH_PARAM': 'filter[search]',
#     'TEST_REQUEST_RENDERER_CLASSES': (
#         'rest_framework_json_api.renderers.JSONRenderer',
#     ),
#     'TEST_REQUEST_DEFAULT_FORMAT': 'vnd.api+json'
# }
