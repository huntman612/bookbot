import sys
from stats import get_book_length
from stats import get_word_count
from stats import get_sorted_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    nums = get_book_length(path)
    num = get_word_count(path)
    sorted = get_sorted_count(nums)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for key, value in sorted.items():
        print(f"{key}: {value}")
    print("============= END ===============")
main()