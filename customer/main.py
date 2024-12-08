from http.server import HTTPServer, BaseHTTPRequestHandler
import json


with open("db.json") as data_file:
	data = json.load(data_file)


class ServiceHandler(BaseHTTPRequestHandler):

	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.end_headers()
		
		
    
	def do_GET(self):
		#defining all the headers
		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.end_headers()
		#prints all the keys and values of the json file
		self.wfile.write(json.dumps(data).encode())
		
    
			
    
	def do_POST(self):
		length = int(self.headers['Content-Length'])
		content = self.rfile.read(length)
		content_str = content.decode('utf-8')
		json_data = json.loads(content_str)
		
		#write the changes to the json file
		with open("db.json",'w+') as file_data:
			data['customers'].append(json_data)
			json.dump(data,file_data)
		self.send_response(201)
		self.send_header('Content-type', 'application/json')
		self.end_headers()
		self.wfile.write(json.dumps({
			"msg": "Customer created!"
		}).encode())

	
	
			
#Server Initialization
try:
    server = HTTPServer(('127.0.0.1',8081), ServiceHandler)
    print("Connected to server!")
    server.serve_forever()
except Exception as err:
	print("Error on server!")