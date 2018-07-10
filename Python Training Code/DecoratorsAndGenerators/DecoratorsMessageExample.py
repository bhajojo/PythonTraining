def messageWithWelcome(str):
    # Nested function
    def addWelcome():
        return "Welcome to "

    # Return concatenation of addWelcome()
    # and str.
    return addWelcome() + str


# To get site name to which welcome is added
def site(site_name):
    return site_name


print messageWithWelcome(site("Google.com"))
