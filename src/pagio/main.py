from pagio.services.copystatics import copy_source_to_destination


def main() -> None:
    copy_source_to_destination("./static/", "./public/")

    pass


if __name__ == "__main__":
    main()
