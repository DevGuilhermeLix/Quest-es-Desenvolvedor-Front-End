import json


dados_faturamento = """
{
    "dias": [
        {"dia": 1, "valor": 221.55},
        {"dia": 2, "valor": 312.43},
        {"dia": 3, "valor": 0.00}, 
        {"dia": 4, "valor": 150.67},
        {"dia": 5, "valor": 180.34}
    ]
}
"""

dados = json.loads(dados_faturamento)
valores = [dia["valor"] for dia in dados["dias"] if dia["valor"] > 0]

menor = min(valores)
maior = max(valores)
media = sum(valores) / len(valores)
dias_acima_media = sum(1 for valor in valores if valor > media)

print(f"Menor valor de faturamento: R${menor:.2f}")
print(f"Maior valor de faturamento: R${maior:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
