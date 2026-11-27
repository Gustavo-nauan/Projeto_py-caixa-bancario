import string #biblioteca com os caracteres de pontuação (usada na validação da senha)

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
