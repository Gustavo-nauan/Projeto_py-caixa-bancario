import string #biblioteca com os caracteres de pontuação (usada na validação da senha)
from decimal import Decimal, InvalidOperation #Decimal faz cálculo exato com dinheiro (evita erro de arredondamento do float)

LIMITE_SAQUE_CENTAVOS = 200000 #limite máximo de saque por operação: R$ 2.000,00 (em centavos)

def obter_cpf(mensagem="Olá bem vindo de volta! Digite seu CPF(somente números):   "):
    while True:
        cpf = input(mensagem)
        cpf_limpo = cpf.replace(".", "").replace("-", "") #verifica se não tem pontuação no digitalizador
        if len(cpf_limpo) == 11 and cpf_limpo.isdigit(): 
            print("CPF Válido! Prosseguir ")#Caso esteja nos conformes pedidos irá validar
            return cpf_limpo
        else:
            print("  CPF inválido. Por favor, digite um CPF válido (11 dígitos).")#Caso não estiver ele inválida e repete novamente até validar 

def validar_senha(mensagem="Digite sua senha (OBS: Criar uma senha forte):   "):
    while True:
        senha = input(mensagem)
        erros = [] #guarda os requisitos que a senha ainda não cumpre
        if len(senha) < 8:
            erros.append("ter no mínimo 8 caracteres")
        if not any(c.isupper() for c in senha):
            erros.append("ter pelo menos uma letra maiúscula")
        if not any(c.islower() for c in senha):
            erros.append("ter pelo menos uma letra minúscula")
        if not any(c.isdigit() for c in senha):
            erros.append("ter pelo menos um número")
        if not any(c in string.punctuation for c in senha):
            erros.append("ter pelo menos um caractere especial (ex: !@#$)")
        if not erros: #se nenhum requisito faltar, a senha é válida
            print("Senha válida! Prosseguir ")
            return senha
        print("  Senha inválida. A senha deve " + ", ".join(erros) + ".")

def obter_valor(mensagem="Digite o valor (ex: 150 ou 1.234,56): "):
    while True:
        texto = input(mensagem).strip() #lê o valor digitado e remove espaços das pontas
        if "," in texto: #se tem vírgula, está no padrão brasileiro: 1.234,56
            texto = texto.replace(".", "").replace(",", ".") #tira o separador de milhar e troca a vírgula por ponto
        try:
            valor = Decimal(texto) #converte o texto para número exato
        except InvalidOperation: #caiu aqui se o texto não é um número (ex: "abc")
            print("  Valor inválido. Digite um número, ex: 150 ou 1.234,56.")
            continue #volta a pedir o valor
        if not valor.is_finite():
            print("  Valor inválido. Digite um número, ex: 150 ou 1.234,56.")
            continue
        if valor <= 0: #transação precisa de valor maior que zero (mesma regra do CHECK do banco)
            print("  O valor deve ser maior que zero.")
            continue
        if valor != valor.quantize(Decimal("0.01")): #se arredondar para centavos muda o valor, tem mais de 2 casas decimais
            print("  O valor pode ter no máximo 2 casas decimais.")
            continue
        return int(valor * 100) #converte para centavos (inteiro), que é como o banco guarda o dinheiro

def validar_saldo_suficiente(saldo_centavos, valor_centavos):
    if valor_centavos <= saldo_centavos: #saldo cobre a operação
        return True
    print("  Saldo insuficiente para essa operação.")
    return False

def validar_limite_saque(valor_centavos, limite_centavos=LIMITE_SAQUE_CENTAVOS):
    if valor_centavos <= limite_centavos: #valor não ultrapassa o limite por saque
        return True
    print("  Valor acima do limite de saque por operação.")
    return False

def validar_conta_ativa(status):
    if status == "ativa": #só contas com status 'ativa' podem movimentar dinheiro
        return True
    print("  Conta não está ativa. Operação não permitida.")
    return False

def validar_transferencia(conta_origem_id, conta_destino_id, status_destino):
    if conta_origem_id == conta_destino_id: #não faz sentido transferir para a mesma conta
        print("  A conta de destino deve ser diferente da conta de origem.")
        return False
    return validar_conta_ativa(status_destino) #a conta de destino também precisa estar ativa
