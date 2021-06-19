# Algoritmo (función) para obtener el área promedio de 5  triángulos especificados (base y altura)

from libreriaGeomArit import areaTriangulo

# base_t1 = float(input('ingrese base triangulo 1: '))
# alt_t1 = float(input('ingrese altura triangulo 1: '))
#
# base_t2 = float(input('ingrese base triangulo 2: '))
# alt_t2 = float(input('ingrese altura triangulo 2: '))
#
# base_t3 = float(input('ingrese base triangulo 3: '))
# alt_t3 = float(input('ingrese altura triangulo 3: '))
#
# base_t4 = float(input('ingrese base triangulo 4: '))
# alt_t4 = float(input('ingrese altura triangulo 4: '))
#
# base_t5 = float(input('ingrese base triangulo 5: '))
# alt_t5 = float(input('ingrese altura triangulo 5: '))
#
# area_t1 = areaTriangulo(base_t1, alt_t1)
# area_t2 = areaTriangulo(base_t2, alt_t2)
# area_t3 = areaTriangulo(base_t3, alt_t3)
# area_t4 = areaTriangulo(base_t4, alt_t4)
# area_t5 = areaTriangulo(base_t5, alt_t5)

# areaPromedio = sum((area_t1,area_t2,area_t3,area_t4,area_t5)) / len((area_t1,area_t2,area_t3,area_t4,area_t5))
# print(areaPromedio)

# Cálculo de impuestos: se reciben los montos de patrimonio, pasivos y activos, cada uno con un impuesto
# de 5%, 15% y 30%. Retornar el pago total por concepto de impuestos.

def calculoImpuestos(patrimonio, pasivos, activos):
    # total_impuestos = 0
    # total_impuestos += patrimonio*0.05
    # total_impuestos += pasivos*0.15
    # total_impuestos += activos*0.30
    # return total_impuestos

    

print('Los impuestos totales son:',calculoImpuestos(10000,10000,15000))
