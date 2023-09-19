import os
import polars as pl
import matplotlib.pyplot as plt

CSV_URL = "https://raw.githubusercontent.com/paiml/wine-ratings/main/wine-ratings.csv"
OUTPUT_FILE = "output.md"  # Specify the Markdown file name
HISTOGRAM_IMAGE_FILE = "wine_rating.png"  # Specify the histogram image file name


def get_loadanddrop():
    df = pl.read_csv(CSV_URL)
    df.drop_in_place('grape')
    return df()

def get_stats():
    df = get_loadanddrop()
    rl = df['rating'].describe()
    return rl

def get_ratingcount_avg():
    df = get_loadanddrop()
    rating_count = 0
    for _ in df['rating']:
        rating_count += 1
    rl = df['rating'].to_list()
    rating_sum = 0
    for n in rl:
        rating_sum += int(n)
    rating_avg = rating_sum/rating_count
    return rating_count, rating_sum, rating_avg

def get_median_rating():
    df = get_loadanddrop()
    median_rating = df['rating'].median()
    return median_rating

def get_stddev_rating():
    df = get_loadanddrop()
    stddev_rating = df['rating'].std()
    return stddev_rating

def save_rating_histogram():
    # Read the CSV data into a Polars DataFrame
    df = pl.read_csv(CSV_URL)
    
    # Plot the histogram of the 'rating' column
    plt.hist(df['rating'].to_list(), bins=20, edgecolor='k')
    plt.xlabel('Wine Ratings')
    plt.ylabel('Frequency')
    plt.title('Distribution of Wine Ratings')
    plt.grid(True)
    dest = os.path.join(
        os.path.dirname(__file__), "..", "output", "wine_rating.png"
    )
    plt.savefig(dest)
    
def write_stats_to_mkdwn():
    stats = get_stats()
    his = save_rating_histogram()
    dest = os.path.join(os.path.dirname(__file__), "..", "output", "summary_stats.md")
    with open(dest, "w", encoding="utf-8") as f:
        f.write(stats.to_markdown())
        f.write(his.to_markdown())
