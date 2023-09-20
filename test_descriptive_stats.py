import sys

sys.path.append("/workspaces/IndividProj1")
sys.path.append("/workspaces/IndividProj1/src")
from descriptivestats import (
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
    # Specify the name of the script file you want to work with
    script_filename = "descriptivestats.py"

    # Specify the name of the generated Markdown file
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
