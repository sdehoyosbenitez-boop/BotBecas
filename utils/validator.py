from urllib.parse import urlparse

def valid_url(u):
 p=urlparse(u); return bool(p.scheme and p.netloc)
