# Programa de control de Stock para el negocio de EL NOBLE
# Desarrollado por Federico Lopez y Agustin Gutierrez

import Promo


#                            (IdProducto, nombre, cantidad vendida, precio)


promo = Promo(1, "5 chipa + Cafe clasico", 0, 60)
dicPromo = {'promo1': promo}

promo = Promo(2, "5 chipa + Cafe especial", 0, 80)
dicPromo['promo2'] = promo

promo = Promo(3, "Cafe clasico + 2 Medialunas", 0, 44)
dicPromo['promo3'] = promo

promo = Promo(4, "Cafe clasico + 1 Medialunas", 0, 37)
dicPromo['promo4'] = promo

promo = Promo(5, "Cafe especial + 2 Medialunas", 0, 64)
dicPromo['promo5'] = promo

promo = Promo(6, "Cafe especial + 1 Medialunas", 0, 57)
dicPromo['promo6'] = promo




# 							(IdProducto, nombre, )
#===============================================================================
# producto= producto(1,"cafe clasico",0)
# producto= producto(1,"cafe clasico",0)
# producto= producto(1,"cafe clasico",0)
#===============================================================================


