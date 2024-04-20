cp_primeiro_semestre = [9, 5, 7]
cp_segundo_semestre = [8, 6, 9]

challenge_primeiro_semestre = [85, 100]
challenge_segundo_semestre = [90, 95]

global_solution_primeiro_semestre = 90
global_solution_segundo_semestre = 92

# Calcula a média do primeiro semestre
cp_soma_primeiro_semestre = sum(cp_primeiro_semestre)
menor_nota_cp_primeiro_semestre = min(cp_primeiro_semestre)
cp_media_primeiro_semestre = (cp_soma_primeiro_semestre - menor_nota_cp_primeiro_semestre) / 2

challenge_soma_primeiro_semestre = sum(challenge_primeiro_semestre)
challenge_media_primeiro_semestre = challenge_soma_primeiro_semestre / 2

meida_geral_primeiro_semestre = (cp_media_primeiro_semestre + challenge_media_primeiro_semestre + global_solution_primeiro_semestre) / 3

# Calcula a média do segundo semestre
cp_soma_segundo_semestre = sum(cp_segundo_semestre)
menor_nota_cp_segundo_semestre = min(cp_segundo_semestre)
cp_media_segundo_semestre = (cp_soma_segundo_semestre - menor_nota_cp_segundo_semestre) / 2

challenge_soma_segundo_semestre = sum(challenge_segundo_semestre)
challenge_media_segundo_semestre = challenge_soma_segundo_semestre / 2

meida_geral_segundo_semestre = (cp_media_segundo_semestre + challenge_media_segundo_semestre + global_solution_segundo_semestre) / 3

# Calcula a média final
media_final = (meida_geral_primeiro_semestre * 0.4) + (meida_geral_segundo_semestre * 0.6)

print(f"Média final: {media_final}")