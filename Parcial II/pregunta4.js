// Daniela Ramirez 16-10940

const X = 9
const Y = 4
const Z = 0

// Se calcula alpha y beta con el nro de carnet
let alpha = ((X+Y)%5)+3 // alpha = 6
let beta = ((Y+Z)%5)+3 // beta = 7

// Se inicializa el arreglo con los casos bases
const casosBases = [];
for(let i = 0; i < alpha * beta; i++) casosBases.push(i);

// Funcion recursiva de F
function recF(n){
    if (n < alpha*beta){
        return n;
    }
    else if (n >= alpha*beta){
        return recF(n - beta*1) + recF(n - beta*2) + recF(n - beta*3) + recF(n - beta*4) + recF(n - beta*5) + recF(n - beta*6);
    }
}

// Funcion recursiva de cola de F
function tailF(n, base = [...casosBases]){
	if(n < alpha * beta){
		return base[n];
	}
    // Se agg de ultimo al arreglo base
	base.push(base[0] + base[7] + base[14] + base[21] + base[28] + base[35]);
    // Se elimina el primer elemento
	base.shift();

	return tailF(n-1, base);
}

// Funcion iterativa de F
function itF(n){
	if(n < alpha*beta) return n;

    // Se copian los valores del arreglo como en la firma de la funcion recursiva de cola
	let fnacci = [...casosBases]

	for(let i = alpha*beta; i <= n; i++){
        // En current_value se va almacenando la suma de los valores fnacci
		let current_value = 0;
        // Bucle para calcular la suma de fnacci[35] + fnacci[28] + ... como en la recursion de cola
		for(let j = 1; j <= alpha; j++){
			current_value += fnacci[i - beta * j];
		}
        // Se agg la suma antes calculada
		fnacci.push(current_value);
	}

	return fnacci[n];
}

const { symlinkSync } = require('fs')
const { exit } = require('process')
// Programa ppal
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const prompt = (query) => new Promise((resolve) => rl.question(query, resolve));

(async () => {
    // Se lee el input del usuario
    const numero = await prompt("Ingrese el numero final n: ");
    const n = parseInt(numero);

    // Se inicializa los arreglos donde iran los resultados
    const rec = [];
    const tail = [];
    const it = [];

    // Se inicializa los arreglos donde iran los tiempos
    const recTime = [];
    const tailTime = [];
    const itTime = [];

    // Se realizo las pruebas de 5 en 5
    for(let i = 0; i < n; i += 10){

        // Recursiva
        var start = performance.now();
        let result = recF(i);
        var end = performance.now();

        rec.push(result);
        recTime.push(end-start);

        // Recursiva de cola
        var startT = performance.now();
        let resultF = tailF(i);
        var endT = performance.now();

        tail.push(resultF);
        tailTime.push(endT - startT);

        // Iterativa
        var startI = performance.now();
        let resultI = itF(i);
        var endI = performance.now();

        it.push(resultI);
        itTime.push(endI - startI);

    }

    // Impresion de resultados
    console.log('\nResultados:\n');
    console.log('\t\t Recursiva \t Recursiva de cola \t Iterativa');
    for(let i = 0; i < rec.length; i ++){
        if (rec[i] > 99999){
            console.log(`Valor ${i} -> \t ${rec[i]} \t ${tail[i]} \t\t ${it[i]}`);
        }
        else{
            console.log(`Valor ${i} -> \t ${rec[i]} \t\t ${tail[i]} \t\t\t ${it[i]}`);
        }

    }

    // Impresion de tiempo en ms
    console.log('\nTiempos en ms:\n');
    console.log('\t\t Recursiva \t Recursiva de cola \t Iterativa');
    for(let i = 0; i < recTime.length; i ++){
        if (i > 9){
            if (recTime[i]>9){
                console.log(`Tiempo ${i} -> \t ${recTime[i].toFixed(3)} \t ${tailTime[i].toFixed(3)} \t\t\t ${itTime[i].toFixed(3)} `);
            }
            else{
                console.log(`Tiempo ${i} -> \t ${recTime[i].toFixed(3)} \t\t ${tailTime[i].toFixed(3)} \t\t\t ${itTime[i].toFixed(3)} `);
            }
        }
        else{
            console.log(`Tiempo ${i}  -> \t ${recTime[i].toFixed(3)} \t\t ${tailTime[i].toFixed(3)} \t\t\t ${itTime[i].toFixed(3)} `);
        }

    }

exit();
})();

