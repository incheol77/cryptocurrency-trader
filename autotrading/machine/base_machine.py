from abc import ABC, abstractmethod

class Machine(ABC):
    #--------------------#
    #     Public APIs    #
    #--------------------#
    @abstractmethod
    def get_ticker(self):
        """method for getting last ticker info"""
        pass

    @abstractmethod
    def get_transaction_history(self):
        """method for getting transaction history"""
        pass

    @abstractmethod
    def get_order_request(self):
        """method for getting current order request"""
        pass

    #--------------------#
    #    Private APIs    #
    #--------------------#

    '''
    @abstractmethod
    def get_wallet_status(self):
        """method for getting user's wallet info"""
        pass

    @abstractmethod
    def get_token(self):
        """method for getting access token info"""
        pass

    @abstractmethod
    def set_token(self):
        """method for making access token info"""
        pass

    @abstractmethod
    def get_username(self):
        """method for getting username"""
        pass

    @abstractmethod
    def buy_order(self):
        """method for executing buy order"""
        pass

    @abstractmethod
    def sell_order(self):
        """method for executing sell order"""
        pass

    @abstractmethod
    def cancel_order(self):
        """method for canceling order"""
        pass

    @abstractmethod
    def get_my_order_status(self):
        """method for getting order status info"""
        pass
    '''