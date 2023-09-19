import sys
sys.path.append("/workspaces/IndividProj1")
sys.path.append("/workspaces/IndividProj1/src")
from src.descriptivestats import get_ratingcountav, get_med, get_stddev, gen_mkdwn, generate_ratings_histogram
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

    # Call the code that generates the Markdown file
    os.system(f"python {script_path}")  # Run the script using the correct path

    # Calculate the path to the generated Markdown file in the 'output' directory
    generated_file_path = os.path.join("..", "output", "summary_stats.md")

    # Check if the file exists
    assert os.path.exists(generated_file_path)

    # Read the file content
    with open(generated_file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Perform assertions on the file content
    assert content != ""
