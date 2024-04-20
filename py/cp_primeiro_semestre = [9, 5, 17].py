cp_1 = [9, 5, 7]
cp_2 = [8, 6, 9]

challenge_primeiro_1 = [85]
challenge_primeiro_2 = [100]

challenge_segundo_1 = [95]
challenge_segundo_2 = [90]

global_solution_primeiro_semestre = 90
global_solution_segundo_semestre = 92

cp_1.remove(min(cp_1))
cp_1_media = cp_1[0] * 0.1
cp_1_media = cp_1[1] * 0.1

cp_2.remove(min(cp_2))
cp_2_media = cp_2[0] * 0.1
cp_2_media = cp_2[1] * 0.1


challenge_primeiro_media = sum(challenge_primeiro_1 + challenge_primeiro_2) / 2 * 0.1
challenge_segundo_media = sum(challenge_segundo_1 + challenge_segundo_2) / 2 * 0.1

meida_geral_primeiro_semestre = cp_1_media + cp_2_media + challenge_primeiro_media + global_solution_primeiro_semestre * 0.6

cp_1.remove(min(cp_1))
cp_1_media = cp_1[0] * 0.1

cp_2.remove(min(cp_2))
cp_2_media = cp_2[0] * 0.1

challenge_primeiro_media = sum(challenge_primeiro_1 + challenge_primeiro_2) / 2 * 0.1
challenge_segundo_media = sum(challenge_segundo_1 + challenge_segundo_2) / 2 * 0.1

meida_geral_segundo_semestre = cp_1_media + cp_2_media + challenge_primeiro_media + challenge_segundo_media + global_solution_segundo_semestre * 0.6

media_final = (meida_geral_primeiro_semestre * 0.4) + (meida_geral_segundo_semestre * 0.6)

print(f"Média final: {media_final}")