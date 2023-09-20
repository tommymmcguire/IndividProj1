import sys

sys.path.append("/workspaces/IndividProj1")
sys.path.append("/workspaces/IndividProj1/src")
from src.descriptivestats import (
    get_ratingcountav,
    get_med,
    get_stddev,
    gen_mkdwn,
    generate_ratings_histogram,
)
import os


def test_count():
    # Test the count_rating function
    rat_count, rat_sum, rat_avg = get_ratingcountav()
    assert int(rat_count) == 32780
    assert int(rat_sum) == 2989097
    assert int(rat_avg) == 91


def test_med():
    med_r = get_med()
    assert int(med_r) == 91


def test_stddev():
    stdev_r = get_stddev()
    assert int(stdev_r) == 2


def test_markdown_generation():
    # Calculate the path to the 'descriptivestats.py' script in the 'src' directory
    script_path = os.path.join("..", "src", "descriptivestats.py")

    # Determine the path to the 'output' directory relative to the test file
    test_file_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(test_file_dir, "..", "output")

    # Calculate the path to the generated Markdown file in the 'output' directory
    generated_file_path = os.path.join(output_dir, "summary_stats.md")

    # Check if the file exists
    assert os.path.exists(
        generated_file_path
    ), f"Markdown file not found at {generated_file_path}"

    # Read the file content
    with open(generated_file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Perform assertions on the file content
    assert content != "", "Markdown file is empty"
