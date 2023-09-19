"""
A script utilizing the descriptive statistics functions in the lib.py module.
"""
import lib 


def get_ratingcountav():
    rate_count, rate_sum, rate_avg = lib.get_ratingcount_avg()
    return rate_count, rate_sum, rate_avg

def get_med():
    med = lib.get_median_rating()
    return med

def get_stddev():
    stddev_rate = lib.get_stddev_rating()
    return stddev_rate

def gen_mkdwn():
    lib.write_stats_to_mkdwn()

def generate_ratings_histogram():
    lib.save_rating_histogram()


if __name__ == "__main__":
    print("Descriptive Statistics")
    stats = lib.get_loadanddrop()  # pragma: no cover

    gen_mkdwn()
    generate_ratings_histogram()

