// Daniela Ramirez 16-10940

// Programa que dadas dos matrices A y B (cuyas dimensiones son N x M y M x P, respectivamente),
// calcula su producto A x B (cuya dimensión es N x P).

import 'dart:io';

void main() {
  // Se inicializa las matrices
  List<List<int>> A = [[]];
  List<List<int>> B = [[]];
  List<List<int>> C = [[]];

  // Se declara una variable temporal
  var temporal = 0;

  // Se le pide al usuario que ingrese la cantidad de filas de A
  print("Ingrese la cantidad de filas de A: ");
  var N = int.parse(stdin.readLineSync() ?? "");

  // Se le pide al usuario que ingrese la cantidad de columnas de A que sera la misma cantidad de filas de B
  print(
      "Ingrese la cantidad de columnas de A que sera la misma cantidad de filas de B: ");
  var M = int.parse(stdin.readLineSync() ?? "");

  // Se le pide al usuario que ingrese la cantidad de columnas de B
  print("Ingrese la cantidad de columnas de B: ");
  var P = int.parse(stdin.readLineSync() ?? "");

  // Ahora se le pide al usuario que ingrese los elementos de las matrices
  // Matriz A
  for (int fila = 0; fila < N; fila++) {
    // Se agrega una nueva fila a la matriz
    A.add([]);
    for (int columna = 0; columna < M; columna++) {
      print("Ingrese el elemento A[$fila][$columna]: ");
      var k = int.parse(stdin.readLineSync() ?? "");
      A[fila].add(k);
    }
  }

  // Matriz B
  for (int fila = 0; fila < M; fila++) {
    // Se agrega una nueva fila a la matriz
    B.add([]);
    for (int columna = 0; columna < P; columna++) {
      print("Ingrese el elemento B[$fila][$columna]: ");
      var k = int.parse(stdin.readLineSync() ?? "");
      B[fila].add(k);
    }
  }

  // Se realiza la multiplicacion de las matrices
  for (int i = 0; i < N; i++) {
    // Se agrega una nueva fila a la matriz
    C.add([]);
    for (int j = 0; j < P; j++) {
      for (int k = 0; k < M; k++) {
        temporal = temporal + A[i][k] * B[k][j];
      }
      C[i].add(temporal);
      temporal = 0;
    }
  }

  // Se imprime la matriz C
  print("El resultado de multiplicar AxB es: ");
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < P; j++) {
      print("C[$i][$j] = ${C[i][j]}");
    }
  }
}
