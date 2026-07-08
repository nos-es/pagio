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


def generate_page(from_path, template_path, dest_path, base_path) -> None:
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
    html_page = html_page.replace('href="/', f'href="{base_path}')
    html_page = html_page.replace('src="/', f'src="{base_path}')

    dest_dir_path = os.path.dirname(dest_path)

    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as html_file:
        html_file.write(html_page)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path) -> None:

    for name in os.listdir(dir_path_content):
        source_item = os.path.join(dir_path_content, name)
        target_item = os.path.join(dest_dir_path, name)

        print(f"Copying: {source_item} -> {target_item}")

        if os.path.isfile(source_item):
            target_item = target_item.replace(".md", ".html")
            generate_page(source_item, template_path, target_item, base_path)
        elif os.path.isdir(source_item):
            generate_pages_recursive(
                source_item, template_path, target_item, base_path)
        else:
            print(f"Skipping unsupported file type: {source_item}")
