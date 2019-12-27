
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

def get_path(file=None, *args, **kw):
  import os
  file = kw.pop('file', file) or __file__
  if kw.pop('root_drive', None):
    import sys
    path = sys.executable
    while os.path.split(path)[1]:
      path = os.path.split(path)[0]
    return path
  if kw.pop('root', None):
    return os.path.dirname(os.path.dirname(os.path.abspath(file)))
  if kw.pop('folder', None):
    return os.path.dirname(os.path.abspath(file))
  return os.path.abspath(file)
  # import inspect
  # os.path.abspath(inspect.stack()[-1][1])

def open_if_exists(filename, mode='rb', encoding='utf-8'):
  """Returns a file descriptor for the filename if that file exists, otherwise ``None``."""
  import os
  if not os.path.isfile(filename) and (mode.rfind('r') != -1 or mode.rfind('a') != -1):
    return None
  try:
    import codecs
  except ImportError:
    try:
        return open(filename, mode=mode, encoding=encoding)
    except ValueError:
        return open(filename, mode=mode)#_io.BufferedReader
  else:
    return codecs.open(filename, mode)
'''
def join(params, separator=None):
  return (separator or '').join((str(_) for _ in params if _))
'''
def join_path(arr, relative_path=True):
  import os
  _j = ''
  if relative_path:
    _j = os.path.dirname(__file__).replace(__name__.split('.')[0], '')
  for _ in arr:
    _j = os.path.join(_j, str(_))
  return _j
def delete_folder(folder_path, recursive=True):
  from shutil import rmtree
  try:
    rmtree(folder_path)
  except OSError:
    pass
def create_folder(folder_path):
  import os
  if not os.path.isdir(folder_path):
    from os import mkdir
    mkdir(folder_path)
  """
  Create a directory (including parents) if it does not exist yet.
  :param path: Path to the directory to create.
  :type path: :class:`pathlib.Path`
  Uses :meth:`pathlib.Path.mkdir`; if the call fails with
  :class:`FileNotFoundError` and `path` refers to a directory, it is treated
  as success.
  """
  #def mkdir_exist_ok(path):
  #    try:
  #        path.mkdir(parents=True)
  #    except FileExistsError:
  #        if not path.is_dir(): raise
def recreate_folder(folder_path):
  delete_folder(folder_path)
  create_if_inexistent(folder_path)
def read_file(filename, mode='rb', **kw):
  """Loads a file"""
  is_json, silent = kw.pop('is_json', filename[-5:]=='.json'), kw.pop('silent', False)
  if kw.pop('is_async', None):
    try:
      async def __read_file__(filename, mode='rb'):
        import aiofiles
        try:
          async with aiofiles.open(filename, mode=mode) as f:
            if is_json:
              import json
              from json.decoder import JSONDecodeError
              try:
                return json.loads(await f.read(), **kw)
                #return json.load(await f.read())
              except json.decoder.JSONDecodeError:
                if not silent:
                  raise
              return {}
            return await f.read()
        except (FileNotFoundError, IsADirectoryError, IOError):
          if not silent:
            raise
      return __read_file__(filename, mode=mode)
    except ImportError:
    	pass
  try:
    f = open_if_exists(filename, mode, encoding=kw.pop('encoding', 'utf-8'))
    if f:
      if is_json:
        import json
        from json.decoder import JSONDecodeError
        try:
          with f:
            r = json.load(f, **kw)
            if not isinstance(r, dict) and isinstance(r, str):
              r = json.loads(r, **kw)
            return r
        except json.decoder.JSONDecodeError:
          if not silent:
            raise
        return {}
      if f.readable():
        return f.read()#lines
      return f
  except (FileNotFoundError, IsADirectoryError, IOError) as e:
    if not silent:
      raise
  return None

def write_file(filename, content=None, mode='w', **kw):
  if kw.get('data_path'):
    filename = f'{kw.pop("data_path", __file__)}/{filename}.{kw.pop("file_type", "json")}'
  #if content and isinstance(content, str):
  #  mode = 'wt'
  is_json = kw.pop('is_json', filename[-5:]=='.json')
  try:
    if kw.pop('is_async', None):
      try:
        async def __write_file__(filename, content=None, mode='w', **kw):
          import aiofiles
          async with aiofiles.open(filename, mode) as f:
            if is_json:
              from json import dumps
              #await f.write(dump(content or {}, **kw))
              await f.write(dumps(content or {}, **kw))
            else:
            	await f.write(content or b'')
        return __write_file__(filename, content=content, mode=mode, **kw)
      except ImportError:
      	pass
    with open_if_exists(filename, mode, encoding=kw.pop('encoding', 'utf-8')) as f:
      if is_json:
        from json import dump
        dump(content or {}, f, **kw)
      else:
      	#f.write(str(content) or b'')
        f.write(content or b'')
  except (FileExistsError, OSError):
    pass
#https://medium.com/python4you/python-io-streams-in-examples-97d2c4367207

'''
def read_file(filename, charset='utf-8'):
  with open(filename, 'r') as f:
    return f.read().decode(charset)

def write_file(filename, contents, charset='utf-8'):
  with open(filename, 'w') as f:
    f.write(contents.encode(charset))
'''
