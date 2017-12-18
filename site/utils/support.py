
import random

def random_list_contact():
    linkedin = """<a href="https://www.linkedin.com/in/%D1%81%D0%B5%D1%80%D0%B3%D0%B5%D0%B9-%D0%BA%D1%83%D1%80%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2-3bbb6165/" class="fa fa-linkedin"></a>"""
    github = """<a href="https://github.com/cnolick" class="fa fa-github"></a>"""
    twitter = """<a href="https://twitter.com/cnolick" class="fa fa-twitter"></a>"""
    facebook = """<a href="https://www.facebook.com/sergey.kurbanov.54" class="fa fa-facebook"></a>"""
    mail = """<a href="mailto:snkurban@infobra.ru" class="fa fa-envelope"></a>"""
    foo = [linkedin, github, twitter, facebook, mail]
    random.shuffle(foo)
    return  foo

