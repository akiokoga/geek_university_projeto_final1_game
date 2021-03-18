"""
Descrição:
Devemos desenvolver uma aplicação que ao ser inicializada solicite ao usuário escolher o nível de dificuldade do jogo e após isso gera e apresenta de forma aleatória um cálculo para que possamos informar o resultado:

Iremos limitar as operações em somar, subtrair e multiplicar
Se o usuário acertar ele recebe um ponto ao seu score
Acertando ou errando, ele poderá ou não continuar o jog
"""
from projetos_geekuniversity.Game1.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejado[1 - Fácil, 2 - Médio , 3 - Difícil, 4 - Expert]: '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s)')

    continuar: int = int(input('Deseja continuar no jogo? [1 - Sim, 0 - Não]: '))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s)')
        print('Até a próxima')

if __name__ == '__main__':
    main()