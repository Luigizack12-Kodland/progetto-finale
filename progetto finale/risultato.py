def calcola_impronta_di_carbonio():
    print("Calcola la tua impronta di carbonio giornaliera\n")

    # Chiedi informazioni sull'attività dell'utente
    km_auto = float(input("Quanti chilometri percorri in guidi al giorno? "))
    ore_aereo = float(input("Quante ore voli in aereo al mese? "))
    consumo_elettrico = float(input("Qual è il tuo consumo elettrico mensile in kWh? "))
    quantita_rifiuti = float(input("Quanti rifiuti produci al giorno (in kg)? "))

    # Calcola l'impronta di carbonio per le attività specificate
    carbonio_auto = km_auto * 0.2  # Assumendo un'efficienza media di 5 km per litro
    carbonio_aereo = ore_aereo * 250  # Assumendo 250 g di CO2 per km per voli
    carbonio_elettrico = consumo_elettrico * 0.5  # Assumendo 0.5 kg di CO2 per kWh
    carbonio_rifiuti = quantita_rifiuti * 0.1  # Assumendo 0.1 kg di CO2 per kg di rifiuti

    # Calcola l'impronta di carbonio totale
    impronta_totale = carbonio_auto + carbonio_aereo + carbonio_elettrico + carbonio_rifiuti

    # Mostra l'impronta di carbonio totale
    print("\nLa tua impronta di carbonio giornaliera è di circa {:.2f} kg di CO2.".format(impronta_totale))

# Esegui la funzione per calcolare l'impronta di carbonio
calcola_impronta_di_carbonio()
