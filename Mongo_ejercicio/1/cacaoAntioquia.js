var map = function(){
    if (this.DEPARTAMENTO == 'ANTIOQUIA'){
        emit(this.MUNICIPIO, this.AreaCosechada);
    }
}

var reduce = function(llave, valor){
    return Array.sum(valor)
}

use cultivos
db.Cacao.mapReduce(map, reduce, {out:'Antioquia'})