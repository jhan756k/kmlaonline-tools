# scp to srv/http/kmla/data/user_pending_list/
# python3 printnames.py

import os
for files in os.listdir("."):
    if files.endswith(".txt"):
        fi = open(files, "r")
        f = fi.read().lstrip()

        # name
        sind = f.index("s_kor_name")
        eind = f.index("s_eng_name")
        name = ['\\' + x for x in f[sind+13:eind-3].split("\\")]
        name.pop(0)
        for i in range(len(name)):
            name[i] = name[i].encode().decode('unicode-escape')
        print("".join(name), end="")

        # birth year
        sind = f.index("n_birth_date_yr")
        year = f[sind+18:sind+22] + "년생"
        print(", " + year, end="")

        fi.close()