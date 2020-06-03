Manual de Referencia Rápida
Forever Mamalone es un lenguaje simple, similar a los lenguajes comunes de programación, con la diferencia de ser menos complejo y programado totalmente por mi, usando todo lo aprendido durante mi carrera para lograrlo.

Forever Mamalone Ofrece:
Declaraciones de variables con y sin arreglos, una funciòn principal con sus funciones a las cuales se deben poder llamar y tener recursividad, estatutos lineales y no lineales. Este lenguaje cae en la categoría de un lenguaje imperativo.

Requisitos
Python 3

Instalación de Forever Mamalone
git clone https://github.com/ArturoCtu/ForeverAlone.git

Getting Started - Hello World
program helloworld;
main(){
	print(“Hello world”);
}

Compilación
Para compilar algún archivo .c (ejemplo helloworld.c) en Forever Mamalone realizamos el siguiente comando /Python mamalone helloworld.c

Resultado
De haber tenido éxito se espera el siguiente output en consola.
“Hello world”

Estructura Básica
program Nombre_prog ;
<Declaración de Variables Globales>
<Definición de Funciones>
main()
<Declaración de Variables Locales>
{
 	<Estatutos>
}

Declaración de Variables
Puedes definir variables tipo
Variables enteras: int
Variables flotantes: float
Caracteres: char

Sintaxis correcta:
var int a,b,c;
      float d, e, f;

Asignación de valores
a = 25;

Operaciones
Forever Mamalone soporta 2 tipos de operaciones aritméticas y lógicas.
Suma: +
Resta: -
Multiplicacion: *
División: /
Comparaciones: >, <, >=, <=, !=, ==,  !=, &&, ||

a= 1 + 25 * 2;
b= 25 + 1 * 2 
if (a != b) then {
  flag = false;
} else {
  flag = true;
}

Es importante dejar espacios entre operandos y operadores. 


Estatutos Lineales
Asignación	Id<dimension> = Expresión;
		Id = Nombre_Módulo(params)
Llamadas	Nombre_Módulo(params)
Lectura	Lee(ID)

Estatutos No Lineales 
Decisión	if (expresión) then{
			 <Estatutos>
		} else{
		 	<Estatutos>
}
While 		while(expresion){
			<Estatutos>
}
For		from asignación to expresion{
			<Estatutos>
}

Funciones
function <tipo-retorno> nombre_módulo ( <Parámetros> ) ;
<Declaración de Variables Locales>
{
 <Estatutos>
}

¡Ya eres un mamalone!
Forever Mamalone made with love in Monterrey, México
