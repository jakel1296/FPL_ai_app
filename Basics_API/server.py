import http.server #import the http.server module
from http.server import HTTPServer #import HTTPServer
import json #import the json module
from urllib.parse import urlparse #import the urlparse module

class handler1(http.server.BaseHTTPRequestHandler): #create a class for the handler
    def do_GET(self): #GET is when client asks for data
        parsed_path = urlparse(self.path) #parse the path
        path = parsed_path.path #get the path
        if path == "/string":
            self.send_response(200) #200 is the status code for success
            self.send_header("Content-type", "text/plain") #content type is text/plain
            self.end_headers() #end the headers
            self.wfile.write(b"Hello from server!") #write the response to the client
        elif path == "/json":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response_data = {"message": "Hello from server", "type": "json"}
            self.wfile.write(json.dumps(response_data).encode())
        else:
            self.send_response(404) #404 is the status code for not found
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")
    def do_POST(self): #POST is when client sends data
        content_length = int(self.headers.get("Content-Length", 0)) #get the content length
        request_body = self.rfile.read(content_length) #read the request body
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        if path == "/echo-string":
            self.send_response(200) 
            self.send_header("Content-type", "text/plain") 
            self.end_headers() #end the headers
            self.wfile.write(b"Server received: " + request_body) 
        elif path == "/echo-json":
            try:
                received_data = json.loads(request_body.decode()) #decode the request body
                response_data = {
                    "status": "received", #status of the request
                    "original": received_data, #original data received
                    "processed": f"Server processed: {received_data}" #processed data
                }
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(response_data).encode())
            except json.JSONDecodeError:
                self.send_response(400)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                error = {"error": "Invalid JSON"}
                self.wfile.write(json.dumps(error).encode())
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run_server(host="127.0.0.1", port=8002): #run the server
    server_address = (host, port) #server address
    httpd = HTTPServer(server_address, handler1) #create a server
    print(f"Server running on http://{host}:{port}") #print the server address
    httpd.serve_forever() #serve the server forever (until ctrl+c)

# commented out as can only have one per file so incorportaed into function at end of file
# if __name__ == "__main__": #used so does not auto run if file is imported
#    run_server() #run the server


#########################################################################################
# Using FAST api instead of barebones: 

from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

# ===== FASTAPI VERSION =====
app = FastAPI()

app.add_middleware( #CORS middleware (allows the client to make requests from different origins)
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/string")
def fastapi_get_string():
    return "Hello from FastAPI server!"

@app.get("/json")
def fastapi_get_json():
    return {"message": "Hello from FastAPI server", "type": "json"} #automatically Converts it to JSON; Sets Content-Type: application/json; Sets status 200; Encodes it to bytes

@app.post("/echo-string")
def fastapi_echo_string(message: str = Body(..., media_type="text/plain")):
    return f"Server received: {message}"

@app.post("/echo-json")
def fastapi_echo_json(data: dict):
    return {
        "status": "received",
        "original": data,
        "processed": f"Server processed: {data}"
    }

if __name__ == "__main__":
    import uvicorn
    print("===== Running FASTAPI version on port 8003 =====")
    uvicorn.run(app, host="127.0.0.1", port=8003)