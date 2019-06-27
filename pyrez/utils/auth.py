def generate_md5_hash(params=(), use_update_method=False):
    """Actually the authKey isn't passed directly, but instead embedded and hashed as MD5 Signature.

    Signatures use 4 items to be created: devId, authKey, methodName (without the Response Format), and timestamp.

    Parameters
    ----------
    methodName : |STR|
        Method name
    timestamp : |STR|
        Current timestamp

    Returns
    -------
    str
        Returns a MD5 hash code of the method (devId + methodName + authKey + timestamp)
    """
    from hashlib import md5
    if isinstance(params, (type(()), type([]))):
        params = ''.join((str(_) for _ in params if _))
    if use_update_method:
        m = md5()
        m.update(params.encode('utf-8'))#.encode()
        return m.hexdigest()
    return md5(params.encode('utf-8')).hexdigest()
