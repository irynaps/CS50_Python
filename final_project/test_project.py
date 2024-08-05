from project import SpotifyDataAnalyzer

test = SpotifyDataAnalyzer("one.csv")


def main():
    test_get_listening_period()
    test_get_total_listening_time()
    test_get_top_performers()
    test_get_top_songs()
    test_get_top_days()


def test_get_listening_period():
    assert test.get_listening_period() == (
        " Start Date: 2022-06-26\n"
        " End Date:   2022-09-15\n"
        " Duration:   80 days and 11 hours\n"
    )


def test_get_total_listening_time():
    assert test.get_total_listening_time() == (
        " Total Minutes: 13284\n" " Total Hours:   221\n" " Total Days:    9\n"
    )


def test_get_top_performers():
    assert test.get_top_performers() == (
        " 1. Lana Del Rey\n"
        " 2. Friends Talking Fantasy Podcast\n"
        " 3. KALEO\n"
        " 4. M83\n"
        " 5. Led Zeppelin\n"
    )


def test_get_top_songs():
    assert test.get_top_songs() == (
        " 1. Stairway to Heaven - Remaster\n"
        " 2. No Deeper We Can Fall\n"
        " 3. You Said It All\n"
        " 4. Amour plastique\n"
        " 5. Solitude\n"
    )


def test_get_top_days():
    assert test.get_top_days() == (
        " 1. 2022-09-03\n"
        " 2. 2022-09-05\n"
        " 3. 2022-07-14\n"
        " 4. 2022-09-02\n"
        " 5. 2022-07-15\n"
    )


if __name__ == "__main__":
    main()
