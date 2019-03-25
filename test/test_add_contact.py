# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
        app.session.login(username="admin", password="secret")
        app.create_contact(Contact(first_name="Konstantin", middle_name="S.", last_name="Morozov", nickname= "koshtet", title="title", company="xb", address="spb", home_phone="111", mobile_phone="222", work_phone="333",
                            fax="444", email="1@1.com", email_2="2@2.com", email_3="3@3.com", homepage="www.homepage.com", birth_day="12", birth_month="February", birth_year="1988", anniversary_day="13",
                            anniversary_month="January", anniversary_year= "2019", sec_address="secAddress", sec_home="secHome", sec_notes="secNotes"))
        app.session.logout()
