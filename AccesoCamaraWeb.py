import cv2

def main():
    # Abre la cámara web (el número 0 indica la primera cámara, si tienes varias)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error al abrir la cámara")
        return

    # Crea la ventana para mostrar el video
    cv2.namedWindow("Cámara Web", cv2.WINDOW_NORMAL)

    while True:
        # Captura un cuadro de la cámara
        ret, frame = cap.read()

        if not ret:
            print("Error al capturar el cuadro")
            break

        # Muestra el cuadro en la ventana
        cv2.imshow("Cámara Web", frame)

        # Si se presiona la tecla 'q', sale del bucle
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera la cámara y cierra la ventana al salir del bucle
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()