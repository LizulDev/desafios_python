# Sistema bancario simples 

## Objetivo: 

Criar um sistema bancario capaz de:

- depositar dinheiro <br>
- sacar dinheiro <br>
- verificar extrato de atividades na conta

Para sacar valores, tem-se **3️ restrições**:

- Há um limite de 500 reais para cada saque;
```py 
VALOR_LIMITE_DE_SAQUE = 500.00
```
- É permitido apenas 3 saques por acesso
```py 
LIMITE_SAQUE = 3
```
- O valor do saque não pode ser superior ao valor do saldo da conta. 
```py 
saldo_da_conta > saque_ solicitado
```

## Versão 2.0

Incluidas as operações de:
-  criar usuário
-  criar conta
-  listar contas
-  modulação de cada ação em funções e procedimentos

Nas seções **criar usuário** e **criar conta**, há a verificação se o usuário existe, e se seu CPF não está em uso em outra conta, respectivamente. 

## Versão 3.0

Código com abordagem de orientação a objetos;

**TODO**: Não é possivel escolher conta para ser recuperada.<br>
Agora: Possível escolher qual conta quer recuperar:

```py
def recuperar_conta_cliente()
```

Linguagem utilizada 
- Python