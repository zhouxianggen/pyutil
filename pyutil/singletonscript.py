#coding: utf-8
import os
import sys
import tempfile
import psutil


class SingletonScript(object):
    def __init__(self):
        path = self.get_script_path(os.getpid())
        pid_file = '%s/%s.pid' % (tempfile.gettempdir(), 
                path.replace('/', '_'))
        if (os.path.isfile(pid_file) and
                self.get_script_path(open(pid_file, 'rb').read()) == path):
            print('script already running')
            sys.exit(-1)
        open(pid_file, 'w').write(str(os.getpid()))

    def get_script_path(self, pid):
        try:
            p = psutil.Process(int(pid))
        except Exception as e:
            return None
        cwd = p.cwd()
        for s in p.cmdline():
            path = os.path.join(cwd, s)
            if os.path.isfile(path) and path[-3:] == '.py':
                return path
        return None

