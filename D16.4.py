LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {asctime} {module}',
            'style': '{',
        },
        'form': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'filters': {
        'special': {
            '()': 'project.logging.SpecialFilter',
            'foo': 'bar',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['special']
        },
    },
    'errors.log': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR' 'CRITICAL',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['console'],
            'level': 'ERROR' 'CRITICAL',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'ERROR' 'CRITICAL',
            'propagate': False,
        },
    'security.log': {
        'django.security': {
            'handlers': ['console'],
            'formatter': 'form'
        },
     },
    'loggers': {
        'django.security': {
            'handlers': ['console'],
            'level': 'INFO',
            'filters': ['special']
        },
    },
}