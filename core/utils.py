def open_file_kv(name):
    path, filename = name.split('.')
    return open('{}/kv/{}.kv'.format(path, filename), encoding='utf-8').read()