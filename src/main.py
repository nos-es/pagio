from textnode import TextNode, TextType
from utilities import split_nodes_image


def main() -> None:
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])

    print(new_nodes)

if __name__ == "__main__":
    main()
