# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p#2gi=9x9wf4)#m-h52032tssdu#4=)+!gwt$u=3h*bi)%dn6@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

LOGGING['formatters']['colored'] = {  # type:  ignore
    '()': 'colorlog.ColoredFormatter',
    'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s',
}
LOGGING['loggers']['att_planner']['level'] = 'DEBUG'  # type:  ignore
LOGGING['handlers']['console']['level'] = 'DEBUG'  # type:  ignore
LOGGING['handlers']['console']['formatter'] = 'colored'  # type:  ignore
