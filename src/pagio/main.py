from pagio.services.copystatics import copy_source_to_destination
from pagio.services.generatepages import generate_pages_recursive


def main() -> None:
    copy_source_to_destination("./static/", "./public/")
    generate_pages_recursive("./content/", "./template.html", "./public")
    # generate_page("./content/index.md", "./template.html",
    #               "./public/index.html")

    pass


if __name__ == "__main__":
    main()
