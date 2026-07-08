from pagio.services.copystatics import copy_source_to_destination
from pagio.services.generatepages import generate_pages_recursive
import sys


def main() -> None:
    base_path = "/"
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    print(base_path)
    copy_source_to_destination("./static/", "./docs/")
    generate_pages_recursive("./content/", "./template.html", "./docs/", base_path)


if __name__ == "__main__":
    main()
