
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
def read_file(filename, *, is_async=False, mode='rb', encoding='utf-8', is_json=False):
  """Loads a file"""
  if filename[-5:]=='.json':
    is_json = True
  if is_async:
    try:
      async def __read_file__(filename, mode='rb', encoding='utf-8', is_json=False):
        import aiofiles
        #, encoding=encoding
        try:
          async with aiofiles.open(filename, mode=mode) as f:
            if is_json:
              import json
              from json.decoder import JSONDecodeError
              try:
                return json.loads(await f.read())
                #return json.load(await f.read())
              except json.decoder.JSONDecodeError:
              	pass
              return {}
            return await f.read()
        except FileNotFoundError:
        	pass
      return __read_file__(filename, mode=mode, encoding=encoding, is_json=is_json)
    except ImportError:
    	pass
  try:
    f = open_if_exists(filename, mode, encoding)
    if f:
      if is_json:
        import json
        from json.decoder import JSONDecodeError
        try:
          with f:
            r = json.load(f)
            if not isinstance(r, dict) and isinstance(r, str):
              r = json.loads(r)
            return r
        except json.decoder.JSONDecodeError:
          pass
        return {}
      if f.readable():
        return f.read()#lines
      return f
  except FileNotFoundError:
    pass
  return None

def write_file(filename, content=None, *, is_async=False, mode='w', is_json=False, encoding='utf-8', data_path=None, file_type='json', **kw):
  if data_path:
    filename = f'{data_path}/{filename}.{file_type}'
  #if content and isinstance(content, str):
  #  mode = 'wt'
  try:
    if is_async:
      try:
        async def __write_file__(filename, content=None, *, mode='w', is_json=False, encoding='utf-8', **kw):
          import aiofiles
          async with aiofiles.open(filename, mode) as f:
            if is_json:
              import json
              #await f.write(json.dump(content or {}, **kw))
              await f.write(json.dumps(content or {}, **kw))
            else:
            	await f.write(content or b'')
            #import json
            #await f.write(json.dumps(content))
          return __write_file__(filename, content=content, mode=mode, is_json=is_json, encoding=encoding, **kw)
      except ImportError:
      	pass
    with open_if_exists(filename, mode, encoding) as f:
      if is_json:
        import json
        json.dump(content or {}, f, **kw)
        #from .json import dump
        #dump(content or {}, f, **kw)
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
