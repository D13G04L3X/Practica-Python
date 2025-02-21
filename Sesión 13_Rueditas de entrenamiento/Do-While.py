'''
Do-While: garantiza que el código se ejecute al menos una vez, independiente de la condición.

'''

import java.util.Scanner;

public class Menu {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("1. Jugar");
            System.out.println("2. Salir");
            System.out.print("Selecciona una opción: ");
            opcion = sc.nextInt();
        } while (opcion != 2);

        System.out.println("Juego temrinado.");
    }
}