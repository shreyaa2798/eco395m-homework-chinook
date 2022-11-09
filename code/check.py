import traceback
from pprint import pformat

import pandas as pd

from database import engine
from queries import *


def check(name, observed, expected):

    p_observed = pformat(observed)
    p_expected = pformat(expected)

    correct = observed == expected

    if not correct:
        print(
            f"Case Wrong! | For {name}: Expected={p_expected}, Observed={p_observed}."
        )
    else:
        print(
            f"Case Correct! | For {name}: Expected={p_expected}, Observed={p_observed}."
        )

    return correct


def grade_1():

    print("*" * 50)
    print("PROBLEM 1")

    try:

        df = pd.read_sql_query(query_1, engine)

        # case 1
        observed = df.loc[0, "count"]
        expected = 275
        case_1_correct = check("count", observed, expected)

        all_cases_correct = all([case_1_correct])

        if all_cases_correct:
            print("PROBLEM CORRECT!")
        else:
            print("PROBLEM INCORRECT!")

        return all_cases_correct

    except Exception as e:
        print("An Error has Occurred while grading PROBLEM:")
        traceback.print_exc()
        print("PROBLEM INCORRECT!")
        return False


def grade_2():

    print("*" * 50)
    print("PROBLEM 2")

    try:

        df = pd.read_sql_query(query_2, engine)

        # case 1
        observed = df.loc[0, "count"]
        expected = 71
        case_1_correct = check("count", observed, expected)

        all_cases_correct = all([case_1_correct])

        if all_cases_correct:
            print("PROBLEM CORRECT!")
        else:
            print("PROBLEM INCORRECT!")

        return all_cases_correct

    except Exception as e:
        print("An Error has Occurred while grading PROBLEM:")
        traceback.print_exc()
        print("PROBLEM INCORRECT!")
        return False


def grade_3():

    print("*" * 50)
    print("PROBLEM 3")

    try:

        df = pd.read_sql_query(query_3, engine)

        # case 1
        observed = df.loc[0, "count"]
        expected = 0
        case_1_correct = check("count", observed, expected)

        all_cases_correct = all([case_1_correct])

        if all_cases_correct:
            print("PROBLEM CORRECT!")
        else:
            print("PROBLEM INCORRECT!")

        return all_cases_correct

    except Exception as e:
        print("An Error has Occurred while grading PROBLEM:")
        traceback.print_exc()
        print("PROBLEM INCORRECT!")

        return False


def grade_4():

    print("*" * 50)
    print("PROBLEM 4")

    try:

        df = pd.read_sql_query(query_4, engine)

        # case 1
        observed = set(df["AC/DC Tracks"].values)
        expected = {
            "C.O.D.",
            "Hell Ain't A Bad Place To Be",
            "Spellbound",
            "Problem Child",
            "Go Down",
            "Dog Eat Dog",
            "Night Of The Long Knives",
            "Inject The Venom",
            "Bad Boy Boogie",
            "Whole Lotta Rosie",
            "Evil Walks",
            "Overdose",
            "Snowballed",
            "Let's Get It Up",
            "Breaking The Rules",
            "For Those About To Rock (We Salute You)",
            "Let There Be Rock",
            "Put The Finger On You",
        }
        case_1_correct = check("count", observed, expected)

        all_cases_correct = all([case_1_correct])

        if all_cases_correct:
            print("PROBLEM CORRECT!")
        else:
            print("PROBLEM INCORRECT!")

        return all_cases_correct

    except Exception as e:
        print("An Error has Occurred while grading PROBLEM:")
        traceback.print_exc()
        print("PROBLEM INCORRECT!")

        return False


def grade_5():

    print("*" * 50)
    print("PROBLEM 5")

    try:
        df = pd.read_sql_query(query_5, engine)

        # case 1
        observed = df.loc[0, "Total Sales"]
        expected = 15.84
        case_1_correct = check("count", observed, expected)

        all_cases_correct = all([case_1_correct])

        if all_cases_correct:
            print("PROBLEM CORRECT!")
        else:
            print("PROBLEM INCORRECT!")

        return all_cases_correct

    except Exception as e:
        print("An Error has Occurred while grading PROBLEM:")
        traceback.print_exc()
        print("PROBLEM INCORRECT!")

        return False


def grade_6():

    print("*" * 50)
    print("PROBLEM 6")

    try:
        df = pd.read_sql_query(query_6, engine)
        series = df.set_index("Artist")["Total Sales"]

        # case 1
        observed = series["The Posies"]
        expected = 0.99
        case_1_correct = check("The Posies", observed, expected)

        # case 2
        observed = series["Billy Cobham"]
        expected = 3.96
        case_2_correct = check("Billy Cobham", observed, expected)

        # case 3
        observed = series["Philharmonia Orchestra & Sir Neville Marriner"]
        expected = 0.99
        case_3_correct = check(
            "Philharmonia Orchestra & Sir Neville Marriner", observed, expected
        )

        # case 4
        observed = series.max() <= 5
        expected = True
        case_4_correct = check('Max("Total Sales") <= 5', observed, expected)

        all_cases_correct = all(
            [case_1_correct, case_2_correct, case_3_correct, case_4_correct]
        )

        if all_cases_correct:
            print("PROBLEM CORRECT!")
        else:
            print("PROBLEM INCORRECT!")

        return all_cases_correct

    except Exception as e:
        print("An Error has Occurred while grading PROBLEM:")
        traceback.print_exc()
        print("PROBLEM INCORRECT!")

        return False


def grade_7():

    print("*" * 50)
    print("PROBLEM 7")

    try:
        df = pd.read_sql_query(query_7, engine)
        series = df.set_index("Artist")["Total Sales"]

        # case 1
        observed = series["The Posies"]
        expected = 0.99
        case_1_correct = check("The Posies", observed, expected)

        # case 2
        observed = series["Billy Cobham"]
        expected = 3.96
        case_2_correct = check("Billy Cobham", observed, expected)

        # case 3
        observed = series["Philharmonia Orchestra & Sir Neville Marriner"]
        expected = 0.99
        case_3_correct = check(
            "Philharmonia Orchestra & Sir Neville Marriner", observed, expected
        )

        # case 4
        observed = (series.diff().dropna() <= 0).all()
        expected = True
        case_4_correct = check("Sorted Desc", observed, expected)

        all_cases_correct = all(
            [case_1_correct, case_2_correct, case_3_correct, case_4_correct]
        )

        if all_cases_correct:
            print("PROBLEM CORRECT!")
        else:
            print("PROBLEM INCORRECT!")

        return all_cases_correct

    except Exception as e:
        print("An Error has Occurred while grading PROBLEM:")
        traceback.print_exc()
        print("PROBLEM INCORRECT!")

        return False


def grade_8():

    print("*" * 50)
    print("PROBLEM 8")

    try:
        df = pd.read_sql_query(query_8, engine)

        # case 1
        observed = set(df["Name"].values)
        expected = {"King, Robert", "Callahan, Laura"}
        case_1_correct = check("Names", observed, expected)

        # case 2
        observed = df.set_index("Name")["Title"]["King, Robert"]
        expected = "IT Staff"
        case_2_correct = check("King, Robert", observed, expected)

        all_cases_correct = all([case_1_correct, case_2_correct])

        if all_cases_correct:
            print("PROBLEM CORRECT!")
        else:
            print("PROBLEM INCORRECT!")

        return all_cases_correct

    except Exception as e:
        print("An Error has Occurred while grading PROBLEM:")
        traceback.print_exc()
        print("PROBLEM INCORRECT!")

        return False


def grade_9():

    print("*" * 50)
    print("PROBLEM 9")

    try:
        df = pd.read_sql_query(query_9, engine)

        row = df.loc[lambda df_: df_["Employee Name"] == "Park, Margaret", :].squeeze()

        # case 1
        observed = row["Employee Name"]
        expected = "Park, Margaret"
        case_1_correct = check("Employee Name", observed, expected)

        # case 2
        observed = row["Employee Title"]
        expected = "Sales Support Agent"
        case_2_correct = check("Employee Title", observed, expected)

        # case 3
        observed = row["Manager Name"]
        expected = "Edwards, Nancy"
        case_3_correct = check("Manager Name", observed, expected)

        # case 4
        observed = row["Manager Title"]
        expected = "Sales Manager"
        case_4_correct = check("Manager Title", observed, expected)

        all_cases_correct = all(
            [case_1_correct, case_2_correct, case_3_correct, case_4_correct]
        )

        if all_cases_correct:
            print("PROBLEM CORRECT!")
        else:
            print("PROBLEM INCORRECT!")

        return all_cases_correct

    except Exception as e:
        print("An Error has Occurred while grading PROBLEM:")
        traceback.print_exc()
        print("PROBLEM INCORRECT!")

        return False


def grade_10():

    print("*" * 50)
    print("PROBLEM 10")

    try:
        df = pd.read_sql_query(query_10, engine)

        row = df.loc[0, :].squeeze()

        # case 1
        observed = row["Name"]
        expected = "Callahan, Laura"
        case_1_correct = check("Name", observed, expected)

        # case 2
        observed = row["Hire Date"]
        expected = pd.Timestamp("2004-03-04 00:00:00")
        case_2_correct = check("Hire Date", observed, expected)

        all_cases_correct = all([case_1_correct, case_2_correct])

        if all_cases_correct:
            print("PROBLEM CORRECT!")
        else:
            print("PROBLEM INCORRECT!")

        return all_cases_correct

    except Exception as e:
        print("An Error has Occurred while grading PROBLEM:")
        traceback.print_exc()
        print("PROBLEM INCORRECT!")

        return False


def grade_11():

    print("*" * 50)
    print("PROBLEM 11")

    try:
        df = pd.read_sql_query(query_11, engine)

        row = df.loc[lambda df_: df_["First Name"] == "Margaret", :].squeeze()

        # case 1
        observed = row["First Name"]
        expected = "Margaret"
        case_1_correct = check("First Name", observed, expected)

        # case 2
        observed = row["Last Name"]
        expected = "Park"
        case_2_correct = check("Last Name", observed, expected)

        # case 3
        observed = row["Tenure"].days
        expected = 2435
        case_3_correct = check("Tenure (Days)", observed, expected)

        all_cases_correct = all([case_1_correct, case_2_correct, case_3_correct])

        if all_cases_correct:
            print("PROBLEM CORRECT!")
        else:
            print("PROBLEM INCORRECT!")

        return all_cases_correct

    except Exception as e:
        print("An Error has Occurred while grading PROBLEM:")
        traceback.print_exc()
        print("PROBLEM INCORRECT!")

        return False


def grade_12():

    print("*" * 50)
    print("PROBLEM 12")

    try:
        df = pd.read_sql_query(query_12, engine)

        series = df["Tenure"].apply(lambda date: date.days)
        row = df.loc[0, :].squeeze()
        print(row)

        # case 1
        observed = (series.diff().dropna() >= 0).all()
        expected = True
        case_1_correct = check("Sorted Asc", observed, expected)

        # case 2
        observed = row["Last Name"]
        expected = "Callahan"
        case_2_correct = check("Last Name", observed, expected)

        # case 3
        observed = row["Tenure"].days
        expected = 2129
        case_3_correct = check("Tenure (Days)", observed, expected)

        all_cases_correct = all([case_1_correct, case_2_correct, case_3_correct])

        if all_cases_correct:
            print("PROBLEM CORRECT!")
        else:
            print("PROBLEM INCORRECT!")

        return all_cases_correct

    except Exception as e:
        print("An Error has Occurred while grading PROBLEM:")
        traceback.print_exc()
        print("PROBLEM INCORRECT!")

        return False


if __name__ == "__main__":
    results = [
        grade_1(),
        grade_2(),
        grade_3(),
        grade_4(),
        grade_5(),
        grade_6(),
        grade_7(),
        grade_8(),
        grade_9(),
        grade_10(),
        grade_11(),
        grade_12(),
    ]

    num_correct = sum(results)
    num_problems = len(results)

    print("=" * 100)
    print(f"{num_correct} out of {num_problems} problems")
    print("=" * 100)
