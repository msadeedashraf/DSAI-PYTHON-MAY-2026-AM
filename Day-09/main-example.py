def  check_grade(score, attendance,submitted):
    if score >= 60:
        if attendance >= 80:
            if submitted:
                print("Pass with good standing")
            else:
                print("Pass but missing assignment")
        else:
            print("Pass but low attendance")
    else:
        print("Fail")


def main():

    
    check_grade(80,85,True)

main()

    