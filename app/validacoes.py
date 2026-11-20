def obter_cpf(mensagem="Olá bem vindo de volta! Digite seu CPF(somente números):   "):
    while True:
        cpf = input(mensagem)
        cpf_limpo = cpf.replace(".", "").replace("-", "") #verifica se não tem pontuação no digitalizador
        if len(cpf_limpo) == 11 and cpf_limpo.isdigit(): 
            print("CPF Válido! Prosseguir ")#Caso esteja nos conformes pedidos irá validar
            return cpf_limpo
        else:
            print("  CPF inválido. Por favor, digite um CPF válido (11 dígitos).")#Caso não estiver ele inválida e repete novamente até validar 