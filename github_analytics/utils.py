from datetime import datetime


def leading_zero(in_string):
    """Add a leading zero to a string with only one character.

    :param in_string:           string of min length 1 and max length 2

    :return:                    string with length of 2 and with leading zero where applies

    """
    len_string = len(in_string)

    if (len_string > 2) or (len_string < 1):
        raise ValueError("Value must have only one or two characters.  Input '{}' has {}".format(in_string, len_string))

    elif len_string == 1:
        return "0{}".format(in_string)

    else:
        return in_string


def convert_google_time(datetime_str, split_string='T'):
    """Convert Google time to datetime as a string.

    :param datetime_str:      Datetime string from GET JSON string for "timestamp" in
                                a format matching this example "2016-10-21T00:00:00Z"

    :param split_string:      String used to split date from time; default is "T"

    :return:                  Datetime string in the format "YYYY-MM-DD HH:mm:SS"

    """
    # get a list of [date, time]
    dt = datetime_str.split(split_string)

    # get a list of [YYYY, MM, DD]
    dte = dt[0].split('-')

    # get a list of [HH, mm, SS], slice of trailing "Z"
    tm = dt[1][:-1].split(':')

    # return formatted string
    return '{}-{}-{} {}:{}:{}'.format(dte[0],  # four digit year
                                      leading_zero(dte[1]),  # two digit month
                                      leading_zero(dte[2]),  # two digit day
                                      leading_zero(tm[0]),  # two digit hour
                                      leading_zero(tm[1]),  # two digit day
                                      leading_zero(tm[2]))  # two digit second


def get_download_datetime():
    """Create a download datetime string matching the format of the formatted GitHub API
    datetime string.

    :return:            Datetime string in the format "YYYY-MM-DD HH:mm:SS"

    """
    # get current datetime
    dt_now = datetime.now()

    return '{}-{}-{} {}:{}:{}'.format(dt_now.year,
                                      leading_zero(str(dt_now.month)),
                                      leading_zero(str(dt_now.day)),
                                      leading_zero(str(dt_now.hour)),
                                      leading_zero(str(dt_now.minute)),
                                      leading_zero(str(dt_now.second)))

