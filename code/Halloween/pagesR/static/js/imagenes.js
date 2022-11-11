function retornarFecha() {
    var fecha
    fecha = new Date();
    var cadena = fecha.getDate() + '/' + (fecha.getMonth() + 1) + '/' + fecha.getYear();
    return cadena;
}

function retornarHora() {
    var fecha
    fecha = new Date();
    var cadena = fecha.getHours() + ':' + fecha.getMinutes() + ':' + fecha.getSeconds();
    return cadena;
}

var photos = new Array()
var which = 0
var a = ''
/*Change the below variables to reference your own images. You may have as many images in the slider as you wish*/
photos[0] = "/static/images/1.jpg"
photos[1] = "/static/images/2.jpg"
photos[2] = "/static/images/3.jpg"
photos[3] = "/static/images/4.jpg"
photos[4] = "/static/images/5.jpg"


function backward() {
    if (which > 0) {
        window.status = ''
        which--
        document.images.photoslider.src = photos[which]
    }
}

function wolas() {

    alert(a);

}

function forward() {
    if (which < photos.length - 1) {
        which++
        document.images.photoslider.src = photos[which]
    }
    else {
        window.status = 'Fin De La Galeria'
    }
}
