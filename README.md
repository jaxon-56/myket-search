# Myket Search

Simple Python library for searching applications on **Myket**.

## Features

* Search apps
* Package name
* Category
* App URL
* Icon URL

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from myket_search import MyketSearch

myket = MyketSearch()

results = myket.search("روبیکا")

print(results)
```

## Requirements

* requests
* beautifulsoup4

## License

MIT License
