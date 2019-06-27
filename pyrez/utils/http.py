def build_user_agent(dependencies, origin=None):
    from ..__version__ import __package_name__, __url__, __version__
    import sys
    __DEFAULT_USER_AGENT__ = '{pyrez} ({url} {ver}) [Python/{py.major}.{py.minor}.{py.micro} {dependencies.__name__}/{dependencies.__version__}]'.format(pyrez=__package_name__, url=__url__, ver=__version__, py=sys.version_info, dependencies=dependencies)
    if origin:
        return {'User-Agent': __DEFAULT_USER_AGENT__, 'Origin': origin}
    return {'User-Agent': __DEFAULT_USER_AGENT__} #return `Client/${package_version}` + ' (JavaScript; Node.js ' + process.version + ')';

def json_or_text(resp, is_async=False, encoding='utf-8'):
    from json.decoder import JSONDecodeError
    if is_async:
        async def a_json_or_text(resp, encoding='utf-8'):
            import aiohttp
            try:
                return await resp.json()
            except (JSONDecodeError, ValueError, aiohttp.ContentTypeError):
                return await resp.text(encoding=encoding)
        return a_json_or_text(resp, encoding)
    try:
        return resp.json()
    except (JSONDecodeError, ValueError):
        return resp.text
