

from abc import ABC,abstractmethod

class BaseService(ABC):
    def __init__(self):
        print("0")

    def get(self, mid):
        try:
            r = self.get_model().objects.get( id = mid )
            return r
        except self.get_model().DoesNotExist :
            return None

    def search(self):
        try:
            r = self.get_model().objects.all()
            return r
        except self.get_model().DoesNotExist :
            return None

    def save(self,m_obj):
        if(m_obj.id == 0):
            m_obj.id = None
        m_obj.save()
        
       
    def delete(self,mid):
        m = self.get(mid)
        m.delete() 
        return m

    def find_by_unique_key(self, mid):
        try:
            r = self.get_model().objects.get( id = mid )
            return r
        except self.get_model().DoesNotExist :
            return None

    @abstractmethod
    def get_model(self):
        pass



