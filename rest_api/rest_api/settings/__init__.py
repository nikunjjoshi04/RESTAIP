try:
    from .production import *
except ImportError as e:
    try:
        from .dev import *
    except ImportError as e:
        raise ImportError('You Need prod.py or dev.py files', e)
