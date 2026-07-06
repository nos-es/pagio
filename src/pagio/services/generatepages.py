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
