def mensagem_text(nome, cpf, senha, senha_sistema):
    msg = f"""
    Olá {nome},

    Segue abaixo suas credenciais de login e senha para acesso aos nossos sistemas na nuvem:
    login: infopublicpb\{cpf}
    senha TS: {senha}
    senha do sistema: {senha_sistema}


    Instruções:
        - Basta utilizar o ícone de acesso e inserir as credenciais informadas nesta mensagem
        (caso não tenha ainda o ícone de acesso, favor solicitá-lo entrando em contato com o suporte
        da Infopublic)
        - Recomendamos inserir o ícone de acesso em sua áre de trabalho para facilitar

    Atenciosamente,

    """

    return msg