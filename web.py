from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!doctype html>
<html>
<head>
<title> My Web Server</title>
</head>
<body>
<table border="5"> 
        <tr>
            <th>Configuration</th>
            <th>Description</th>
        </tr>
        <tr>
           <td>processor</td>
           <td>13th Gen Intel(R) Core(TM) i5-1335U, 1300 Mhz, 10 Core(s),12 Logical Processor</td>
        </tr>
        <tr>
            <td>OS name</td>
            <td>Microsoft  Windows 11 Home Single Language</td>
        </tr>
        <tr>
            <td>memory</td>
            <td>350</td>
        </tr>
        <tr>
            <td>RAM</td>
            <td>16GB</td>
        </tr>
        <TR>
            <td>System manufacture</td>
            <td>LENOVA</td>
        </TR>
        <tr>
            <td>OS manufacture</td>
            <td>Microsoft Corporation</td>
        </tr>
        
    </table>
</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()