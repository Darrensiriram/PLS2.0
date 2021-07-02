import controllers.PersonHelper as PersonHelper
import controllers.LoanItemHelper as LoanItemHelper


class LoanAdministrationHelper:

    @staticmethod
    def administration_loan_book():
        user = PersonHelper.PersonHelper.search_user()
        LoanItemHelper.LoanItemHelper.loan_book(user)

    @staticmethod
    def administration_return_book():
        user = PersonHelper.PersonHelper.search_user()
        LoanItemHelper.LoanItemHelper.return_book(user)
