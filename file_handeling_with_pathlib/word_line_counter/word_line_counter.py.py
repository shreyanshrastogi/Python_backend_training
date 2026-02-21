from pathlib import Path


def word_and_line_counter(paragraph: str) -> tuple[int, int]:
    """This function returns word and line count respectively."""
    file = Path("file.txt")
    file.write_text(paragraph)

    data = file.read_text()
    count_w = len(data.split())
    count_l = len(data.splitlines())

    return (count_w, count_l)


if __name__ == "__main__":
    paragraph = input("Enter paragraph (use \\n for new lines): ")
    paragraph = paragraph.replace("\\n", "\n")

    word, line = word_and_line_counter(paragraph=paragraph)
    print(f"total Words: {word} | total Lines: {line}")
