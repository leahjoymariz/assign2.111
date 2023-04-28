from flask import Flask         # from the flask module import the flask class


app = Flask(__name__)           # create an instance of Flask into our variable "app"
                                # from here on out, "app" is now an "object"



@app.get("/api/aboutme")       # We can now use our objects method "get" as a decorator
def index():                    # A decorator wraps a function (more on this in a bit)
    me = {                      # On line 8, we can create a new dictionary with key/value pairs.
    "first_name": "Leah",
    "last_name": "Duco",
    "hobbies": "Cooking",
    "is_active": True
    }

    return me                  # When you return a dictionary from a view       function,
                               # flask automatically converts it to JSON for compatibility
