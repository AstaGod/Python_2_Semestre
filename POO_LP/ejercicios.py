# haciendo uso de la POO crear un objeto para entidad celular
class Celular:
    marca="Samsumng"
    tamaño="163.3,77.3"
    color="negro"
    pantalla="super amoled"

    def enceder_celular(self):
        return "mantiene presionado el boton encender"
    
    def mensaje(self):
        return "escribir y recibir mensajes de texto"
    
print(Celular.marca)
# haciendo uso de la POO crear un objeto para entidad vehiculo
class Vehiculo:
    marca="Lanborguini"
    motor="10000000 caballos de fuerza"
    color="dorado"
    asientos=2

    def avanzar(self):
        return "recorriste 10 km"
    
    def estacionar(self):
        return "te estasionaste en el lugar 7"
    
print(Vehiculo.color)
# haciendo uso de la POO crear un objeto para entidad avion
class avion:
    color="blanco"
    motores=2
    ruedas=20

    def vuela(self):
        return "despejo de la line a de aterrisaje"
    
    def aterriza(self):
        return "se aterrizo con exito en el aeropuerto"
print(avion.color)
# haciendo uso de la POO crear un objeto para un heroe de dota2
class heroe:
    nombre="Jinx"
    rol="tirador"
    edad=19

    def habilidad_pasiva(self):
        return "gran aumento de velocidad de movimiento y velocidad de ataque"
    
    def habilidad_q(self):
        return "¡Cambiazo!: Jinx modifica sus ataques básicos al alternar entre Pium Pium, su ametralladora, y Espinas, su lanzacohetes."
    
    def habilidad_w(self):
        return "¡Zap!: Jinx usa a Chispita, su pistola de rayos, para disparar un rayo que ralentiza e inflige daño al primer enemigo que golpea, revelándolo."
    
    def habilidad_e(self):
        return "¡Mascafuegos!: Jinx lanza una hilera de granadas paralizantes que explotan tras 5 s y envuelven en llamas a los enemigos circundantes."
    
    def habilidad_r(self):
        return "¡Supermegacohete mortal!: Jinx dispara un supercohete por todo el mapa que va aumentando su daño a medida que avanza"

print(heroe.nombre)

# haciendo uso de la POO crear un objero para una pc
class pc:
    componentes="Monitor, Case, Teclado, etc"
    color="rgb"

    def prender(self):
        return "presionar el boton de encendidio"
    def teclado(self):
        return "escribir en el teclado"
    
print(pc.componentes)
# haciendo uso de la POO crear un objero para una impresora
class impresora:
    color="negro"
    tinta="negro, azul, rojo, etc"

    def imprimir(self):
        return "imprimi una hoja"
    def escan(self):
        return "escanea una imagen o documento"
    def momnocromatica(self):
        return "solo imprime en color negro"
print(impresora.tinta)
# haciendo uso de la POO crear un objero para emitir una factura
class factura:
    nombre="nombre del cliente"
    DNI="4454564654"

    def agreagar_p(self):
        return "agregar producto"
    def igv(self):
        return "sacar el igv"
    
print(factura.nombre)
