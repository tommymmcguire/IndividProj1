from lib import (
    get_ratingcount_avg,
    get_median_rating,
    get_stddev_rating,
)
import os

def test_markdown_gen():
    # Specify the name of the file you want to work with
    script_filename = "lib.py"

    # Calculate the path to the generated Markdown file
    generated_file_path = "output/summary_stats.md"

    # Check if the file exists
    assert os.path.exists(script_filename), f"File not found: {script_filename}"
    assert os.path.exists(
        generated_file_path
    ), f"Markdown file not found: {generated_file_path}"

    # Read the file content
    with open(generated_file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Perform assertions on the file content
    assert content != "", "Markdown file is empty"


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
