import socket
import re
from urllib.parse import urlparse, parse_qs
import inspect
class App:


  def __init__(self):
    self.routes = {}
    self.client_socket = None
    self.client_address = None


  def run(self ,host='localhost', port=8000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))

    server_socket.listen(5)
    print(f"Server running on http://{host}:{port}/")
    try:
      while True:
        client_socket, client_address = server_socket.accept()
        self.handle_requests(client_socket , client_address)
    except KeyboardInterrupt:

      print("\nServer is shutting down...")
    finally:
      server_socket.close()



  def handle_requests(self, client_socket, client_address):
    request = client_socket.recv(1024).decode()
    print(f"Request: {request}")

    request_line = request.split('\r\n')[0]
    method, url, _ = request_line.split(' ')
    parsed_url = urlparse(url)
    path = parsed_url.path
    query_params = parse_qs(parsed_url.query)

    handler , dynamic_params = self.match_route(path)


    if handler is None:
        response_body = "404 handler not found"
        status = "404 Not Found"
        content_type = 'text/plain'
        response_body = response_body.encode()  # Ensure it is bytes
    else:
        # Check if the function accepts query parameters
        sig = inspect.signature(handler)
        params = sig.parameters

        if 'query_params'  in params:
          response_body = handler(query_params , **dynamic_params)
          while isinstance(response_body , tuple):
            handler , dynamic_params = response_body
            response_body = handler(query_params , **dynamic_params)
        else:
          response_body = handler(**dynamic_params)
          while isinstance(response_body , tuple):

            handler , dynamic_params = response_body
            response_body = handler(**dynamic_params)

        # Since `read_html` returns bytes, we handle it as HTML
        if isinstance(response_body, bytes):
            status = '200 OK'
            content_type = 'text/html'
            response = response_body
            client_socket.sendall(response)
            client_socket.close()
        else:
            status = '200 OK'
            content_type = 'text/plain'
            response_body = response_body.encode()
            response = f"HTTP/1.1 {status}\r\nContent-Type: {content_type}\r\n\r\n".encode() + response_body
            client_socket.sendall(response)
            client_socket.close()



  def route(self , url):
    def wrapper(func):
      self.routes[url] = func
      return func
    return wrapper

  def match_route(self, path):
      for route in self.routes:
          # Replace the dynamic parts with regex capture groups using named groups
          pattern = re.sub(r'<(\w+)>', lambda m: f"(?P<{m.group(1)}>\w+)", route)
          match = re.match(f"^{pattern}$", path)
          if match:
              return self.routes[route], match.groupdict()  # Extract dynamic params
      return None, {}

  def reroute(self , path):
    handler , dynamic_params = self.match_route(path)
    return handler , dynamic_params


  # def detect_call(func):
  #    def wrapper(*args , **kwargs):
  #     wrapper.was_called = True
  #     return func(*args, **kwargs)
  #    wrapper.was_called = False
  #    return wrapper






class read_files:
  @staticmethod
  def read_html(path):
    with open(path , 'r') as f:
      contents = f.read()
      response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{contents}"
    return response.encode()














