def overwrite(fn):
    """
    @decorator

    Purely used to help identify methods that have been overwritten from the EWrapper
    """
    return fn