// Daniela Ramirez 16-10940

// Programa que dados tres enteros no–negativos a, b y c , tal que c >= 2, c
// calcula la potenciación modulada (a^b) mod c.

import 'dart:io';

// Funcion para calcular la potenciacion modulada
int power(int a, int b, int c) {
  var result;

  if (b == 0) {
    result = 1;
  } else if (b > 0) {
    result = ((a % c) * power(a, b - 1, c)) % c;
  }

  return result;
}

void main() {
  var result;

  // Le pedimos al usuario los valores y los almacenamos
  print("Introduzca el valor de a: ");
  var a = int.tryParse(stdin.readLineSync() ?? "");

  print("Introduzca el valor de b: ");
  var b = int.tryParse(stdin.readLineSync() ?? "");

  print("Introduzca el valor de c: ");
  var c = int.tryParse(stdin.readLineSync() ?? "");

  // Si el usuario no introduce nada pero da enter
  if (a == null || b == null || c == null) {
    print("Error: Introduzca un numero valido.");
    main();
  }
  // Las variables deben cumplir las condiciones para poder realizar el calculo
  else if (a > 0 && b >= 0 && c >= 2) {
    result = power(a, b, c);
    print("($a^$b) mod $c = $result");
  }
  // Si el usuario ingresa numeros que no cumplan con las condiciones anteriores
  else {
    print("Introduzca tres enteros no negativos a, b y c , tal que c >= 2");
    main();
  }
}
