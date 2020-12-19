

from service.models import User
from service.utility.DataValidator import DataValidator
from .BaseService import BaseService

'''
It contains User business logics.   
'''
class UserService(BaseService):

    def authenticate(self,params):
        userList = self.search(params) 
        if (userList.count() > 0):
            for userData in userList:
                print("-----------------llll--------->",params['login_id'],"         --",userData.login_id)
                if(params['login_id']==userData.login_id):
                    #print("-----------------llll--------->",userData)
                    return userData
        else:
            return None
     
    def search(self,params):

        q = self.get_model().objects.filter()

        val = params.get("id",None)
        if( DataValidator.isInt(val)):
            q= q.filter( id = val)

        val = params.get("firstName",None)
        if( DataValidator.isNotNull(val)):
            q= q.filter( firstName = val)

        val = params.get("lastName",None)
        if( DataValidator.isNotNull(val)):
            q= q.filter( lastName = val)

        val = params.get("login_id",None)
        if( DataValidator.isNotNull(val)):
            q= q.filter( login_id = val)

        val = params.get("password",None)
        if( DataValidator.isNotNull(val)):
            q= q.filter( password = val)

        return q
    def get_login_id(self,login_id):
        self.get_model().objects.all()



    def get_model(self):
        return User
