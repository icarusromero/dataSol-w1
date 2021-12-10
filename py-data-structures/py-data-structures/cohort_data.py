"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> all_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    houselist = []


    # TODO: replace this with your code

    filename = open(filename)
    
    for line in filename:
          split_line = line.split('|')
          house = split_line[2]
          if house != '':
                houselist.append(house)
    filename.close()
    
    houses = set(houselist)

    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    filename = open(filename)
    students = []

    def pick(cohort):
          for line in filename:
            split_line = line.split('|')
            if split_line[4].__contains__(cohort):
                  student = f'{split_line[0]} {split_line[1]}'
                  students.append(student)

    if cohort == 'All':
          for line in filename:
            split_line = line.split('|')
            if split_line[2] != '':
                  student = f'{split_line[0]} {split_line[1]}'
                  students.append(student)
    elif cohort == 'Fall 2015':
          pick('Fall 2015')
    elif cohort == 'Winter 2016':
          pick('Winter 2016')
    elif cohort == 'Spring 2016':
          pick('Spring 2016')
    elif cohort == 'Summer 2016':
          pick('Summer 2016')

    filename.close()
    # TODO: replace this with your code

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    # TODO: replace this with your code
    filename = open(filename)

    for line in filename:
          split_line = line.split('|')
          if split_line[4].__contains__('I'):
                teacher = f'{split_line[0]} {split_line[1]}'
                instructors.append(teacher)
          elif split_line[4].__contains__('G'):
                ghost = f'{split_line[0]} {split_line[1]}'
                ghosts.append(ghost)
          elif split_line[2] == 'Gryffindor':
                  student = f'{split_line[0]} {split_line[1]}'
                  gryffindor.append(student)
          elif split_line[2] == 'Hufflepuff':
                  student = f'{split_line[0]} {split_line[1]}'
                  hufflepuff.append(student)
          elif split_line[2] == 'Ravenclaw':
                  student = f'{split_line[0]} {split_line[1]}'
                  ravenclaw.append(student)
          elif split_line[2] == 'Slytherin':
                  student = f'{split_line[0]} {split_line[1]}'
                  slytherin.append(student)
          elif split_line[2] == 'Dumbledore\'s Army':
                  student = f'{split_line[0]} {split_line[1]}'
                  dumbledores_army.append(student)

    filename.close()

    return [sorted(dumbledores_army), sorted(gryffindor), sorted(hufflepuff), sorted(ravenclaw), sorted(slytherin), sorted(ghosts), sorted(instructors)]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    # TODO: replace this with your code
    filename = open(filename)

    for line in filename:
          line = line.strip('\n')
          split_line = line.split('|')
          tupled = (split_line[0] + " " + split_line[1], split_line[2], split_line[3], split_line[4])
          all_data.append(tupled)

    filename.close()

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Someone else')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    # TODO: replace this with your code
    filename = open(filename)

    for line in filename:
          line = line.strip('\n')
          split_line = line.split('|')
          person = f'{split_line[0]} {split_line[1]}'
          if person == name:
                return split_line[4]

    filename.close()
    return 'None'


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    # TODO: replace this with your code
    filename = open(filename)

    last_names = []
    import collections

    for line in filename:
          split_line = line.split('|')
          last_names.append(split_line[1])
    duplicates = [item for item, count in collections.Counter(last_names).items() if count > 1]

    filename.close()
    return duplicates


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: replace this with your code\
    filename = open(filename)

    house = ''
    cohort = ''
    housemates = []

    for line in filename:
          split_line = line.split('|')
          person = f'{split_line[0]} {split_line[1]}'
          if person == name:
                if split_line[2] != '':
                      house = split_line[2]
                      cohort = split_line[4].strip('\n')

    filename.close()

    filename2 = open(filename)

    for line in filename2:
          print(line)
          split_line = line.split('|')
          student = f'{split_line[0]} {split_line[1]}'
          # if split_line[2] == house and split_line[4] == cohort:
          #       housemates.append(student)
    # print(housemates)
    # filename.close()
    # return housemates


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
