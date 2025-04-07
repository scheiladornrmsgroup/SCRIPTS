def valorfrete():
    valor = checklist.get_value("FRETE")
    return valor

def comissao(): 
    porcentagem = 0 
    tipo_veiculo = checklist.get_value("QUAL A COMISSÃO?") 

    if tipo_veiculo == "7%": 
        porcentagem = 7.0 
    else: 
        porcentagem = 5.0 

    valor_frete = float(valorfrete()) 
    total = valor_frete * (porcentagem / 100.0) 
    return checklist.format_double(total, "n2")

comissao()