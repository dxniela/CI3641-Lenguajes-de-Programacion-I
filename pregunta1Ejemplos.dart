// Daniela Ramirez 16-10940

// Ejemplos para la pregunta 1

import 'dart:math';

// 1er ejemplo: Ejemplo de alcance

bool topLevel = true;
void main() {
  var insideMain = true;

  void myFunction() {
    var insideFunction = true;

    void nestedFunction() {
      var insideNestedFunction = true;

      assert(topLevel);
      assert(insideMain);
      assert(insideFunction);
      assert(insideNestedFunction);
    }
  }
}

// 2do ejemplo: Ejemplo de aliases

typedef IntList = List<int>;
IntList il = [1, 2, 3];

// Un alias de tipo puede tener parámetros de tipo:

typedef ListMapper<X> = Map<X, List<X>>;
Map<String, List<String>> m1 = {}; // Detallado.
ListMapper<String> m2 = {}; // Lo mismo pero más corto y más claro.

// 3er ejemplo: Poliformismo

class Circle {
  double _radius;
  String _color;

  Circle(this._radius, this._color) {
    this._radius = 1.0;
    this._color = 'red';
  }

  Circle.withRadius(this._radius, this._color, double r) {
    this._radius = r;
    this._color = 'red';
  }

  Circle.withRadiusColor(double r, String c, this._radius, this._color) {
    this._radius = r;
    this._color = c;
  }

  double get radius => this._radius;
  String get color => this._color;
  set radius(double r) => this._radius = r;
  set color(String c) => this._color = c;

  String toString() => 'Circle[radius=$_radius, color=$_color]';
  double area() => double.tryParse((pi * pow(radius, 2)).toStringAsFixed(2));
}

// Subclase de Circle:

class Cylinder extends Circle {
  double _height;

  Cylinder(this._height) : super() {
    this._height = 1.0;
  }
  Cylinder.withHeight(this._height) : super();

  Cylinder.withHeightRadius(this._height, double r) : super.withRadius(r);

  Cylinder.withHeightRadiusColor(this._height, double r, String c)
      : super.withRadiusColor(r, c);

  double get height => this._height;
  set height(double h) => this._height = h;

  // String toString() => 'Cylinder[base=${super.toString()}, height=$_height]';
  double volume() => double.tryParse((area() * _height).toStringAsFixed(2));
}
