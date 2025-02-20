"""
Practice Problem Statement:
Mr. X wants to invest his money in a mutual fund which guarantees a stable return of 12% per annum.
Given a lump sum investment of X rupees, calculate the value of the total corpus over T years at 5 year intervals.
Extension: Assuming an average inflation rate of 7%, compute the inflation-adjusted value of the corpus.
"""

class InvestmentCalculator:
    """
    A calculator for computing the future corpus of a mutual fund investment.

    This class computes:
      - The final corpus after a specified number of years using compound interest.
      - The inflation-adjusted corpus value based on a given inflation rate.

    Attributes:
        principal_amount (float): The initial investment amount.
        interest_rate (float): The annual return rate (default is 12%).
        inflation_rate (float): The annual inflation rate (default is 7%).
        compound_frequency (int): The number of times interest is compounded per year (default is 1).
    """

    def __init__(self, principal_amount: float, 
                 interest_rate: float = 12.00, 
                 inflation_rate: float = 7.00, 
                 compound_frequency: int = 1):
        """
        Initializes the InvestmentCalculator with user-defined values.

        Args:
            principal_amount (float): The initial lump sum investment.
            interest_rate (float, optional): The annual interest rate in percentage (default is 12%).
            inflation_rate (float, optional): The annual inflation rate in percentage (default is 7%).
            compound_frequency (int, optional): Number of times interest is compounded per year (default is 1).
        """
        assert 0.05 <= principal_amount and isinstance(principal_amount, (int, float)), "Principal amount must be a positive number. (Also, the lowest ticket size in mutual funds is 5 paisa.)"
        assert 0 <= interest_rate <= 100 and isinstance(interest_rate, (int, float)), "Interest rate must be between 0 and 100"
        assert 0 <= inflation_rate <= 100 and isinstance(inflation_rate, (int, float)), "Inflation rate must be between 0 and 100"
        assert compound_frequency in {1, 2, 4, 12}, "Invalid compounding frequency"

        self.principal_amount = principal_amount
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal
        self.inflation_rate = inflation_rate / 100  # Convert percentage to decimal
        self.compound_frequency = compound_frequency

    def final_corpus(self, years: int) -> float:
        """
        Calculates the final corpus after a given number of years using compound interest.

        Formula:
            A = P (1 + r/n)^(nt)

        Args:
            years (int): The number of years for the investment.

        Returns:
            float: The final corpus value after applying compound interest.
        """
        return (self.principal_amount * 
                (1 + self.interest_rate / self.compound_frequency) ** 
                (self.compound_frequency * years))

    def inflation_adjusted_corpus(self, years: int) -> float:
        """
        Calculates the inflation-adjusted corpus value after a given number of years.

        Formula:
            Inflation Adjusted Corpus = Final Corpus / (1 + inflation_rate) ^ years

        Args:
            years (int): The number of years for the investment.

        Returns:
            float: The inflation-adjusted corpus value.
        """
        final_value = self.final_corpus(years)
        return final_value / ((1 + self.inflation_rate) ** years)

    def show_returns(self, years_list: list[int]) -> dict[int, tuple[float, float]]:
        """
        Computes and returns the final and inflation-adjusted corpus for each specified period.

        Args:
            years_list (list[int]): A list of investment durations in years.

        Returns:
            dict[int, tuple[float, float]]: 
                A mapping from each year to a tuple (final_corpus, inflation_adjusted_corpus).
        """
        returns = {}
        for years in years_list:
            final_val = self.final_corpus(years)
            adjusted_val = self.inflation_adjusted_corpus(years)
            returns[years] = (final_val, adjusted_val)
        return returns


if __name__ == "__main__":
    # Example usage with an investment of 100 rupees.

    try:
        user_input = input("Enter the investment amount (default is 100 rupees): ").strip()
        investment_amount = float(user_input) if user_input else 100
    except ValueError:
        print("Invalid input, using default value of 100 rupees.")
        investment_amount = 100

    investment = InvestmentCalculator(investment_amount)
    durations = list(range(1, 41, 5))
    results = investment.show_returns(durations)
    
    print(f"Results for an investment of {investment_amount} rupees at "
          f"{investment.interest_rate * 100:.2f}% interest per year with an average inflation rate of "
          f"{investment.inflation_rate * 100:.2f}%:")

    for years, (final_val, adj_val) in results.items():
        print(f"After {years} years: Final Corpus = {final_val:.2f}, Inflation-adjusted = {adj_val:.2f}")

"""
However, excessive commenting is also something which is not recommended as;
YOUR CODE SHOULD SPEAK FOR ITSELF in most of the cases especially the trivial ones.
PEP8 provided a certain set of recommendations however according to the core principles of python;
whatever that is simpler and better readable should be escalated over their counterparts.
"""