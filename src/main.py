from textnode import TextNode, TextType


def main() -> None:
    test = None
    print(test)
    text_node = TextNode(
        "Test Text Node", TextType.BOLD, "https://hello.com")
    print(text_node)


if __name__ == "__main__":
    main()
