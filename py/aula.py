cp = [9, 5, 7]

challenge= [85, 100]

global_solution = 90

cps_soma = sum(cp)
menor_nota_cp = min(cp)
cps_media = (cps_soma - menor_nota_cp) / 2


challenge = sum(challenge)
challenge_media = challenge / 2

meida_geral = (cps_media + challenge_media + global_solution) / 3

print(f"Média geral: {meida_geral}")
