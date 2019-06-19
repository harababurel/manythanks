#!/usr/bin/env python3
from random import choice
from flask import Flask

TEMPLATE = """
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="s.css" />
        <title>Show your appreciation!</title>
    </head>
    <body>
        <h1 class="msg">%s</h1>
    </body>
</html>
"""

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    many = [
        "many %s", "numerous %s", "a great deal of %s",
        "great quantities of %s", "plenty of %s", "countless %s",
        "innumerable %s", "an army of %s", "a multitude of %s",
        "a multiplicity of %s", "multitudinous %s", "numberless %s",
        "abundant %s", "profuse %s", "an abundance of %s", "a profusion of %s",
        "eleventy %s", "loads of %s", "masses of %s", "stacks of %s",
        "heaps of %s", "piles of %s", "bags of %s", "oodles of %s",
        "hundreds of %s", "thousands of %s", "millions of %s",
        "billions of %s", "zillions of %s",
        "more %s than one can shake a stick at", "gazillions of %s",
        "bazillions of %s"
    ]
    thanks = [
        "thanks", "gratitude", "gratefulness", "appreciation", "recognition",
        "credit"
    ]
    return TEMPLATE % (choice(many) % choice(thanks))
