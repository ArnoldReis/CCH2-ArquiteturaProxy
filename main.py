
class Documento:
    def __init__(self, conteudo):
        self.conteudo = conteudo

    def exibir(self):
        return f"Conteudo do Documento: {self.conteudo}"

class Usuario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

    def autorizado(self):
        return self.cargo.lower() in ['admin', 'gerente']

class DocumentoProxy:
    def __init__(self, documento, usuario):
        self.documento = documento
        self.usuario = usuario

    def exibir(self):
        if self.usuario.autorizado():
            return self.documento.exibir()
        else:
            return f"Acesso Negado: Usuario {self.usuario.nome} nao possui permissao para visualizar este documento."


if __name__ == "__main__":
    doc_confidencial = Documento("Informaçoes sensiveis da empresa.")

    usuario_admin = Usuario("Carlos", "admin")
    usuario_funcionario = Usuario("Mariana", "funcionario")

    proxy_admin = DocumentoProxy(doc_confidencial, usuario_admin)
    proxy_funcionario = DocumentoProxy(doc_confidencial, usuario_funcionario)

    print("Acesso do Administrador:\n")
    print(proxy_admin.exibir())
    
    print("Acesso do Funcionario:")
    print(proxy_funcionario.exibir())

