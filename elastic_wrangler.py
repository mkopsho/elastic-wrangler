import argparse
import json
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers

# create a simple cli with argparse
parser = argparse.ArgumentParser(
    prog="python es_wrangler",
    description="Indexes the contents of a file into an Elasticsearch index",
    epilog="Git goin', cowpoke!",
)

# add positional args to the cli
parser.add_argument("filename", help="the json file with your data")
parser.add_argument("index", help="the target elasticsearch index")
parser.add_argument("api", help="the target elasticsearch api")
parser.add_argument("username", help="your elasticsearch username")
parser.add_argument("password", help="your elasticsearch password")

# gather and assign all of the inputs
args = parser.parse_args()
filename = args.filename
index = args.index
api = args.api
username = args.username
password = args.password


# read, transform, and index the data from the local file
def transform_and_index_data(filename, index):
    data = []
    with open(filename) as file:
        for line in file:
            data.append(json.loads(line))

    for entry in data:
        yield {
            "_index": index,
            "time": datetime.strptime(entry["time"], "%d/%b/%Y:%H:%M:%S %z"),
            "remote_ip": entry["remote_ip"],
            "remote_user": entry["remote_user"],
            "request": entry["request"],
            "response": entry["response"],
            "bytes": entry["bytes"],
            "referrer": entry["referrer"],
            "agent": entry["agent"],
        }


# controller
def main():
    # setup es client with basic auth
    elastic_client = Elasticsearch(
        hosts=[api],
        basic_auth=(username, password),
    )
    helpers.bulk(
        elastic_client, transform_and_index_data(filename, index), stats_only=True
    )


if __name__ == "__main__":
    main()
