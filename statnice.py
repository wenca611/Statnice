"""
Státnice 2021/22.

University: VUT Brno
Faculty: FEKT
File name: statnice.py
Author: Václav Pastušek
Creation date: 2021/22
Python Version: 3.8
"""

# import standart libraries
try:
    import sys
    import random as rn
    import time as tim
    import math
    import cv2
    from tkinter import Tk
except ModuleNotFoundError as e:
    e.msg += """.\nBe careful, this module is standard and
should not be missing.
I recommend reinstalling Python."""
    raise ModuleNotFoundError(e) from None

# in Spyder you need define tha PATH (top right)
FILEPATH = "data/statnice.txt"
RESET = False  # POZOR resetuje všechny body a přírustek bodů
win = Tk()
SCREEN_X = win.winfo_screenwidth()
SCREEN_Y = win.winfo_screenheight()
win.withdraw()


def control_lines(lines):
    """
    Control lines.

    :param lines: lines
    :return: None
    """
    for index, line in enumerate(lines):
        if not line.startswith("#"):  # není koment
            len_line = len(line.split(':'))
            # přidání bodů a přírůstek bodů za lexémy
            if len_line == 2:
                lines[index] = line.replace("\n", "") + ":0:0\n"
            elif len_line == 3:  # jiný počet lexémů
                # bude vždy vypysovat jen první chybu a ostatní ignorovat XD
                print("chyba, 3 lexémy na řádku:", index+1)
                print("chceme 0,1,2 nebo 4")
                sys.exit(1)
            elif len_line > 4:
                # too much slov
                print("chyba, více jak 4 lexémy na řádku:", index+1)
                print("chceme 0,1,2 nebo 4")
                sys.exit(2)


def repeat_it(text, not_need_zero=False, f=None, lines=None):
    """
    Repeat input until I am satisfied.

    :param text: text
    :param not_need_zero: True/False
    :param f: file
    :param lines: lines
    :return:
    """
    while True:  # nekonečná smyčka
        try:
            inp_control = input(text)
            if inp_control in ["q", "x"]:  # ukončení
                break
            elif not_need_zero and inp_control == "0":
                1/0  # 1000 IQ a přitom lepší než GOTO XD
            else:
                if inp_control.isdigit():
                    if int(inp_control) < 0:
                        1/0  # -999 IQ
                    return int(inp_control)
                else:
                    1/0  # 420 IQ
        except (SyntaxError, ZeroDivisionError):
            print("zadej to znovu nebo x or q pro ukončení")

    if f:
        f.write("".join(lines))
        f.close()
    print("\nUkončil(a) jsi program, progres je na 99,98% uložen.")
    sys.exit(3)


def duplicates(data):
    """
    Control duplicates questions and answers.

    :param data: data
    :return: None
    """
    def control_dup(name, str_name):
        duplicates = []
        for index, word in enumerate(name):
            if name.count(word) > 1:
                if word in duplicates:
                    # kvůli sortu se ignoruje ta z nejvíce body !!!
                    print("duplikace "+str_name+":", word,
                          "na řádku:", data[index][0]+1)
                duplicates += [word]

        if duplicates:
            sys.exit(4)

    questions, answers = [elem[1] for elem in data], [elem[2] for elem in data]
    control_dup(questions, "otázky")
    control_dup(answers, "odpovědi")


def score(correct, loop_num):
    """
    Test assessment.

    :param correct: number
    :param loop_num: number
    :return: None
    """
    correct_percent = correct*100/loop_num
    score = 'F'
    if correct_percent < 30:
        score = 'F-'
    elif correct_percent < 40:
        score = 'F'
    elif correct_percent < 50:
        score = 'F+'
    elif correct_percent < 53:
        score = 'E-'
    elif correct_percent < 57:
        score = 'E'
    elif correct_percent < 60:
        score = 'E+'
    elif correct_percent < 63:
        score = 'D-'
    elif correct_percent < 67:
        score = 'D'
    elif correct_percent < 70:
        score = 'D+'
    elif correct_percent < 73:
        score = 'C-'
    elif correct_percent < 77:
        score = 'C'
    elif correct_percent < 80:
        score = 'C+'
    elif correct_percent < 83:
        score = 'B-'
    elif correct_percent < 87:
        score = 'B'
    elif correct_percent < 90:
        score = 'B+'
    elif correct_percent < 93:
        score = 'A-'
    elif correct_percent < 97:
        score = 'A'
    else:
        score = 'A+'

    print("Úspěšnost:", correct_percent, "%. Známka:", score+'.')


def open_image(q_num, image_Q, image_index_A, image_list_A, f=False,
               lines=False, all_choices=False):
    """
    Open image (jpg).

    :param q_num: question number
    :param image_Q: question image
    :param image_index_A: answers indexes
    :param image_list_A: answer list of images
    :param f: file
    :param lines: lines
    :param all_choices: all choices
    :return: False
    """
    try:
        if image_Q:
            img = cv2.imread("data\\"+image_Q+".jpg")
            x, y, _ = img.shape
            if x < 250:
                img = cv2.resize(img, (250, 250))
            cv2.imshow("Q "+q_num+image_Q+".jpg:", img)

        if image_list_A:
            for nth, index in enumerate(image_index_A):
                img = cv2.imread("data\\"+image_list_A[nth]+".jpg")
                cv2.namedWindow("A "+str(index)+") "+image_list_A[nth]+".jpg:")
                cv2.moveWindow("A "+str(index)+") "+image_list_A[nth]+".jpg:",
                               (20+index*250) % (SCREEN_X-250),
                               (SCREEN_Y-500-index*50))
                x, y, _ = img.shape
                if x < 250:
                    img = cv2.resize(img, (250, 250))
                cv2.imshow("A "+str(index)+") "+image_list_A[nth]+".jpg:", img)
    except cv2.error:
        print("\nZkontrolujte cestu k obrázku u otázky:")
        print(image_Q)
        print("\nNebo odpovědí:")
        [print(elem) for elem in image_list_A]
        cv2.destroyAllWindows()  # destroys the window showing image

        if f:
            f.write("".join(lines))
            f.close()
        sys.exit(6)

    cv2.waitKey(0)  # waits until a key is pressed
    cv2.destroyAllWindows()  # destroys the window showing image


def pymain():
    """
    Pymain function.

    :return: None
    """
    start = tim.perf_counter()
    print("""
Vítejte v alfa verzi programu
- varování: zálohujte si textový soubor s daty, v případě spadnutí
        programu při otevřeném souboru přijdete o data XD

- doporučení: program jde kdykoliv ukončit napsáním a potvrzením 'x' nebo 'q'
""")
    with open(FILEPATH, encoding="utf8") as f:
        lines = f.readlines()
    f.close()
    # kontrola řádků
    control_lines(lines)

    # výběr možností
    # počet kol
    loop_num = repeat_it("počet kol(1+)[best 10,20,50,100,500]: ", True)
    # počet odpovědí
    choose_num = repeat_it("počet odpovědí(1+)[best 4, 7, 10]: ", True)

    # data [[index-1, otázka, odpověď, body, přírustek bodů],...]
    # ignoruje komenty a 0 nebo 1 lexém
    data = [[index] + elem.split(":") for index, elem in enumerate(lines)
            if len(elem.split(':')) > 1 and not elem.startswith("#")]
    len_data = len(data)

    # výběrové číslo nemůže být větší než je počet otázek !!!
    choose_num = len_data if choose_num > len_data else choose_num

    # setřídění podle bodů
    data = sorted(data, key=lambda x: int(x[3]))

    # kontrola duplicitních otázek nebo odpovědí
    duplicates(data)

    f = open(FILEPATH, 'w', encoding="utf8")  # open file for write
    if RESET:  # POZOR RESET všech bodů na :0:0 !!!!!!!!!
        for index, line in enumerate(lines):
            if len(line.split(':')) > 1 and not line.startswith("#"):
                lines[index] = ":".join(line.split(":")[:2]) + ":0:0\n"

        f.write("".join(lines))
        f.close()
        print("Byl proveden reset bodů a přírustku bodů.")
        sys.exit(5)

    correct = 0
    incorrect_list = []
    image_index_A = []
    image_list_A = []

    # random ubrání bodů XD, pro zopakování i otázek s více body
    if len(data):
        bad_repeat = math.ceil(math.log(len(data)+1))
        for _ in range(bad_repeat):
            points = data[rn.randint(0, len(data)-1)][3]
            data[rn.randint(0, len(data)-1)][3] = str(int(points)-100)

    if len_data:  # 1 nebo více otázek
        # bodová váha
        points_weight = [int(elem[3]) for elem in data]
        print(points_weight, 69)
        # vybrání otázek a odpovědí
        QA_data = [[elem[1], elem[2]] for elem in data]
        # váhovaný náhodný generátor
        QA_data = rn.choices(
            population=QA_data,
            # zvýšení hodnoty nad 0 a převrácení hodnoty
            weights=list(map(lambda x: 1 / (x-min(points_weight) + 1) + 1,
                             points_weight)),
            # budu násobit data, pokud chci více kol, než je dat
            # nebo krát 1 -> data se nezvětší
            k=len_data*math.ceil(loop_num/len_data)
        )
        print()

        for i in range(loop_num):
            start_part = tim.perf_counter()
            image_Q, image_list_A, image_index_A = "", [], []
            Q_A = rn.randint(0, 1)
            print(str(i+1)+"/"+str(loop_num)+")", QA_data[i][Q_A]+": ")

            image_Q = QA_data[i][Q_A]
            if image_Q.startswith("[") and image_Q.endswith("]"):
                image_Q = image_Q[1:-1]
            else:
                image_Q = ""

            QA_data_without_correct_choice = QA_data.copy()
            correct_choice = QA_data_without_correct_choice.pop(i)
            incorrect_choice = rn.choices(
                population=QA_data_without_correct_choice,
                # zvýšení hodnoty nad 0 a převrácení hodnoty
                weights=list(range(len(QA_data_without_correct_choice))),
                k=choose_num-1
            )
            # správné číslo
            randnum = rn.randint(0, choose_num-1)
            incorrect_choice.insert(randnum, correct_choice)  # all_choice

            all_correct = [randnum]
            for j, elem in enumerate(incorrect_choice):
                if j == randnum:
                    continue

                if elem[not Q_A] == correct_choice[not Q_A]:  # stejné s Good
                    for _ in range(int(1e9)):
                        better_choice = rn.choices(incorrect_choice)
                        if better_choice == correct_choice:
                            continue
                        else:
                            incorrect_choice[j] = better_choice[0]
                            break
                    if elem[not Q_A] == correct_choice[not Q_A]:
                        all_correct += [j]

            for k, elem in enumerate(incorrect_choice):
                print(str(k)+")", incorrect_choice[k][not Q_A])
                image_A = incorrect_choice[k][not Q_A]
                if image_A.startswith("[") and image_A.endswith("]"):
                    image_list_A += [image_A[1:-1]]
                    image_index_A += [k]
            open_image(str(i+1)+"/"+str(loop_num)+") ", image_Q, image_index_A,
                       image_list_A, f, lines)

            guessed_number = repeat_it("Vyber správné číslo: ", False, f,
                                       lines)

            ###################################################################
            # vyhodňovací část
            c_flag = False  # correct flag
            if guessed_number in all_correct:
                c_flag = True
                print("correct".upper(), end="")
                correct += 1

            else:
                c_flag = False
                print("incorrect".upper(), "správné:", str(randnum)+")",
                      end="")
                incorrect_list += [correct_choice]

            # pozor je o 1 menší (indexace od 0)
            correct_index = [elem[0] for elem in data if [elem[1], elem[2]] ==
                             correct_choice][0]

            # vybraný řádek
            choosen_line = [elem for elem in data if elem[0] ==
                            correct_index][0]

            gain = int(choosen_line[4])
            if c_flag:  # správně
                if gain < 1e7:
                    gain += 1
                else:  # omezení, aby se nešlo do nekonečna
                    gain -= 1
            else:  # špatně
                if gain > 0:  # nad nulou ubírám za špatné odpovědi více bodů
                    gain = int((gain+1)/3)
                else:
                    gain -= 1

            choosen_line[3] = str(int(choosen_line[3])+gain)
            choosen_line[4] = str(gain)+"\n"

            lines[choosen_line[0]] = ":".join([choosen_line[1],
                                               choosen_line[2],
                                               choosen_line[3],
                                               choosen_line[4]])

            print(", čas úlohy:", round(tim.perf_counter() - start_part, 2),
                  "s")
            print("\n")

    # zapsání a zavření souboru
    f.write("".join(lines))
    f.close()

    full_time = round(tim.perf_counter() - start, 2)
    m, s = divmod(full_time, 60)
    h, m = divmod(m, 60)
    h, m = int(h), int(m)
    print("Celkový čas:", f'{h}:{m}:{s:2}', "h:m:s")
    print("Průměrný čas na úlohu:", round(full_time/loop_num, 2), "s")

    # Ohodnocení testu
    score(correct, loop_num)

    if incorrect_list:
        print("\nNeuhodnuté slova:")
        [print(elem) for elem in incorrect_list]

    print("\nCelkově nejhorší slova se zápornými body:")
    worst = [elem for elem in data if int(elem[3]) < 0]
    [print(elem[1], "=", elem[2], "- body:", elem[3]) for elem in worst]

    sys.exit(0)


if __name__ == "__main__":  # main
    pymain()
