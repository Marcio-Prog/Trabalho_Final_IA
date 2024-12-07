import cv2
import math

# Parâmetros de detecção
MIN_AREA_CARRO = 500  # Tamanho mínimo de um contorno para ser considerado um carro
LINHA_DETECTORA = 255  # Posição da linha horizontal que conta os carros
OFFSET = 10  # Tolerância para interseção com a linha
CARROS_CONTADOS = 0

# Lista de rastreamento
rastreamento_carros = []

def calcula_centroide(x, y, w, h):
    """
    Calcula o centroide de um retângulo.
    """
    return (x + w // 2, y + h // 2)

def desenha_info(frame, carros):
    """
    Desenha a linha de contagem e o número total de carros no frame.
    """
    altura, largura = frame.shape[:2]
    # Linha de contagem
    cv2.line(frame, (0, LINHA_DETECTORA), (largura, LINHA_DETECTORA), (0, 0, 255), 2)
    # Texto do número de carros
    cv2.putText(frame, f'Carros: {carros}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

def distancia(p1, p2):
    """
    Calcula a distância euclidiana entre dois pontos.
    """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def main():
    global CARROS_CONTADOS

    # Carregar vídeo
    video_path = 'rodovia.mov'
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Erro ao abrir o vídeo: {video_path}")
        return

    # Subtração de fundo
    subtrator = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Redimensionar o vídeo para processamento mais rápido
        frame = cv2.resize(frame, (800, 450))
        frame_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Subtração de fundo
        mascara = subtrator.apply(frame_cinza)
        mascara = cv2.medianBlur(mascara, 5)
        _, mascara = cv2.threshold(mascara, 127, 255, cv2.THRESH_BINARY)

        # Encontrar contornos
        contornos, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        novos_centroides = []
        for cnt in contornos:
            area = cv2.contourArea(cnt)
            if area < MIN_AREA_CARRO:
                continue

            # Desenhar retângulo em torno do contorno
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Calcular centroide
            centroide = calcula_centroide(x, y, w, h)
            novos_centroides.append(centroide)

            # Verificar se cruzou a linha
            if LINHA_DETECTORA - OFFSET <= centroide[1] <= LINHA_DETECTORA + OFFSET:
                # Verificar se o centroide já foi contado
                ja_contado = False
                for rastro in rastreamento_carros:
                    if distancia(centroide, rastro) < 40:  # Distância máxima para considerar o mesmo carro
                        ja_contado = True
                        break
                if not ja_contado:
                    CARROS_CONTADOS += 1
                    rastreamento_carros.append(centroide)

        # Atualizar rastreamento de carros, mantendo apenas os carros próximos
        rastreamento_carros[:] = [
            rastro for rastro in rastreamento_carros if any(distancia(rastro, nc) < 50 for nc in novos_centroides)
        ]

        # Desenhar informações no frame
        desenha_info(frame, CARROS_CONTADOS)

        # Exibir vídeo
        cv2.imshow("Rodovia", frame)
        cv2.imshow("Máscara", mascara)

        # Sair ao pressionar 'q'
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


