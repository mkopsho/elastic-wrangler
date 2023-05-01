# ESWrangler
A small Python CLI that indexes the contents of a file into an Elasticsearch index.
<p align="center">
  <img src=https://user-images.githubusercontent.com/33524375/235536304-91961886-032b-4593-bf9b-28a5be1a1d3d.png
</p>

```
usage: python es_wrangler [-h] filename index api username password

Indexes the contents of a file into an Elasticsearch index

positional arguments:
  filename    the json file with your data
  index       the target elasticsearch index
  api         the target elasticsearch api
  username    your elasticsearch username
  password    your elasticsearch password

optional arguments:
  -h, --help  show this help message and exit

Git goin', cowpoke!
```

# Setup
This was built with Python 3.9.x, so run this with a modern version of Python. I recommend [pyenv](https://github.com/pyenv/pyenv) to manage Python versions and virtualenvs.

Install your dependencies:
```
pip install requirements.txt
```

Optionally, run the demo ES cluster:
```
docker compose up
```
# Execution
This will index the sample `nginx` logs provided in this repo into the `nginx` index in your local Elasticsearch cluster. Notice that you will have to [add minimal security to your cluster](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/security-minimal-setup.html) to utilize usernames and passwords.
```
python elastic_wrangler.py nginx.json nginx http://localhost:9200 username password
```

Navigate to `http://localhost:5601` to access Kibana and play with the data.
