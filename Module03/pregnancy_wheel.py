import datetime


def print_header():
    print("-----------------------------")
    print("        Due Date")
    print("-----------------------------")
    print()


def get_lmp_from_patient():
    print("When was the patient's last normal menstrual cycle?")

    date_str = input("Format: dd/mm/yyyy? ")
    # "05/06/2018"

    parts = date_str.split('/')
    if len(parts) != 3:
        print("Incorrect date. Please use the following format: dd/mm/yyyy", date_str)
        return get_lmp_from_patient()

    year = int(parts[2])
    month = int(parts[1])
    day = int(parts[0])

    lmp = datetime.date(year, month, day)
    return lmp


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)

    dt = this_year - target_date
    return dt.days


def print_due_date_information(min_due_date, max_due_date, expected_due_date):

    print("Your expected due date is", expected_due_date.strftime('%a, %b %d %Y.'))
    print("Your expected due date may be as early as", min_due_date.strftime('%m/%d/%Y.'))
    print("Your expected due date may be as late as", max_due_date.strftime('%m/%d/%Y.'))


def main():
    print_header()
    lmp_day = get_lmp_from_patient()
    gest_length = datetime.timedelta(days=281)
    gest_std = datetime.timedelta(days=13)
    # today = datetime.date.today()

    exp_due_date = lmp_day + gest_length
    min_due_date = exp_due_date - gest_std
    max_due_date = exp_due_date + gest_std

    # number_of_days = compute_days_between_dates(bday, today)
    print_due_date_information(min_due_date, max_due_date, exp_due_date)


main()
