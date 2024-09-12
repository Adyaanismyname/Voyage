class read_files:
  @staticmethod
  def read_html(path):
    with open(path , 'r') as f:
      contents = f.read()
      response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{contents}"
    return response.encode()

