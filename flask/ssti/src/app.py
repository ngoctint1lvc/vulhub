from flask import Flask, request, render_template_string
from jinja2 import Template

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get('name', 'guest')

    # we cannot use flask global variables like config, g,... inside the template in this case
    # t = Template("Hello " + name)
    # return t.render()

    return render_template_string("Hello " + name)

if __name__ == "__main__":
    app.run()