grade ={
"A+":	4.5,
"A0":	4.0,
"B+":	3.5,
"B0":	3.0,
"C+":	2.5,
"C0":	2.0,
"D+":	1.5,
"D0":	1.0,
"F":	0.0,
}
AllCredits = 0.0
AllScores = 0.0
for _ in range(20):
    _, credit, score = input().split()
    res = grade.get(score,'PASS')
    if res == 'PASS': continue
    AllScores += float(credit) * res
    AllCredits += float(credit)
print(round(AllScores / AllCredits,6))