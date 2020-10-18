import re
import json
from datetime import datetime


def replace_chunk(content, marker, chunk):
    replacer = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    chunk = "<!-- {} starts -->\n{}\n<!-- {} ends -->".format(marker, chunk, marker)
    return replacer.sub(chunk, content)


def ord(n):
    return str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))


def dtStylish(dt,f):
    return dt.strftime(f).replace("{th}", ord(dt.day))


def pprint(string):
    json_formatted_str = json.dumps(string, indent=2)
    print(json_formatted_str)

def date_to_iso(string):
    return datetime.strptime(string, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d')