import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Find the first iframe tag
    iframe_match = re.search(r'<iframe\b[^>]*>', s)
    if not iframe_match:
        return None

    iframe_tag = iframe_match.group(0)

    src_match = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', iframe_tag)
    if src_match:
        video_id = src_match.group(1)
        return f"https://youtu.be/{video_id}"

    return None


if __name__ == "__main__":
    main()
