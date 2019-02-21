# coding: utf8 
import logging
import socket
from .singletonscript import SingletonScript
from .hash64 import hash64

def get_logger(name='log', level=logging.INFO):
    log = logging.getLogger(name)
    log.setLevel(level)
    if not log.handlers:
        fmtStr = ('[%(name)-15s %(threadName)-10s %(levelname)-8s '
                '%(asctime)s] %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(fmtStr))
        log.addHandler(handler)
    return log


def get_ip():
    try:
        t = socket.gethostbyname_ex(socket.gethostname())
        ips = [ip for ip in t[2] if not ip.startswith("127.")]
        if ips:
            return ips[0]
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(('8.8.8.8', 53))
            n = s.getsockname()
            return n[0] if n else None
    except Exception as e:
        return None


__all__ = (
        'get_logger',
        'get_ip'
        'SingletonScript', 
        'hash64')

