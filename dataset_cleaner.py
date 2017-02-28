def clean_up_word(word, punctuations):
    if "<i>" in word:
        word = word.replace("<i>", "")

    for spl in punctuations.keys():
        if word and spl in word:
            word = word.replace(spl, "")

    if word and "$" in word:
        word = "<amount>"

    elif word and word.isdigit():
        if ("19" in word or "18" in word) and len(word) <= 5:
            word = "<year>"
        word = "<number>"

    if "?" in word:
        if not word[-1] == "?":
            print "QM = %s" % word

    # Check if it is time
    for c in word:
        if c.isdigit() and not word.isdigit():
            if "am" in word or "pm" in word:
                word = "<time>"
            # Check if is reference to 1st/2nd/3rd/4th
            elif "st" in word or "nd" in word or "rd" in word or "th" in word:
                word = "<number nth>"

            elif "'" in word:
                word = "<apos number>"

            elif ("ft" in word or "lbs" in word or "psi" in word or word[-1] == "s" or word[-1] == "m"):
                word = "<number units>"

            else:
                word = "<rand_number>"

    return word


def read_data(num_movie_scripts):
    punctuations = {"!": 1, ".": 1, "<": 1, ">": 1, ";": 1, ":": 1, "{": 1, "}": 1, "[": 1, "]": 1, "-": 1, "_": 1, "+": 1,
                "=": 1, "*": 1, "&": 1, "`": 1, "~": 1, "@": 1, "#": 1, "%": 1, "^": 1, "(": 1, ")": 1, "/": 1, "..": 1,
                "...": 1, "....": 1}
    data_tokens = []
    # Append each line in file to the set
    for i in range(0, num_movie_scripts):
        path = 'data/' + str(i) + 'raw.txt'
        raw = open(path, 'r+')
        print 'Reading ', path, '...'
        holder = ""
        for line in raw:
            this_line = line
            if "' il" in this_line:
                this_line = this_line.replace("' il", "'ll")
            if "' " in line:
                this_line = this_line.replace("' ", "'")
            if " ?" in line:
                this_line = this_line.replace(" ?", "?")

            new_line = ""
            for word in this_line:
                new_word = clean_up_word(word, punctuations)
                new_line += new_word
            holder += new_line
        raw.seek(0)
        raw.write(holder)
        raw.truncate()
        raw.close()

read_data(2318)
