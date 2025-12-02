"""
Calculadora  em Python 
Autor: Lucas Scala

Versão: 1.0.3
"""

import math
import json
import os
from datetime import datetime
from typing import List, Dict, Union, Optional
from pathlib import Path


class CalculadoraError(Exception):
    """Exceção personalizada para erros da calculadora"""
    pass


class DivisaoPorZeroError(CalculadoraError):
    """Exceção para divisão por zero"""
    pass


class Calculadora:
    """Classe principal da calculadora com todas as operações básicas"""
    
    def __init__(self):
        """Inicializa a calculadora"""
        self._memoria = 0.0
        self._ultimo_resultado = None
        self._historico = []
        self._total_operacoes = 0
        self._max_historico = 50
        
        self._limpar_tela()
        self._exibir_cabecalho()
    
    # ========== PROPRIEDADES ==========
    
    @property
    def memoria(self) -> float:
        """Retorna o valor atual da memória"""
        return self._memoria
    
    @property
    def ultimo_resultado(self) -> Optional[float]:
        """Retorna o último resultado calculado"""
        return self._ultimo_resultado
    
    @property
    def total_operacoes(self) -> int:
        """Retorna o total de operações realizadas"""
        return self._total_operacoes
    
    @property
    def historico(self) -> List[Dict]:
        """Retorna uma cópia do histórico"""
        return self._historico.copy()
    
    # ========== MÉTODOS PRIVADOS ==========
    
    def _limpar_tela(self) -> None:
        """Limpa a tela do console"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def _exibir_cabecalho(self) -> None:
        """Exibe o cabeçalho da calculadora"""
        print("=" * 60)
        print("          CALCULADORA BÁSICA EM PYTHON")
        print("=" * 60)
    
    def _exibir_linha(self) -> None:
        """Exibe uma linha separadora"""
        print("-" * 60)
    
    def _adicionar_ao_historico(self, expressao: str, resultado: float, tipo: str) -> None:
        """Adiciona uma operação ao histórico"""
        entrada = {
            'timestamp': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            'expressao': expressao,
            'resultado': resultado,
            'tipo': tipo
        }
        
        self._historico.append(entrada)
        self._ultimo_resultado = resultado
        self._total_operacoes += 1
        
        # Limitar tamanho do histórico
        if len(self._historico) > self._max_historico:
            self._historico.pop(0)
    
    def _validar_numero(self, valor: str) -> bool:
        """Valida se a string é um número válido"""
        try:
            float(valor)
            return True
        except ValueError:
            return False
    
    def _obter_numero(self, mensagem: str = "Digite um número: ") -> Union[int, float]:
        """Obtém um número válido do usuário"""
        while True:
            try:
                entrada = input(mensagem).strip()
                
                # Permite usar 'M' para memória
                if entrada.upper() == 'M':
                    return self._memoria
                
                # Permite usar 'U' para último resultado
                if entrada.upper() == 'U' and self._ultimo_resultado is not None:
                    return self._ultimo_resultado
                
                # Converte para número
                num = float(entrada)
                
                # Retorna como int se for inteiro
                if num.is_integer():
                    return int(num)
                return num
                
            except ValueError:
                print("ERRO: Digite um número válido!")
                print("   Use 'M' para memória ou 'U' para último resultado")
    
    def _formatar_numero(self, num: Union[int, float]) -> str:
        """Formata um número para exibição"""
        if isinstance(num, int):
            return str(num)
        elif num.is_integer():
            return str(int(num))
        else:
            # Mostra no máximo 10 casas decimais
            return f"{num:.10f}".rstrip('0').rstrip('.')
    
    # ========== OPERAÇÕES BÁSICAS ==========
    
    def somar(self) -> None:
        """Realiza a soma de dois números"""
        self._limpar_tela()
        print("OPERAÇÃO: SOMA")
        self._exibir_linha()
        
        a = self._obter_numero("Digite o primeiro número: ")
        b = self._obter_numero("Digite o segundo número: ")
        
        resultado = a + b
        expressao = f"{self._formatar_numero(a)} + {self._formatar_numero(b)}"
        
        self._adicionar_ao_historico(expressao, resultado, "Soma")
        
        print("\n" + "=" * 40)
        print(f"RESULTADO: {expressao} = {self._formatar_numero(resultado)}")
        print("=" * 40)
        input("\nPressione Enter para continuar...")
    
    def subtrair(self) -> None:
        """Realiza a subtração de dois números"""
        self._limpar_tela()
        print("OPERAÇÃO: SUBTRAÇÃO")
        self._exibir_linha()
        
        a = self._obter_numero("Digite o primeiro número: ")
        b = self._obter_numero("Digite o segundo número: ")
        
        resultado = a - b
        expressao = f"{self._formatar_numero(a)} - {self._formatar_numero(b)}"
        
        self._adicionar_ao_historico(expressao, resultado, "Subtração")
        
        print("\n" + "=" * 40)
        print(f"RESULTADO: {expressao} = {self._formatar_numero(resultado)}")
        print("=" * 40)
        input("\nPressione Enter para continuar...")
    
    def multiplicar(self) -> None:
        """Realiza a multiplicação de dois números"""
        self._limpar_tela()
        print("OPERAÇÃO: MULTIPLICAÇÃO")
        self._exibir_linha()
        
        a = self._obter_numero("Digite o primeiro número: ")
        b = self._obter_numero("Digite o segundo número: ")
        
        resultado = a * b
        expressao = f"{self._formatar_numero(a)} × {self._formatar_numero(b)}"
        
        self._adicionar_ao_historico(expressao, resultado, "Multiplicação")
        
        print("\n" + "=" * 40)
        print(f"RESULTADO: {expressao} = {self._formatar_numero(resultado)}")
        print("=" * 40)
        input("\nPressione Enter para continuar...")
    
    def dividir(self) -> None:
        """Realiza a divisão de dois números"""
        self._limpar_tela()
        print("OPERAÇÃO: DIVISÃO")
        self._exibir_linha()
        
        a = self._obter_numero("Digite o numerador: ")
        
        while True:
            b = self._obter_numero("Digite o denominador: ")
            if b == 0:
                print("ERRO: Não é possível dividir por zero!")
            else:
                break
        
        resultado = a / b
        expressao = f"{self._formatar_numero(a)} ÷ {self._formatar_numero(b)}"
        
        self._adicionar_ao_historico(expressao, resultado, "Divisão")
        
        print("\n" + "=" * 40)
        print(f"RESULTADO: {expressao} = {self._formatar_numero(resultado)}")
        print("=" * 40)
        input("\nPressione Enter para continuar...")
    
    def resto_divisao(self) -> None:
        """Calcula o resto da divisão"""
        self._limpar_tela()
        print("OPERAÇÃO: RESTO DA DIVISÃO")
        self._exibir_linha()
        
        a = int(self._obter_numero("Digite o primeiro número (inteiro): "))
        
        while True:
            b = int(self._obter_numero("Digite o segundo número (inteiro): "))
            if b == 0:
                print("ERRO: Não é possível dividir por zero!")
            else:
                break
        
        resultado = a % b
        expressao = f"{a} % {b}"
        
        self._adicionar_ao_historico(expressao, resultado, "Resto Divisão")
        
        print("\n" + "=" * 40)
        print(f"RESULTADO: {expressao} = {resultado}")
        print("=" * 40)
        input("\nPressione Enter para continuar...")
    
    def potencia(self) -> None:
        """Calcula a potência de um número"""
        self._limpar_tela()
        print("OPERAÇÃO: POTÊNCIA")
        self._exibir_linha()
        
        base = self._obter_numero("Digite a base: ")
        expoente = self._obter_numero("Digite o expoente: ")
        
        resultado = base ** expoente
        expressao = f"{self._formatar_numero(base)} ^ {self._formatar_numero(expoente)}"
        
        self._adicionar_ao_historico(expressao, resultado, "Potência")
        
        print("\n" + "=" * 40)
        print(f"RESULTADO: {expressao} = {self._formatar_numero(resultado)}")
        print("=" * 40)
        input("\nPressione Enter para continuar...")
    
    def raiz_quadrada(self) -> None:
        """Calcula a raiz quadrada"""
        self._limpar_tela()
        print("🔢 OPERAÇÃO: RAIZ QUADRADA")
        self._exibir_linha()
        
        while True:
            numero = self._obter_numero("Digite o número: ")
            if numero < 0:
                print("ERRO: Não existe raiz quadrada de número negativo!")
            else:
                break
        
        resultado = math.sqrt(numero)
        expressao = f"√{self._formatar_numero(numero)}"
        
        self._adicionar_ao_historico(expressao, resultado, "Raiz Quadrada")
        
        print("\n" + "=" * 40)
        print(f"RESULTADO: {expressao} = {self._formatar_numero(resultado)}")
        print("=" * 40)
        input("\nPressione Enter para continuar...")
    
    def porcentagem(self) -> None:
        """Calcula porcentagem"""
        self._limpar_tela()
        print("OPERAÇÃO: PORCENTAGEM")
        self._exibir_linha()
        
        valor = self._obter_numero("Digite o valor: ")
        percentual = self._obter_numero("Digite a porcentagem: ")
        
        resultado = (valor * percentual) / 100
        expressao = f"{self._formatar_numero(valor)}% de {self._formatar_numero(percentual)}"
        
        self._adicionar_ao_historico(expressao, resultado, "Porcentagem")
        
        print("\n" + "=" * 40)
        print(f"RESULTADO: {expressao} = {self._formatar_numero(resultado)}")
        print("=" * 40)
        input("\nPressione Enter para continuar...")
    
    def fatorial(self) -> None:
        """Calcula o fatorial"""
        self._limpar_tela()
        print("OPERAÇÃO: FATORIAL")
        self._exibir_linha()
        
        while True:
            n = int(self._obter_numero("Digite um número inteiro (0-20): "))
            if n < 0:
                print("ERRO: Fatorial não definido para números negativos!")
            elif n > 20:
                print("AVISO: Número muito grande para cálculo preciso!")
            else:
                break
        
        resultado = math.factorial(n)
        expressao = f"{n}!"
        
        self._adicionar_ao_historico(expressao, resultado, "Fatorial")
        
        print("\n" + "=" * 40)
        print(f"RESULTADO: {expressao} = {resultado}")
        print("=" * 40)
        input("\nPressione Enter para continuar...")
    
    # ========== FUNCIONALIDADES DA CALCULADORA ==========
    
    def gerenciar_memoria(self) -> None:
        """Gerencia a memória da calculadora"""
        self._limpar_tela()
        print("GERENCIAR MEMÓRIA")
        self._exibir_linha()
        
        print(f"Valor atual na memória: {self._formatar_numero(self._memoria)}")
        print("\n1. Definir novo valor")
        print("2. Adicionar valor atual")
        print("3. Subtrair valor atual")
        print("4. Limpar memória")
        print("5. Usar memória em cálculo")
        print("0. Voltar")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            novo_valor = self._obter_numero("Digite o novo valor: ")
            self._memoria = novo_valor
            print(f"Memória definida para: {self._formatar_numero(novo_valor)}")
        
        elif opcao == "2":
            valor = self._obter_numero("Digite o valor para adicionar: ")
            self._memoria += valor
            print(f"Valor adicionado. Memória atual: {self._formatar_numero(self._memoria)}")
        
        elif opcao == "3":
            valor = self._obter_numero("Digite o valor para subtrair: ")
            self._memoria -= valor
            print(f"Valor subtraído. Memória atual: {self._formatar_numero(self._memoria)}")
        
        elif opcao == "4":
            self._memoria = 0.0
            print("Memória limpa!")
        
        elif opcao == "5":
            print(f"Use 'M' como entrada para usar o valor da memória: {self._formatar_numero(self._memoria)}")
        
        input("\nPressione Enter para continuar...")
    
    def exibir_historico(self) -> None:
        """Exibe o histórico de operações"""
        self._limpar_tela()
        print("HISTÓRICO DE OPERAÇÕES")
        self._exibir_linha()
        
        if not self._historico:
            print("Nenhuma operação no histórico!")
        else:
            print(f"Total de operações: {len(self._historico)}")
            self._exibir_linha()
            
            for i, operacao in enumerate(reversed(self._historico), 1):
                print(f"{i}. [{operacao['timestamp']}]")
                print(f"   {operacao['expressao']} = {self._formatar_numero(operacao['resultado'])}")
                print(f"   Tipo: {operacao['tipo']}")
                print()
        
        input("\nPressione Enter para continuar...")
    
    def exibir_estatisticas(self) -> None:
        """Exibe estatísticas da calculadora"""
        self._limpar_tela()
        print("ESTATÍSTICAS DA CALCULADORA")
        self._exibir_linha()
        
        print(f"Total de operações realizadas: {self._total_operacoes}")
        print(f"Operações no histórico: {len(self._historico)}")
        print(f"Último resultado: {self._formatar_numero(self._ultimo_resultado) if self._ultimo_resultado is not None else 'Nenhum'}")
        print(f"Valor na memória: {self._formatar_numero(self._memoria)}")
        
        if self._historico:
            # Contar operações por tipo
            tipos = {}
            for op in self._historico:
                tipo = op['tipo']
                tipos[tipo] = tipos.get(tipo, 0) + 1
            
            print("\n Operações por tipo:")
            for tipo, quantidade in sorted(tipos.items(), key=lambda x: x[1], reverse=True):
                print(f"  {tipo}: {quantidade} operações")
        
        input("\nPressione Enter para continuar...")
    
    def salvar_historico(self) -> None:
        """Salva o histórico em um arquivo"""
        self._limpar_tela()
        print("SALVAR HISTÓRICO")
        self._exibir_linha()
        
        if not self._historico:
            print("Nenhuma operação para salvar!")
            input("\nPressione Enter para continuar...")
            return
        
        nome_arquivo = input("Digite o nome do arquivo (sem extensão): ").strip()
        if not nome_arquivo:
            nome_arquivo = "historico_calculadora"
        
        nome_arquivo += ".json"
        
        try:
            # Converter para formato serializável
            historico_serializavel = []
            for op in self._historico:
                historico_serializavel.append({
                    'timestamp': op['timestamp'],
                    'expressao': op['expressao'],
                    'resultado': float(op['resultado']) if isinstance(op['resultado'], (int, float)) else op['resultado'],
                    'tipo': op['tipo']
                })
            
            with open(nome_arquivo, 'w', encoding='utf-8') as f:
                json.dump({
                    'total_operacoes': self._total_operacoes,
                    'memoria': self._memoria,
                    'ultimo_resultado': self._ultimo_resultado,
                    'historico': historico_serializavel
                }, f, indent=2, ensure_ascii=False)
            
            print(f" Histórico salvo em: {nome_arquivo}")
            
        except Exception as e:
            print(f"Erro ao salvar histórico: {e}")
        
        input("\nPressione Enter para continuar...")
    
    def calcular_expressao(self) -> None:
        """Calcula uma expressão matemática simples"""
        self._limpar_tela()
        print(" CALCULAR EXPRESSÃO")
        self._exibir_linha()
        
        print("Digite uma expressão matemática simples (ex: 2 + 3 * 4)")
        print("Operadores suportados: +, -, *, /, ^, %")
        print("Use 'M' para memória, 'U' para último resultado")
        
        expressao = input("\nExpressão: ").strip()
        
        if not expressao:
            print(" Expressão vazia!")
            input("\nPressione Enter para continuar...")
            return
        
        try:
            # Substituir M e U
            expressao = expressao.replace('M', str(self._memoria))
            expressao = expressao.replace('U', str(self._ultimo_resultado if self._ultimo_resultado is not None else 0))
            
            # Substituir operadores do Python
            expressao = expressao.replace('^', '**')
            
            # Avaliar a expressão
            resultado = eval(expressao)
            
            self._adicionar_ao_historico(expressao.replace('**', '^'), resultado, "Expressão")
            
            print("\n" + "=" * 40)
            print(f" RESULTADO: {expressao.replace('**', '^')} = {self._formatar_numero(resultado)}")
            print("=" * 40)
            
        except ZeroDivisionError:
            print("ERRO: Divisão por zero!")
        except Exception as e:
            print(f"ERRO: Expressão inválida! ({e})")
        
        input("\nPressione Enter para continuar...")
    
    def exibir_menu_principal(self) -> None:
        """Exibe o menu principal"""
        self._limpar_tela()
        self._exibir_cabecalho()
        
        print(f"Estatísticas: {self._total_operacoes} operações | Memória: {self._formatar_numero(self._memoria)}")
        
        if self._ultimo_resultado is not None:
            print(f"Último resultado: {self._formatar_numero(self._ultimo_resultado)}")
        
        self._exibir_linha()
        print("OPERAÇÕES BÁSICAS:")
        print("  1. Soma (+)")
        print("  2. Subtração (-)")
        print("  3. Multiplicação (×)")
        print("  4. Divisão (÷)")
        print("  5. Resto da divisão (%)")
        
        print("\nOPERAÇÕES AVANÇADAS:")
        print("  6. Potência (^)")
        print("  7. Raiz quadrada (√)")
        print("  8. Porcentagem (%)")
        print("  9. Fatorial (!)")
        
        print("\nFUNCIONALIDADES:")
        print("  E. Calcular Expressão")
        print("  H. Ver Histórico")
        print("  M. Gerenciar Memória")
        print("  S. Estatísticas")
        print("  G. Salvar Histórico")
        
        print("\n CONFIGURAÇÕES:")
        print("  C. Limpar Histórico")
        print("  R. Resetar Calculadora")
        print("  0. Sair")
        self._exibir_linha()
    
    def limpar_historico(self) -> None:
        """Limpa o histórico de operações"""
        self._historico.clear()
        print(" Histórico limpo!")
        input("\nPressione Enter para continuar...")
    
    def resetar_calculadora(self) -> None:
        """Reseta a calculadora para valores iniciais"""
        self._memoria = 0.0
        self._ultimo_resultado = None
        self._historico.clear()
        self._total_operacoes = 0
        print(" Calculadora resetada!")
        input("\nPressione Enter para continuar...")
    
    # ========== MÉTODO PRINCIPAL ==========
    
    def executar(self) -> None:
        """Método principal para executar a calculadora"""
        while True:
            self.exibir_menu_principal()
            
            opcao = input("\nEscolha uma opção: ").strip().upper()
            
            if opcao == "0":
                print("\nObrigado por usar a Calculadora!")
                print("=" * 60)
                break
            
            elif opcao == "1":
                self.somar()
            
            elif opcao == "2":
                self.subtrair()
            
            elif opcao == "3":
                self.multiplicar()
            
            elif opcao == "4":
                self.dividir()
            
            elif opcao == "5":
                self.resto_divisao()
            
            elif opcao == "6":
                self.potencia()
            
            elif opcao == "7":
                self.raiz_quadrada()
            
            elif opcao == "8":
                self.porcentagem()
            
            elif opcao == "9":
                self.fatorial()
            
            elif opcao == "E":
                self.calcular_expressao()
            
            elif opcao == "H":
                self.exibir_historico()
            
            elif opcao == "M":
                self.gerenciar_memoria()
            
            elif opcao == "S":
                self.exibir_estatisticas()
            
            elif opcao == "G":
                self.salvar_historico()
            
            elif opcao == "C":
                self.limpar_historico()
            
            elif opcao == "R":
                self.resetar_calculadora()
            
            else:
                print(" Opção inválida! Tente novamente.")
                input("\nPressione Enter para continuar...")


# ========== FUNÇÃO PRINCIPAL ==========

def main():
    """Função principal do programa"""
    try:
        calculadora = Calculadora()
        calculadora.executar()
    except KeyboardInterrupt:
        print("\n\n Programa interrompido pelo usuário!")
    except Exception as e:
        print(f"\n Erro inesperado: {e}")


if __name__ == "__main__":
    main()

    """Ultilizei de IA para me auxiliar com os comentario pois nao tenho muito costume ainda"""