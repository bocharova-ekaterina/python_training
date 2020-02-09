from sys import maxsize


class Client:

    def __init__(self, id=None, firstname=None, lastname=None, address=None,
                 home=None, mobile=None, work=None, phone2=None,
                 email=None, email2=None, email3=None, all_phones_from_home_page=None,
                 all_emails_from_home_page=None):
        self.firstname=firstname
        self.lastname=lastname
        self.address=address
        self.home=home
        self.mobile=mobile
        self.work=work
        self.phone2=phone2
        self.email=email
        self.email2=email2
        self.email3=email3
        self.id=id
        self.all_phones_from_home_page=all_phones_from_home_page
        self.all_emails_from_home_page=all_emails_from_home_page

    def __repr__(self):
        return "%s: %s; %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize