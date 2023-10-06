from dateutil.parser import parse
from dateutil.rrule import *
import datetime


def validate_date_format(passed_date):
    """ This function is used to we validate that the date is in a valid format,
    and that all fields have been provided.
    """
    default_1 = datetime.datetime.strptime('01/01/01', '%d/%m/%y')
    default_2 = datetime.datetime.strptime('02/02/02', '%d/%m/%y')
    # If any date value was not provided, the two valude of parsed date
    # will be different, because they use different defaults
    if parse(
        passed_date, dayfirst=True, default=default_1
        ) == parse(
            passed_date, dayfirst=True, default=default_2
            ):
        # If the values are the same it means that the full date was provided
        # and the two pased_values will match
        return passed_date


def validate_class(new_class):

    result = new_class
    errors = []
    start = None
    end = None

    # Check if all mandatory fields were provided
    mandatory_fields = ["id", "class_name", "capacity", "start_date", "end_date"]
    for field in mandatory_fields:
        if field not in new_class.keys():
            errors.append(f"Mandatory value not provided '{field}'")
        # For date fields we check if they are in a valid format
        if field == "start_date" or field == "end_date":
            try:
                valid_date = validate_date_format(new_class[f"{field}"])
                if(valid_date) != None:
                    new_class[f"{field}"] = valid_date
                else:
                    errors.append(
                        "Invalid date passed. Please enter the following format dd-mm-yyyy"
                        )
            except:
                errors.append("Invalid date passed")

    # If start_date and end_date are passed,
    # we also check if the selected date is valid
    if "start_date" in new_class.keys() and "end_date" in new_class.keys():
        try:
            start = parse(new_class["start_date"], dayfirst=True)
            end = parse(new_class["end_date"], dayfirst=True)
            today = parse(datetime.date.today().strftime('%d-%m-%Y'), dayfirst=True)
            # Start date should not be in the past
            if start < today:
                errors.append(f"Start date {start} cannot be in the past {today}")
            # end date should be after start date
            if start > end:
                errors.append("End date should be after start date")

        except:
            errors.append("Invalid date passed")

    # If there is any error, return them all
    if len(errors) > 0:
        result = {"error" : {
            "errors": errors
        }}

    return result


def check_dates(dates_tuple1, dates_tuple2):
    """ This function is used to validate if the date ranges provided
    are overlapping at any point
    """
    # Get the range 1 and 2 from the start, end date tuple 1 and 2
    # It returns a list of one date per day in range start, end
    range1 = list(rrule(DAILY, 
                      dtstart=parse(dates_tuple1[0], dayfirst=True),
                      until=parse(dates_tuple1[1], dayfirst=True)))
    
    range2 = list(rrule(DAILY, 
                      dtstart=parse(dates_tuple2[0], dayfirst=True),
                      until=parse(dates_tuple2[1], dayfirst=True)))
    # Returns True if any date is both in range 1 and 2
    return any(i in range2 for i in range1)


def calculate_dates_tuples(i, existing_classes):
    """ This function is used to return the tuples, that will be used
    in the validate_overlapping function.
    """
    return (existing_classes[f"{i}"]["start_date"], existing_classes[f"{i}"]["end_date"])


def validate_overlapping(new_class, existing_classes):
    """ This function is used to check if the new class overlaps with existing ones """

    start = new_class["start_date"]
    end = new_class["end_date"]
    tuple1 = (start, end)

    overlaps = False

    for i in range(len(existing_classes)):
        tuple2 = calculate_dates_tuples(i, existing_classes)
        if check_dates(tuple1, tuple2):
            overlaps = True

    return overlaps
