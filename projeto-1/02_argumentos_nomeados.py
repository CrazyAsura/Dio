def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")
    
salvar_carro("Fiat", "Pálio", "1999", "ABC-1234")
salvar_carro(marca="Fiat", modelo="Pálio", ano="1999", placa="ABC-1234")
salvar_carro(**{"marca":"Fiat", "modelo":"Pálio", "ano":"1999", "placa":"ABC-1234"})