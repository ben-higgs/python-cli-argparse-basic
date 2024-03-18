#!/usr/bin/env python
"""{{ cookiecutter.description }}"""
import argparse
import requests

{% for command in commands %}
def {{ command }}(args):
    requests.post(
        args.url,
        headers={},
        params={},
        data=""
    )
{% endfor %}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://localhost:8000", help="The base url")

    subparsers = parser.add_subparsers(help="Commands")

    {% for command in commands %}
    {{ command }}_parser = subparsers.add_parser("{{ command }}", help="")
    {{ command }}_parser.set_defaults(func={{ command }})
    {{ command }}_parser.add_argument("-o", "--opt", help="")
    {% endfor %}

    args = parser.parse_args()
    print(args.func(args))
