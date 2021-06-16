


class Calc:
    rental_income = input("What's your monthly rental income?: ")
    misc_1 = input(" Misc(Laundry, Storage, Other): ")
    total_income = rental_income + misc_1

    insurance = input("What's your insurance costs?: ")
    utilities = input("How much is spent on utilities yearly?(Electric, Water, Sewer, Garbage, Gas): ")
    hoa = input("HOA (Home Owner Association) Fees: ")
    repairs = input("How much have you spent on repairs?: ")
    mortgage = input("How much is your mortgage payments?: ")
    misc_2 = input("Misc(Vacancy, CapEx, Lawn/Snow, Tax, Property Manager): ")
    total_expenses = insurance + utilities + hoa + repairs + mortgage + misc_2

    monthly_cash_flow = int(total_income) - int(total_expenses)

    down_payment = input("Please Enter Down Payment Amount: ")
    closing_costs = input("Please input Closing Costs: ")
    rehab_budget = input("What's your rehab budget amount?: ")
    misc_3 = input("Misc(Other): ")

    total_investment = down_payment + closing_costs + rehab_budget + misc_3
    annual_cash_flow = monthly_cash_flow * 12
    percent = int(annual_cash_flow) / int(total_investment)
    roi = percent * 100
    print(str(roi) + ("%"))
# total_income = {}
#


# can't figure out how to use __init__ and change attributes without pycharm assuming my functions as a static method  :/
# income = input("")
#
# class Calc:
#     def __init__(self, rental_income, insurance, investment, tax, utilities, hoa, lawn_snow, vacancy, repairs):
#         self.rental_income = rental_income
#         self.insurance = insurance
#         self.investment = investment
#         self.tax = tax
#         self.utilities = utilities
#         self.hoa = hoa
#         self.lawn_snow = lawn_snow
#         self.vacancy = vacancy
#         self.repairs = repairs
#
#     def rental_income(self):
#     #Why is it a static method by default? does it think i forgot to call it as @staticmethod????
#         while True:
#             income = input("What's your monthly rental income?")
#         if self.rental_income.lower() == 'quit':
#             break            # outside of loop????
#         #if not self.rental_income.isdigit():
#           print("Please add numbers only")
#
