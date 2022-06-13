// Daniela Ramirez 16-10940

// Programa que simula un manejador de memoria que implementa el buddy system.

// Clase para representar el indice inferior y el superior de un bloque
class Pair {
    constructor(a, b) {
        this.lb = a;
        this.ub = b;
    }
}
 
let size;
let arr;
 
function Buddy(s) {
    size = s;
     
    // Todas las posibles potencias de 2 que pueden ser usadas para el tamaño de la memoria
    let x = Math.ceil(Math.log(s) / Math.log(2));
       
    // Se agrega un elemento al arreglo para que el arreglo tenga la cantidad de elementos necesaria
    arr = new Array(x + 1);
       
    for(let i = 0; i <= x; i++)
        arr[i] =[];
           
    // Inicialmente solo el bloque más grande está libre para almacenar el tamaño requerido
    // y por lo tanto está en la lista libre
    arr[x].push(new Pair(0, size - 1));
}
 
function asignar(s) {
     
    // Se calcula qué lista hay libre para obtener el bloque mas pequeño
    // lo suficientemente grande como para almacenar el tamaño requerido
    let x = Math.floor(Math.ceil(Math.log(s) / Math.log(2)));
       
    let i;
    let temp = null;
    
    // Si ya se tiene un bloque libre para el tamaño requerido
    if (arr[x].length > 0)
    {
         
        // Se elimina de la lista libre el bloque
        temp = arr[x].shift();
        console.log("Memoria desde " + temp.lb + " a " + temp.ub + " asignada");
        return;
    }
       
    // Si no se tiene un bloque libre para el tamaño requerido
    // se busca por un bloque grande suficiente
    for(i = x + 1; i < arr.length; i++)
    {
        if (arr[i].length == 0)
            continue;
               
        // Si se encuentra un bloque grande suficiente se hace break
        break;
    }
       
    // Esto será True si no se encontró un bloque grande suficiente
    if (i == arr.length)
    {
        console.log("Error: No hay memoria suficiente para asignar el bloque");
        return;
    }
       
    // Se elimina de la lista libre el primer bloque grande suficiente
    temp = arr[i].shift(0);
       
    i--;
       
    // Se recorre la lista libre para buscar un bloque pequeño suficiente
    for(; i >= x; i--)
    {
         
        // Se divide el bloque en dos partes
        // el indice inferior a la mitad-1
        let newPair = new Pair(temp.lb, temp.lb + Math.floor((temp.ub - temp.lb) / 2));
           
        // el indice superior a la mitad
        let newPair2 = new Pair(temp.lb + Math.floor((temp.ub - temp.lb + 1) / 2), temp.ub);
           
        // Se agregan a la lista que busca bloques de tamaño pequeños
        arr[i].push(newPair);
        arr[i].push(newPair2);
           
        // Se elimina el bloque para continuar buscando
        temp = arr[i].shift(0);
    }
       
    // Se le informa al usuario donde se ha almacenado el bloque en la memoria
    console.log("Memoria desde " + temp.lb + " a " + temp.ub + " asignada");
}
 

// Programa principal

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const prompt = (query) => new Promise((resolve) => rl.question(query, resolve));

(async () => {
    const initialMemory = await prompt("Ingrese el tamaño de la memoria: ");
    const memory = parseInt(initialMemory);
    if (isNaN(memory)) {
        console.log("El tamaño de la memoria debe ser un numero. Intente de nuevo.");
        return;
    }       
    Buddy(memory);
    
    while(true){
        
        const command = (await prompt("\nIngrese un comando: ")).toUpperCase();

        if (command == "RESERVAR") {
            const size = await prompt("\nIngrese el tamaño del bloque a reservar: ");
            const sizeInt = parseInt(size);
            if (isNaN(sizeInt)) {
                console.log("El tamaño del bloque debe ser un numero");
                continue;
            }
            asignar(sizeInt);
        }
        else if (command == "SALIR") {
            process.exit(0);
        }  
        else {
            console.log("\nComando invalido");
        }
    }
    
})();