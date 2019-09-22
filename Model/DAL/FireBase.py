from firebase import firebase



class FireBase :
    def __init__(self, searchData):
        self.baseURL = 'https://contentsquaresearch.firebaseio.com/'
        self.searchData = searchData
        self.instance = firebase.FirebaseApplication(self.baseURL, None)

    def getAll(self):
        return self.instance.get('/{}'.format(self.searchData), None)

    def getOne(self, id):
        return self.instance.get('/{}'.format(self.searchData), id)