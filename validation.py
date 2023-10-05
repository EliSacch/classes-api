from dateutil.parser import parse
import datetime


def validate_date_format(passed_date):
    # Here we validate that the date is in a valid format, and that all fields have been provided
    default_1 = datetime.datetime.strptime('01/01/01', '%d/%m/%y')
    default_2 = datetime.datetime.strptime('02/02/02', '%d/%m/%y')
    if parse(
        passed_date, dayfirst=True, default=default_1
        ) == parse(
            passed_date, dayfirst=True, default=default_2
            ):
        return passed_date


def validate_class(new_class):

    result = new_class
    errors = []

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

    # If there is any error, return them all
    if len(errors) > 0:
        result = {"error" : {
            "There were some errors in your request": errors
        }}


    return result
