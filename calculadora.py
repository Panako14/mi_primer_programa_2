operacion = input('¿Que operación quieres realizar (multiplicar / dividir / sumar / restar)?: ')
primer_numero = int(input('Dime un número: '))
segundo_numero = int(input('Dime otro número: '))

if operacion == 'multiplicar':
    resultado = primer_numero * segundo_numero

elif operacion == 'dividir':
    resultado = primer_numero / segundo_numero

elif operacion == 'sumar':
    resultado = primer_numero + segundo_numero

elif operacion == 'restar':
    resultado = primer_numero - segundo_numero

print('El resultado es {}'.format(resultado))