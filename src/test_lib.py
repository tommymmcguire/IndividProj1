import sys

sys.path.append("/workspaces/IndividProj1")
sys.path.append("/workspaces/IndividProj1/src")
from src.lib import (
    get_ratingcount_avg,
    get_median_rating,
    get_stddev_rating,
    write_stats_to_mkdwn,
)
import os


def test_ratecount():
    # Test the count_rating function
    r_count, r_sum, r_avg = get_ratingcount_avg()
    assert int(r_count) == 32780
    assert int(r_sum) == 2989097
    assert int(r_avg) == 91


def test_median_r():
    median_r = get_median_rating()
    assert int(median_r) == 91


def test_stddev_r():
    stddeviation_r = get_stddev_rating()
    assert int(stddeviation_r) == 2


def test_markdown_gen():
    # Calculate the path to the 'descriptivestats.py' script in the 'src' directory
    script_path = os.path.join("..", "src", "lib.py")

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
