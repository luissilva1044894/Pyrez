
def get_json():
    # ujson is blazing fast, but fall back to standard json if not installed
    try:
        import ujson as json
    except ImportError:
        try:
            import simplejson as json
        except ImportError:
            try:
                from django.utils import simplejson as json
            except ImportError:
                import json #raise ImportError('A json library is required to use this python library')
    return json
def to_json(data, *, separators=(',', ':'), ensure_ascii=True, sort_keys=True, indent=2):
    return get_json().dumps(data, separators=separators, ensure_ascii=ensure_ascii, sort_keys=sort_keys, indent=indent)
def unpack_json(data):
    return get_json().loads(data)

def read(path, is_async=False, mode='r', encoding='utf-8'):#read(**kwargs):
    """
    if is_async:
        try:
            import aiofiles
            async def __read__(path, mode='r', encoding='utf-8'):
                async with aiofiles.open(path, mode=mode, encoding=encoding) as f:
                    return get_json().load(await f.read())
            return __read__(path, mode, encoding)
        except ImportError:
            pass
    """
    try:
        import codecs
        try:
            with codecs.open(path, mode) as f:
                return get_json().load(f)
        except ImportError:
            with open(path, mode=mode, encoding=encoding) as f:#open(str(kwargs.get('file', None))
                return get_json().load(f)
    except FileNotFoundError:
        return None
def write(data, path, is_async=False, mode='w', encoding='utf-8'):
    """
    if is_async:
        try:
            import aiofiles
            async def __write__(path, mode='r', encoding='utf-8'):
                #RuntimeWarning: coroutine 'write.<locals>.__write__' was never awaited
                async with aiofiles.open(path, mode=mode, encoding=encoding) as f:
                    await f.write(to_json(data))
            return __write__(path, mode, encoding)
        except ImportError:
            pass
    """
    try:
        import codecs
    except ImportError:
        with open(path, mode=mode, encoding=encoding) as f:
            f.write(to_json(data))#get_json().dumps(data, f)
    else:
        with codecs.open(path, mode) as f:
            f.write(to_json(data))
