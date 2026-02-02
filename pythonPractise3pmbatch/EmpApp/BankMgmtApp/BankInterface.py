'''
in this interface including the details of person and input data
two method
'''

from abc import  abstractmethod,ABC
class BankMgmt(ABC):#Bank Interface Create
    @abstractmethod
    def DisaplyAccountHolderDetails(self):
        pass
