from Model.DAL import FireBase as DAL

class Users :

    def __init__(self, id, dataType):
        self.id = str(int(id) -1)
        self.dataType = dataType


    def exec(self):

        return DAL.FireBase(self.dataType).getOne(self.id)