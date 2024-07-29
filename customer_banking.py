# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input('What is your Savings Account Balance?'))
    savings_interest = float(input('What is the APR for Savings Account?'))
    savings_maturity = int(input('What is the Length of Term?'))                     

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    # Display the savings account data.
    print('Here are the details of the savings account.')
    print("The balance is: $", format(savings_balance, ',.2f'))
    print("APR Interest Rate is: ", format(savings_interest, ',.2f'),"%")
    print(f"Length of CD is: {savings_maturity}months")
    print("Savings Interest Earned would be: $ ", format(interest_earned, ',.2f'))
    print(f"Your projected Savings balance will be: ${updated_savings_balance}")


    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input('What is your CD Account Balance?'))
    cd_interest = float(input('What is the APR for CD Account?'))
    cd_maturity = int(input('What is the Length of CD Term?'))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_cd_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print('Here are the details of the projected CD account.')
    print("The balance is: $", format(cd_balance, ',.2f'))
    print("APR Interest Rate is: ", format(cd_interest, ',.2f'),"%")
    print(f"Length of CD is: {cd_maturity}months")
    print("CD Interest Earned would be: $ ", format(interest_cd_earned, ',.2f'))
    print(f"Your projected CD balance will be: ${updated_cd_balance}")
    

if __name__ == "__main__":
   
# Call the main function.
    main ()


