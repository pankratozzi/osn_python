# default params
def user_data(name='Bob', surname='Bobston', year=1988, home_town='Paris', email='123@mail.ru', phone_num='555-35-05'):
    print('\t%s %s was born %d and lives in %s. Send him mail %s or call %s' % (
    name, surname, year, home_town, email, phone_num))


# named params
def user_data_named(name, surname, year, home_town, email, phone_num):
    return ('\t%s %s was born %d and lives in %s. Send him mail %s or call %s' % (
    name, surname, year, home_town, email, phone_num))


# mixed arguments
def mixed(name, surname, year, *address, home_town='Rome'):
    return ('\t%s %s was born %d and lives in %s. Contacts: %s' % (name, surname, year, home_town, ', '.join(address)))


if __name__ == '__main__':
    user_data()
    user_data('Jim', 'Morrison')
    print(user_data_named(name='Bob', surname='Bobston', year=1990, home_town='Paris', email='123@mail.ru',
                          phone_num='555-35-05'))
    contacts = ('123@mail.ru', '555-25-05', '@bobby78')
    print(mixed('Bob', 'Bobston', 1987, *contacts, home_town='Paris'))
