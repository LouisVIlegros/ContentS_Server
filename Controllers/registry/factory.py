from Controllers.factory import autocomplete
from Controllers.factory import Users
mainFactory = {
    "search" : {
        "autocomplete" : autocomplete.SearchEngine,
        "byID" : Users.Users
    }
}
