from student import Student_info    # importing...

if __name__ == "__main__":
    st1 = Student_info("NARESH SHARMA",20,2002)         # we are creating a Naresh object of Student_info type class
    st2 = Student_info("RAWAL SAHRMA",23,1999)
    st3 = Student_info("KRAMLINGAM",23,1999)

    print("STUDENT 1 NAME IS - ",st1.name)
    print("STDUNET 1 AGE IS - ",st1.age)
    print("STUDENT 1 DATE_OF_BIRTH IS - ",st1.Birth_Year)
    print()
    print("STUDENT 2 NAME IS - ",st2.name)
    print("STDUNET 2 AGE IS - ",st2.age)
    print("STUDENT 2 DATE_OF_BIRTH IS - ",st2.Birth_Year)
    print()
    print("STUDENT 3 NAME IS - ",st3.name)
    print("STDUNET 3 AGE IS - ",st3.age)
    print("STUDENT 3 DATE_OF_BIRTH IS - ",st3.Birth_Year)
    print()

    st1.read()
    st2.read()
    st3.read()
    st1.write()
    st2.write()
    st3.write()
    print()

    st1.give_mcq()
