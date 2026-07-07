import os
from pagio.services.markdowns import markdown_to_html_node


def extract_title(markdown: str) -> str:
    if markdown is None:
        raise ValueError("Provided value was None")

    lines = markdown.splitlines()

    if not lines:
        raise ValueError("Markdown must not be empty.")

    first_line = lines[0].strip()

    if not first_line.startswith("# "):
        raise Exception("Markdown must begin with h1 header.")

    title = first_line[2:].strip()

    if not title:
        raise ValueError("The H1 heading must contain a title.")

    return title


def generate_page(from_path, template_path, dest_path) -> None:
    print(f"Generating page from {from_path} to {
          dest_path} using {template_path}")

    markdown = ""
    with open(from_path) as markdown_file:
        markdown = markdown_file.read()

    template = ""
    with open(template_path) as template_file:
        template = template_file.read()

    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    html_page = template.replace("{{ Title }}", title)
    html_page = html_page.replace("{{ Content }}", content)

    dest_dir_path = os.path.dirname(dest_path)

    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as html_file:
        html_file.write(html_page)
