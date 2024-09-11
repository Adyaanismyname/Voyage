from Voyage import App , read_files


app = App()


@app.route('/home/')
def home():
  return read_files.read_html('home.html')

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

