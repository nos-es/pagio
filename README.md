# Pagio

Pagio is a small static site generator written in Python. It converts Markdown files into HTML pages, applies a shared HTML template, and copies static assets into the generated site.

## Features

* Converts Markdown files to HTML
* Supports headings, paragraphs, bold and italic text, inline code, links, images, quotes, code blocks, and lists
* Processes nested content directories recursively
* Copies CSS, images, and other static files
* Supports a custom base path for deployments under a subdirectory

## Requirements

* Python 3.10 or newer

Pagio uses only the Python standard library, so no additional packages need to be installed.

## Usage

Run the generator from the project root:

```bash
PYTHONPATH=src python3 -m pagio.main
```

The generated site will be written to the `docs/` directory.

To serve the site locally:

```bash
cd docs
python3 -m http.server 8888
```

The site will then be available at:

```text
http://localhost:8888
```

An optional base path can be passed as the first argument. This is useful when the site is hosted under a subdirectory, for example on GitHub Pages:

```bash
PYTHONPATH=src python3 -m pagio.main /pagio/
```

## Project Structure

```text
content/        Markdown content
static/         CSS, images, and other static files
src/pagio/      Static site generator source code
tests/          Unit tests
template.html   HTML template used for generated pages
docs/           Generated website
```

## Tests

Run the unit tests with:

```bash
./test.sh
```

## License

This project is licensed under the MIT License.

## Project Origin

This project was built as part of the [Build a Static Site Generator in Python](https://www.boot.dev/courses/build-static-site-generator-python) course on [Boot.dev](https://www.boot.dev/).

