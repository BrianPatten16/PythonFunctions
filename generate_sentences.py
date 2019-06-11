def generate_sentence(subjects, predicates, objects):
    """This function takes three lists of string as arguments
       This function returns a string that contains all the possible
       sentences in alphabetical order that can be constructed using the
        provided subjects, predicates and objects. Each sentence ends with
        a full stop "." and sentences are separated by a space"""
    subjects.sort()
    predicates.sort()
    objects.sort()
    finished_sentence = ''
    for sub in subjects:
        for pred in predicates:
            for obj in objects:
                sentence = sub + ' ' + pred + ' ' + obj + "." + " "
                finished_sentence += sentence

    return finished_sentence
