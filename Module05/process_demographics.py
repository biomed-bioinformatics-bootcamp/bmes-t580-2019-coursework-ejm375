import csv
import os


def main():

    print_the_header()

    filename = get_filename()

    out_filename = filename + '.valid'

    age_min, age_max = get_age_cutoff()

    pat_sex = get_pat_sex()

    inf_length_min, inf_length_max = get_inf_length()

    pat_ther = get_pat_ther()

    pat_coin = get_pat_coin()

    num_pats = 0

    # Open file and start reader
    with open(filename, mode='r') as handle:
        reader = csv.DictReader(handle)

        with open(out_filename, mode='w') as out_handle:
            fields = ['PAT_NUM', 'SEX', 'AGE', 'INFECTION_LENGTH',
                      'ON_THERAPY', 'COINFECTION']
            writer = csv.DictWriter(out_handle, fields)

            writer.writeheader()

            for row in reader:
                pat_age = int(row['AGE'])
                pat_sex_req = str(row['SEX'])
                inf_length_req = int(row['INFECTION_LENGTH'])
                pat_ther_req = str(row['ON_THERAPY'])
                pat_coin_req = str(row['COINFECTION'])

                match_age = (pat_age > age_min) and (pat_age < age_max)
                match_sex = (pat_sex_req == pat_sex) or (pat_sex == "0")
                match_inf_length = (inf_length_req > inf_length_min) and (inf_length_req < inf_length_max)
                match_pat_ther = (pat_ther_req == pat_ther) or (pat_ther == "0")
                match_pat_coin = (pat_coin_req == pat_coin) or (pat_coin == "0")

                if match_age and match_sex and match_inf_length and match_pat_ther and match_pat_coin:
                    num_pats += 1
                    writer.writerow(row)

    while True:

        age_crit = age_min != -1 and age_max != 150
        sex_crit = pat_sex != "0"
        inf_crit = inf_length_min != -1 and inf_length_max != 520
        ther_crit = pat_ther != "0"
        coin_crit = pat_coin != "0"

        if age_crit or sex_crit or inf_crit or ther_crit or coin_crit:

            print('Based on the following criteria:')
            if age_crit:
                print(' - Age: [%i, %i]' % (age_min, age_max))
            if sex_crit:
                print(' - Sex: [%s]' % pat_sex)
            if inf_crit:
                print(' - Infection Length: [%i, %i]' % (inf_length_min, inf_length_max))
            if ther_crit:
                print(' - On therapy?: [%s]' % pat_ther)
            if coin_crit:
                print(' - Co-infection?: [%s]' % pat_coin)

            print('There are %i eligible patients.' % num_pats)
            break

        else:
            print("You've selected no criteria.")
            print('There are %i eligible patients.' % num_pats)
            break


def print_the_header():
    print('---------------------------------')
    print('      Process Demographics')
    print('---------------------------------')
    print()


def get_filename():

    filename = None
    while filename is None:

        filename = input('What is the /path/to/the/file? ')

        # Check if the filename exists.
        if not os.path.exists(filename):
            print('That file could not be found. Try again.')
            filename = None

    return filename


def get_age_cutoff():

    while True:

        age_input = input("Is the patient's age relevant to this study? ")
        age_input = age_input.lower().replace('es', '').replace('o', '')
        age_input = age_input.replace('y', 'Yes').replace('n', 'No')
        if age_input == "Yes":

            age_min, age_max = None, None

            while age_min is None:
                age_inp = input('What is the youngest age for the study? ')
                try:
                    age_min = int(age_inp)
                except ValueError:
                    print(age_inp + ' is not a number. Please try again')
                    continue

                if age_min < 18:

                    print('Ethics boards require special permission for youth cohort.')

                    override_age_input = input("Would you like to override the age requirement? ")
                    override_age_input = override_age_input.lower().replace('es', '').replace('o', '')
                    override_age_input = override_age_input.replace('y', 'Yes').replace('n', 'No')

                    while True:

                        if override_age_input == "Yes":
                            break
                        elif override_age_input == "No":
                            age_min = None
                            break
                        else:
                            print("Invalid input. Please try again.")
                            age_min = None
                            break

            while age_max is None:
                age_inp = input('What is the oldest age for the study? ')
                try:
                    age_max = int(age_inp)
                except ValueError:
                    print(age_inp + ' is not a number. Please try again')
                    continue

            return age_min, age_max
        elif age_input == "No":
            age_min = -1
            age_max = 150
            return age_min, age_max
        else:
            print("Invalid input. Please try again.")
            continue


def get_pat_sex():

    while True:

        sex_input = input("Is the patient's sex relevant to this study? ")
        sex_input = sex_input.lower().replace('es', '').replace('o', '')
        sex_input = sex_input.replace('y', 'Yes').replace('n', 'No')
        if sex_input == "Yes":
            while True:

                pat_sex = input('Please select the sex for participants, (e.g. Male, Female): ')
                pat_sex = pat_sex.lower().replace('ale', '').replace('em', '')
                pat_sex = pat_sex.replace('m', 'Male')
                pat_sex = pat_sex.replace('f', 'Female')

                if pat_sex == "Male":
                    return pat_sex
                elif pat_sex == "Female":
                    return pat_sex
                else:
                    print("Invalid input. Please try again.")
                    continue

            return pat_sex
        elif sex_input == "No":
            pat_sex = "0"
            return pat_sex
        else:
            print("Invalid input. Please try again.")
            continue


def get_inf_length():

    while True:

        inf_input = input("Is the patient's length of infection relevant to this study? ")
        inf_input = inf_input.lower().replace('es', '').replace('o', '')
        inf_input = inf_input.replace('y', 'Yes').replace('n', 'No')
        if inf_input == "Yes":

            inf_length_min, inf_length_max = None, None
            while inf_length_min is None:
                inf_length_inp = input('What is the minimum infection length? ')
                try:
                    inf_length_min = int(inf_length_inp)
                except ValueError:
                    print(inf_length_inp + ' is not a number. Please try again')
                    continue

            while inf_length_max is None:
                inf_length_inp = input('What is the maximum infection length? ')
                try:
                    inf_length_max = int(inf_length_inp)
                except ValueError:
                    print(inf_length_inp + ' is not a number. Please try again')
                    continue

            return inf_length_min, inf_length_max
        elif inf_input == "No":
            inf_length_min = -1
            inf_length_max = 520
            return inf_length_min, inf_length_max


def get_pat_ther():

    while True:
        ther_input = input("Is whether the patient is undergoing therapy relevant to this study? ")
        ther_input = ther_input.lower().replace('es', '').replace('o', '')
        ther_input = ther_input.replace('y', 'Yes').replace('n', 'No')
        if ther_input == "Yes":
            while True:

                pat_ther = input('Should the patient be on therapy? [Yes or No]: ')
                pat_ther = pat_ther.lower().replace('es', '').replace('o', '')
                pat_ther = pat_ther.replace('y', 'Yes').replace('n', 'No')

                if pat_ther == "Yes":
                    return pat_ther
                elif pat_ther == "No":
                    return pat_ther
                else:
                    print("Invalid input. Please try again.")
                    continue
        elif ther_input == "No":
            pat_ther = "0"
            return pat_ther
        else:
            print("Invalid input. Please try again.")
            continue


def get_pat_coin():

    while True:
        coin_input = input("Is whether the patient has a co-infection relevant to this study? ")
        coin_input = coin_input.lower().replace('es', '').replace('o', '')
        coin_input = coin_input.replace('y', 'Yes').replace('n', 'No')
        if coin_input == "Yes":
            while True:

                pat_coin = input('Should the patient have a co-infection? [Yes or No]: ')
                pat_coin = pat_coin.lower().replace('es', '').replace('o', '')
                pat_coin = pat_coin.replace('y', 'Yes').replace('n', 'No')

                if pat_coin == "Yes":
                    return pat_coin
                elif pat_coin == "No":
                    return pat_coin
                else:
                    print("Invalid input. Please try again.")
                    continue
        elif coin_input == "No":
            pat_coin = "0"
            return pat_coin
        else:
            print("Invalid input. Please try again.")
            continue


if __name__ == '__main__':
    main()
