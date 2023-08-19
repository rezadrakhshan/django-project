from . import jalali

def jalali_converter(time):
    jmonths = ["فروردین","اردیبهشت","خرداد","تیر","مرداد","شهریور","مهر","ابان","اذر","دی","بهمن","اسفند"]
    time_to_str = "{},{},{}".format(time.year,time.month,time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()

    time_to_list = list(time_to_tuple)
    for index, month in enumerate(jmonths):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break
    output = "{} {} {}".format(
        time_to_list[2],
        time_to_list[1],
        time_to_list[0],
    )
    return output