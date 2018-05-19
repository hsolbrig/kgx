import kgx

_transformers = {
    'txt' : kgx.PandasTransformer,
    'csv' : kgx.PandasTransformer,
    'tsv' : kgx.PandasTransformer,
    'graphml' : kgx.GraphMLTransformer,
    'ttl' : kgx.ObanRdfTransformer,
    'json' : kgx.JsonTransformer,
    'rq' : kgx.SparqlTransformer
}

_file_types = ', '.join(_transformers.keys())

def get_transformer(extention):
    return _transformers.get(extention)

def get_file_types():
    return _file_types

def get_type(filename):
    for t in _transformers.keys():
        if filename.endswith('.' + t):
            return t
    else:
        return None

class Config(object):
    def __init__(self):
        self.debug = False