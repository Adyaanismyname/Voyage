
# Voyage Framework

Voyage is a lightweight and easy-to-use web framework for Python, designed for building simple web applications with ease. With a focus on routing and flexibility, Voyage allows you to define routes, handle query parameters, and even reroute users to different pages.

## Features

- **Simple Routing**: Easily define routes using decorators.
- **Dynamic URL Parameters**: Capture dynamic segments of URLs with ease.
- **Query Parameters**: Access query parameters for your routes.
- **Rerouting**: Seamlessly reroute users to different pages.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Adyaanismyname/Voyage.git


# Quick Start

Here's a simple example of how to use the Voyage framework:

```python
from Voyage.App import App
from Voyage.Serve import read_html


app = App()


@app.route('/home/')
def home():
  return read_html('home.html')

@app.route('/about/<id>')
def about(id):
  return f"Welcome to framework lol , id = {id}"

@app.route('/search')
def search(query_params):
  search_query = query_params.get('query' , [''])[0]
  return f"You searched for {search_query}"

@app.route('/reroute/home/')
def reroute_to_home():
  return app.reroute('/home/')

app.run()


```
Here’s a breakdown of the key features:

- **`@app.route('/home/')`**: Defines a route for the `/home/` URL.
- **`@app.route('/about/<id>')`**: Captures a dynamic segment in the URL and passes it to the `about` function.
- **`query_params.get('query', [''])[0]`**: Retrieves the value of the query parameter from the URL.
- **`app.reroute('/home/')`**: Reroutes the user to the `/home/` URL.

This setup allows for flexible routing and parameter handling in your web application.


# Running the Application

To run your application , simply execute the Python script:

   ```bash
python your_script_name.py
```
The application will start, and you can access it by navigating to http://localhost:8000 in your web browser.

# Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.







