def merge(values):      # values - это список словарей
    x = {}
    for s in  values:
        for key, value in s.items():
            x.setdefault(key,set()).add(value)
    return x