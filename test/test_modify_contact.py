from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Del"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="EditedName", middle_name="EditedMiddleName", last_name="EditedLastName", nickname="EditedNickName", title="title", company="xb", address="spb", home_phone="111", mobile_phone="222", work_phone="333",
                                   fax="444", email="1@1.com", email_2="2@2.com", email_3="3@3.com", homepage="www.homepage.com", birth_day="12", birth_month="February", birth_year="1988", anniversary_day="13",
                                   anniversary_month="January", anniversary_year="2019", sec_address="secAddress", sec_home="secHome", sec_notes="secNotes")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

