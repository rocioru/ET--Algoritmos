print("----  | Bienvedio a CREATIVOS.CL |  ----")

listaRun = [10987789,20402657,21234403]  #RUN
listaOcupado = [14,15,16,33,45] #ASIENTOS OCUPADOS

precioPlatinum = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
precioGold = [21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
precioSilver = [51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
listaAsiento = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]

menu = '''
        MENU
    1. Comprar entradas
    2. Mostrar ubicaciones disponibles
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    0. Salir
    Digite opcion: '''

menuEntradas = '''
        MENU ENTRADAS
    1. Entrada Platinum ==> $120000
    2. Entrada Gold     ==> $80000
    3. Entrada Silver   ==> $50000
    Digite opcion: '''

while True:
    try:
        opc = int(input(menu))
        if opc == 0:
            break
        elif opc == 1:
            print("-----------------------------------------------")
            print("Ingrese cantidad de entradas que desea comprar:")
            print("---------------------ESCENARIO-----------------------")
            print("----1----2----3----4----5----6----7----8----9---10---")
            print("---11---12---13---14---15---16---17---18---19---20---")
            print("---21---22---23---24---25---26---27---28---29---30---")
            print("---31---32---33---34---35---36---37---38---39---40---")
            print("---41---42---43---44---45---46---47---48---49---50---")
            print("---51---52---53---54---55---56---57---58---59---60---")
            print("---61---62---63---64---65---66---67---68---69---70---")
            print("---71---72---73---74---75---76---77---78---79---80---")
            print("---81---82---83---84---85---86---87---88---89---90---")
            print("---91---92---93---94---95---96---97---98---99---100--")
            print("-----------------------------------------------------")
            print("-----------------------------------------------------")
            print("---LOS PRECIOS DE LAS ENTRADAS SON: ")
            print("---PLATINUM---$120.000--")
            print("---GOLD-------$80.000---")
            print("---SILVER-----$50.000---")
            
            while True:
                try:
                    run = int(input("run: "))
                    if run > 0: 
                        listaRun.append(run)
                        print("El RUN ha sido ingresado correctamente")
                        break
                    else:
                        print("error, RUN debe ser mayor que cero")
                except:
                    print("excepcion de run")
            #--------------------------------------------------------------
          
            while True:
                try:
                    asiento = input("asiento: ")
                    if len(asiento) >= 1:
                        listaAsiento.append(asiento)
                        break
                    else:
                        print("ERROR")
                except:
                    print("excepcion de asiento")

                    
            #--------------------------------------------------------------
                    
            
          
        elif opc == 2:
            print("opcion 2")
            print("---------------|UBICACIONES DISPONIBLES|---------------")
            print("---------------------|ESCENARIO|-----------------------")
            print("----1----2----3----4----5----6----7----8----9---10---")
            print("---11---12---13----X----X----X---17---18---19---20---")
            print("---21---22---23---24---25---26---27---28---29---30---")
            print("---31---32----X---34---35---36---37---38---39---40---")
            print("---41---42---43---44----x---46---47---48---49---50---")
            print("---51---52---53---54---55---56---57---58---59---60---")
            print("---61---62---63---64---65---66---67---68---69---70---")
            print("---71---72---73---74---75---76---77---78---79---80---")
            print("---81---82---83---84---85---86---87---88---89---90---")
            print("---91---92---93---94---95---96---97---98---99---100--")
            
      
        elif opc == 3:
            print("opcion 3")
            print("Ver listado de asistente")
            asistente = input("asistente a mostrar: ")
            print(f" LISTA asistente: {asistente} \n")
            print("N°| RUN | ENTRADA PLATINUM | ENTRADA GOLD | ENTRADA SILVER | ")
            print("--+-----+------------------+--------------+----------------+-")
            for i in range(len(listaRun)):
                if asistente.lower() == listaRun[i].lower():
                    print(f"{i+1} | {listaRun[i]:8d} | {precioPlatinum[i]:8d} | {precioGold[i]:8d} | {precioSilver[i]:8d} |")
                    print("-------+------------------+-------------------------+---------------------+----------------------+")

        elif opc == 4:
          print("opcion 4")
          print("Mostrar ganancias totales")
          while menuEntradas == 1: 
                  try:
                      EntradaPlatinum = int(input("cuantas? :"))
                      EntradaGold = int(input("cuantas? : "))
                      EntradaSilver = int(input("cuantas? : "))
                      if menuEntradas == 1:
                          totaluno = EntradaPlatinum * 120000
                          break
                      elif menuEntradas == 2:
                           totaldos = EntradaGold * 80000
                           break
                      elif menuEntradas == 3:
                           totaltres = EntradaSilver * 50000
                           break
                      else:
                          print("rango incorrecto [1-3]") 
                  except:
                      print("E")
            

        elif opc == 5:
            print("opcion 5")
            print("Salir")
            print("RocioRodriguezUrrutia")
            print("10/07/2023")
            

    
        else:
            print("opcion incorrecta")
    except:
        print("Hasta la próxima")
#FIN
