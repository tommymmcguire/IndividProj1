from src.descriptivestats import get_ratingcountav, get_med, get_stddev, gen_mkdwn, generate_ratings_histogram

def test_count():
    # Test the count_rating function
    rat_count, rat_sum, rat_avg = get_ratingcountav()
    assert int(rat_count) == 32780
    assert int(rat_sum) == 2989097
    assert int(rat_avg) == 91

    
     rating_avg, median_rating, stddev_rating = read_csv_and_count_rating()
    assert int(rating_count) == 32780
    assert int(rating_avg) == 91
    assert int(median_rating) == 91
    assert int(stddev_rating) == 2