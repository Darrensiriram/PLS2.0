from controllers.LoanItemHelper import LoanItemHelper


class SubscriberHelper:

    @staticmethod
    def subscriber_loan_book(user):
        LoanItemHelper.loan_book(user)
    @staticmethod
    def subscriber_rent_book(user):
        LoanItemHelper.return_book(user)
