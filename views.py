class View():
    def view_type(self):
        return type(self).__name__

class ListView(View):
    pass # no operation

# implement these as empty classes such as we we did for ListView above:
# defining the class inheritance signature and providing an empty class body with the keyword *pass*
# DetailView descends from View
# SearchView is a DetailView
# SearchResultsView inherits from ListView and SearcView

# so this code can run
print(View().view_type())
print(ListView().view_type())
print(DetailView().view_type())
print(SearchView().view_type())
print(SearchResultsView().view_type())
