def mensagem_text(**kwargs):
    msg = f"""
    Olá {kwargs['nome']},

    Segue abaixo suas credenciais de login e senha para acesso aos nossos sistemas na nuvem:
    login: infopublicpb\{kwargs['cpf']}
    senha TS: {kwargs['senha_ts']}
    senha do sistema: {kwargs['senha_sistema']}


    Instruções:
        - Basta utilizar o ícone de acesso e inserir as credenciais informadas nesta mensagem
        (caso não tenha ainda o ícone de acesso, favor solicitá-lo entrando em contato com o suporte
        da Infopublic)
        - Recomendamos inserir o ícone de acesso em sua áre de trabalho para facilitar

    Atenciosamente,

    """

    return msg

def msg_informativo_text(msg):
    return msg