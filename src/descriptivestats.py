"""
A script utilizing the descriptive statistics functions in the lib.py module.
"""
import lib 


def get_ratingcountav(df):
    rate_count, rate_sum, rate_avg = lib.get_ratingcount_avg(df)
    return rate_count, rate_sum, rate_avg

def get_med(df):
    med = lib.get_median_rating(df)
    return med

def get_stddev(df):
    stddev_rate = lib.get_stddev_rating
    return stddev_rate

def gen_mkdwn():
    lib.write_stats_to_mkdwn()

def generate_ratings_histogram():
    lib.save_rating_histogram()

gen_mkdwn()
generate_ratings_histogram()

