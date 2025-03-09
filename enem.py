# Média enem student 1
score_1 = 680
score_2 = 720
score_3 = 650
score_Redação = 900

result_CD1 = ((score_1 + score_2 + score_3 + score_Redação) / 4)


# Média enem student 2

score_4 = 550
score_5 = 600
score_6 = 580
score_Redação_2 = 800

result_CD2 = ((score_4 + score_5 + score_6 + score_Redação_2) / 4)


# Média enem student 3

score_7 = 750
score_8 = 780
score_9 = 700
score_Redação_3 = 940

result_CD3 = ((score_7 + score_8 + score_9 + score_Redação_3) / 4)


# Média geral
Média_geral = (result_CD1 + result_CD2 + result_CD3) / 3


"""script do result
"""

print(f"""
     Média de Cada student: 
      \nstudent 1 = {result_CD1}, 
      \nstudent 2 = {result_CD2}, 
      \nCandidado 3 = {result_CD3}, 
      \nMédia geral = {Média_geral}
    """)
