import requests
import bs4
import csv

file1 = open("Marks.csv", "w", newline='')
file_writer = csv.writer(file1)
file1.seek(0)

base_url = "http://results.vtu.ac.in/cbcs_17/result_page.php?usn=1pe15is"
levels = [0, 0, 0, 0, 40, 45, 50, 60, 70, 80, 90, 100]
grades = [0, 0, 0, 0, 4, 5, 6, 7, 8, 9, 10]
multiplier = [4, 4, 4, 4, 4, 4, 2, 2]

def get_grade(myMark):
    temp = 0
    for i in range(11):
        if(int(myMark) >= levels[i]):
            temp = grades[i]
        else:
            break
    return temp

def get_sgpa(myMarks):
    Sum = 4*10*7
    mySum = 0
    myGrades = []
    for i in range(8):
        myGrade = get_grade(myMarks[i])
        myGrades.append(myGrade)
        mySum += myGrade * multiplier[i]
    return str(round(mySum*10/Sum, 2))


for i in range(1, 200):
    try:
        url = base_url + ("{0:0=3d}".format(i))
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')

        temp_soup = str(soup)
        if "alert(\"University Seat Number is not available or Invalid..!\");" in temp_soup:
            continue

        j = 1
        student_name = (soup.find_all('tr')[1].find_all('td')[1].renderContents().strip()).decode("utf-8").replace("<b>:</b> ", "")
        USN = (soup.find_all('tr')[0].find_all('td')[1].renderContents().strip()).decode("utf-8").replace("<b> :</b> ", "").upper()
        final_marks = []
        for tr_tag in soup.find_all('tr')[3:]:
            final_marks.append((tr_tag.find_all('td')[4].renderContents().strip()).decode('utf-8'))
            if j == 8:
                break
            j += 1

        sgpa = get_sgpa(final_marks)
        row = [USN, student_name]
        row.extend(final_marks)
        row.append(sgpa)
        file_writer.writerow(row)

        print(str(i) + " done")
    except:
        continue
