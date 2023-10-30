#!/usr/bin/env python3
# created october 30th 2023 by Declan Moher


import constants


def main():
    # asks for age of user
    user_age_str = input("Enter age:")

    try:
        # converts age into integer
        user_number = int(user_age_str)
    except ValueError:
        # if that can't this will print
        print(f"{user_age_str} is not a valid age")
    else:
        # if it's lower than 0 this will print
        if user_number < 0:
            print(f"{user_number} is not a valid age")

        elif user_number >= 122:
            # if this greater or equal to 122 this will print
            print(f" {user_number} is not a valid age.")

        elif user_number >= constants.VOTING_USA and constants.VOTING_CANADA:
            # if age is above 21 and 18
            print(f"at age {user_number} you can vote in AMERICA.")
            print(f"at age {user_number} you can vote in THE GREAT WHITE NORTH.")

        elif user_number >= constants.VOTING_CANADA:
            # if under age of 21 then this will print
            print(f"at age {user_number} you can vote in THE GREAT WHITE NORTH.")

    finally:
        # when code is done running it will print no matter what
        print("")


if __name__ == "__main__":
    main()
