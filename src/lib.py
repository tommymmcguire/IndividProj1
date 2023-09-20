import os
import polars as pl
import matplotlib.pyplot as plt

CSV_URL = "https://raw.githubusercontent.com/paiml/wine-ratings/main/wine-ratings.csv"
OUTPUT_FILE = "output.md"  # Specify the Markdown file name
OUTPUT_FOLDER = os.path.join(os.path.dirname(__file__), "..", "output")


def get_loadanddrop():
    df = pl.read_csv(CSV_URL)
    df.drop_in_place("grape")
    return df


def get_stats():
    df = get_loadanddrop()
    rl = df["rating"].describe()
    return rl


def get_ratingcount_avg():
    df = get_loadanddrop()
    rating_count = 0
    for _ in df["rating"]:
        rating_count += 1
    rl = df["rating"].to_list()
    rating_sum = 0
    for n in rl:
        rating_sum += int(n)
    rating_avg = rating_sum / rating_count
    return rating_count, rating_sum, rating_avg


def get_median_rating():
    df = get_loadanddrop()
    median_rating = df["rating"].median()
    return median_rating


def get_stddev_rating():
    df = get_loadanddrop()
    stddev_rating = df["rating"].std()
    return stddev_rating


def save_rating_histogram():
    # Read the CSV data into a Polars DataFrame
    df = pl.read_csv(CSV_URL)

    # Plot the histogram of the 'rating' column
    plt.hist(df["rating"].to_list(), bins=20, edgecolor="k")
    plt.xlabel("Wine Ratings")
    plt.ylabel("Frequency")
    plt.title("Distribution of Wine Ratings")
    plt.grid(True)
    dest = os.path.join(OUTPUT_FOLDER, "wine_rating.png")
    plt.savefig(dest)
    return dest  # Return the path to the saved image


def write_stats_to_mkdwn():
    rating_count, rating_sum, rating_avg = get_ratingcount_avg()
    median_rating = get_median_rating()
    stddev_rating = get_stddev_rating()
    hist_path = save_rating_histogram()
    dest = os.path.join(OUTPUT_FOLDER, "summary_stats.md")

    with open(dest, "w") as markdown_file:
        markdown_file.write(f"Count of rating is: {rating_count}\n\n")
        markdown_file.write(f"Sum of rating is: {rating_sum}\n\n")
        markdown_file.write(f"Average rating is: {rating_avg}\n\n")
        markdown_file.write(f"Median of rating is: {median_rating}\n\n")
        markdown_file.write(f"Standard deviation of rating is: {stddev_rating}\n\n")
        markdown_file.write(f"\n![Histogram](file://{hist_path})")
