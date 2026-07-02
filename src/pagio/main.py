# from textnode import TextNode, TextType
from pagio.nodes.leafnode import LeafNode


def main() -> None:
    test_leafnode = LeafNode("p", "test")
    print(test_leafnode.tag)


if __name__ == "__main__":
    main()
