'''Run local cgi server from the current directory treating *.cgi file as executable python cgi scripts.'''
import http.server, sys, os

class CGIExtHTTPRequestHandler(http.server.CGIHTTPRequestHandler): # looks for CGI files(*.cgi) in any subdirectory
    
    def is_python(self, path):
        return path.lower().endswith('.cgi')

    def is_cgi(self):
        base = self.path
        query = ''
        i = base.find('?')
        if i != -1:
            query = base[i:]
            base = base[:i]
        if not base.lower().endswith('.cgi'):
            return False
        [parentDirs, script] = base.rsplit('/', 1)
        self.cgi_info = (parentDirs, script+query)
        return True

def main():
    blanks = os.getcwd().count(' ')
    if blanks == 0: # server cannot handle blanks in path names
        cgiServer = http.server.HTTPServer(('localhost', 80), CGIExtHTTPRequestHandler)
        print('Localhost CGI server started')
        cgiServer.serve_forever()
    else:
        input("Path {dirName} has {blanks} space(s). Remove blanks or move files. Press enter to close.".format(**locals()))

main()