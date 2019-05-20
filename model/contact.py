from sys import maxsize

class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None,
                       title=None, company=None, address=None, home_phone=None, mobile_phone=None,
                       work_phone=None, fax=None, email=None, email_2=None, email_3=None,
                       homepage=None, birth_day=None, birth_month=None, birth_year=None,
                       anniversary_day=None, anniversary_month=None, anniversary_year=None,
                       sec_address=None, sec_home=None, sec_notes=None, id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.sec_address = sec_address
        self.sec_home = sec_home
        self.sec_notes = sec_notes
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
