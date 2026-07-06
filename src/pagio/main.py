import os
import shutil


def recursive_copy(source_path: str, target_path: str) -> None:
    # creates folder if not exists
    os.makedirs(target_path, exist_ok=True)

    for name in os.listdir(source_path):
        source_item = os.path.join(source_path, name)
        target_item = os.path.join(target_path, name)

        print(f"Copying: {source_item} -> {target_item}")

        if os.path.isfile(source_item):
            shutil.copy(source_item, target_item)
        elif os.path.isdir(source_item):
            recursive_copy(source_item, target_item)
        else:
            print(f"Skipping unsupported file type: {source_item}")


def copy_source_to_destination(
    source_path: str,
    target_path: str,
) -> None:

    # guard clauses
    if source_path is None or target_path is None:
        raise ValueError("Source path and target path must not be None.")

    source_path = os.path.abspath(source_path)
    target_path = os.path.abspath(target_path)

    if not os.path.exists(source_path):
        raise FileNotFoundError(
            f"Source path does not exist: {source_path}"
        )

    if not os.path.isdir(source_path):
        raise NotADirectoryError(
            f"Source path is not a directory: {source_path}"
        )

    common_path = os.path.commonpath([source_path, target_path])

    if common_path == source_path:
        raise ValueError(
            "The target directory must not be inside the source directory."
        )

    if common_path == target_path:
        raise ValueError(
            "The target directory must not contain the source directory."
        )

    if os.path.exists(target_path):
        print(f"Deleting existing target directory: {target_path}")
        shutil.rmtree(target_path)

    recursive_copy(source_path, target_path)


def main() -> None:
    copy_source_to_destination("./static/", "./public/")

    pass


if __name__ == "__main__":
    main()
