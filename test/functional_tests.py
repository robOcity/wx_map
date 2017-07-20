import wpc_map_scraper as wpc
import os


def test_scrape_map_sequence(tmpdir):
    # create a sequence of events with two occurrences on two days
    expected, paths = scrape_maps(tmpdir, '2017-06-30', '2017-07-01', ['00', '12'], ['usfntsfc', 'ussatsfc'])

    # perform tests
    check_numbers(expected, paths, tmpdir)
    check_files_exist(paths)


def test_scrape_map(tmpdir):
    # create a sequence of events with two occurrences on two days
    expected, paths = scrape_maps(tmpdir, '2017-07-04', '2017-07-04', ['18'], ['namussfc'])

    # perform tests
    check_numbers(expected, paths, tmpdir)
    check_files_exist(paths)


def check_files_exist(paths):
    for path in paths:
        assert (os.path.exists(path))


def check_numbers(expected, paths, tmpdir):
    assert (len(paths)) == expected
    assert (len(tmpdir.listdir())) == expected


def scrape_maps(tmpdir, start, stop, times, maps):
    # create a sequence of events with two occurrences on two days
    dates = [date for date in wpc.make_time_series(start, stop, times)]

    # create the unique file names for each map and time
    paths = [wpc.get_map_path(tmpdir, date, map)
             for date in dates
             for map in maps]
    wpc.scrape_map(start, stop, times, maps, tmpdir)
    expected_num = len(dates) * len(maps)
    return expected_num, paths

