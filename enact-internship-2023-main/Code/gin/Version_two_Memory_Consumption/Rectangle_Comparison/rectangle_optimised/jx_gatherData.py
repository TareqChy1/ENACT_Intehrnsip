import math as ma
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

if __name__ == '__main__':
    # En paramètres d'entrée :
    # dossier result
    # Le dossier result contient plusieurs dossiers qui contiennent des .csv
    dossier_result = sys.argv[1]
    listeFichiers = []

    # Paramètres pour export en csv
    noms_methodes = []
    iterations = []
    params = []
    puissances = []
    energies = []

    # Collecter les fichiers de consommation d'énergie pour chaque méthode dans le dossier energy/methods
    for root, _, files in os.walk("./" + dossier_result + "/energy/methods", topdown=False):
        for name in files:
           if name.endswith("-all-methods-energy.csv"):
           	listeFichiers.append(os.path.join(root, name))
    for i in range(len(listeFichiers)):
        data = pd.read_csv(listeFichiers[i], header=None,keep_default_na=False)  # [methode, valeur]
        # Les noms de fichiers sont de la forme "./jx_results/energy/methods/joularJX-"$java_pid"-all-methods-energy.csv"
        file_parts = listeFichiers[i].split("/")
        file_name = file_parts[-1]
        #print(file_name)
        # Split file name by "-" character
        file_name_parts = file_name.split("-")
        # Extract information from file name
        if len(file_name_parts) >= 4:
            param = file_name_parts[0]
            iteration = int(file_name_parts[1])
            # Convert second column to float
            data[1] = data[1].astype(float)
            # Filter data based on condition (e.g., values in second column > 0.0)
            data = data[data[1] > 0.0] # On ne garde que les lignes intéressantes
            if not data.empty:
                for j in range(len(data[0])):
                    noms_methodes.append(data[0].values[j])
                    energies.append(data[1].values[j])
                    params.append(param)
                    iterations.append(iteration)

    pd_energy_dict = {
        "Methode" : noms_methodes,
        "Param": params,
        "Iteration": iterations,
        "Consommation totale (J)": energies
    }

    pd_energy = pd.DataFrame(pd_energy_dict)
    

    noms_methodes.clear()
    iterations.clear()
    params.clear()
    puissances.clear()
    energies.clear()
    listeFichiers.clear()
    
    
    # Collecter les fichiers de consommation d'énergie pour chaque méthode dans le dossier energy/calltrees
    for root, _, files in os.walk("./" + dossier_result + "/energy/calltrees", topdown=False):
        for name in files:
           if name.endswith("-all-call-trees-energy.csv"):
           	listeFichiers.append(os.path.join(root, name))
           	
    for i in range(len(listeFichiers)):
        data = pd.read_csv(listeFichiers[i], header=None,keep_default_na=False)  # [methode, valeur]
        # Les noms de fichiers sont de la forme "./jx_results/energy/calltrees/joularJX-25000-all-call-trees-energy.csv"
        file_parts = listeFichiers[i].split("/")
        file_name = file_parts[-1]
        #print(file_name)
        # Split file name by "-" character
        file_name_parts = file_name.split("-")
        # Extract information from file name
        if len(file_name_parts) >= 4:
            param = file_name_parts[0]
            iteration = int(file_name_parts[1])
            # Convert second column to float
            data[1] = data[1].astype(float)
            # Filter data based on condition (e.g., values in second column > 0.0)
            data = data[data[1] > 0.0] # On ne garde que les lignes intéressantes
            if not data.empty:
                for j in range(len(data[0])):
                    noms_methodes.append(data[0].values[j])
                    energies.append(data[1].values[j])
                    params.append(param)
                    iterations.append(iteration)

    pd_energy_dict = {
        "Methode" : noms_methodes,
        "Param": params,
        "Iteration": iterations,
        "Consommation totale (J)": energies
    }

    pd_energy_1 = pd.DataFrame(pd_energy_dict)

    noms_methodes.clear()
    iterations.clear()
    params.clear()
    puissances.clear()
    energies.clear()
    listeFichiers.clear()
    
    # Collecter les fichiers de consommation d'énergie pour chaque méthode dans le dossier power/methods
    for root, _, files in os.walk("./" + dossier_result + "/power/methods", topdown=False):
        for name in files:
           if name.endswith("-all-methods-power.csv"):
           	listeFichiers.append(os.path.join(root, name))
    for i in range(len(listeFichiers)):
        data = pd.read_csv(listeFichiers[i], header=None,keep_default_na=False)  # [methode, valeur]
        # Les noms de fichiers sont de la forme "./jx_results/power/methods/joularJX-25000-all-methods-power.csv"
        file_parts = listeFichiers[i].split("/")
        file_name = file_parts[-1]
        #print(file_name)
        # Split file name by "-" character
        file_name_parts = file_name.split("-")
        # Extract information from file name
        if len(file_name_parts) >= 4:
            param = file_name_parts[0]
            iteration = int(file_name_parts[1])
            # Convert second column to float
            data[1] = data[1].astype(float)
            # Filter data based on condition (e.g., values in second column > 0.0)
            data = data[data[1] > 0.0] # On ne garde que les lignes intéressantes
            if not data.empty:
                for j in range(len(data[0])):
                    noms_methodes.append(data[0].values[j])
                    puissances.append(data[1].values[j])
                    params.append(param)
                    iterations.append(iteration)

    pd_power_dict = {
        "Methode": noms_methodes,
        "Param": params,
        "Iteration": iterations,
        "Puissance moy (W)": puissances,
    }

    pd_power = pd.DataFrame(pd_power_dict)

    noms_methodes.clear()
    iterations.clear()
    params.clear()
    puissances.clear()
    energies.clear()
    listeFichiers.clear()


    # Collecter les fichiers de consommation d'énergie pour chaque méthode dans le dossier power/calltrees
    for root, _, files in os.walk("./" + dossier_result + "/power/calltrees", topdown=False):
        for name in files:
           if name.endswith("-all-call-trees-power.csv"):
           	listeFichiers.append(os.path.join(root, name))
           	
    for i in range(len(listeFichiers)):
        data = pd.read_csv(listeFichiers[i], header=None,keep_default_na=False)  # [methode, valeur]
        # Les noms de fichiers sont de la forme "./jx_results/power/calltrees/joularJX-25000-all-call-trees-power.csv"
        file_parts = listeFichiers[i].split("/")
        file_name = file_parts[-1]
        #print(file_name)
        # Split file name by "-" character
        file_name_parts = file_name.split("-")
        # Extract information from file name
        if len(file_name_parts) >= 4:
            param = file_name_parts[0]
            iteration = int(file_name_parts[1])
            # Convert second column to float
            data[1] = data[1].astype(float)
            # Filter data based on condition (e.g., values in second column > 0.0)
            data = data[data[1] > 0.0] # On ne garde que les lignes intéressantes
            if not data.empty:
                for j in range(len(data[0])):
                    noms_methodes.append(data[0].values[j])
                    puissances.append(data[1].values[j])
                    params.append(param)
                    iterations.append(iteration)

    pd_power_dict = {
        "Methode": noms_methodes,
        "Param": params,
        "Iteration": iterations,
        "Puissance moy (W)": puissances,
    }

    pd_power_1 = pd.DataFrame(pd_power_dict)


    #to_csv_df = pd.merge(pd_energy, pd_power, how='left', on=["Methode", "Param", "Iteration"])

    #to_csv_df = to_csv_df.sort_values(['Methode', 'Param', 'Iteration'])
    #nom_fichier = "joularJX.csv"
    #to_csv_df.to_csv("./" + dossier_result + nom_fichier, index=False)



    # Exporter les données en CSV
    pd_energy.to_csv("./" + dossier_result + "/energy_methods_summary.csv", index=False)
    pd_power.to_csv("./" + dossier_result + "/power_methods_summary.csv", index=False)
    
    # Read energy_summary.csv and power_summary.csv into dataframes
    energy_df = pd.read_csv('./' + dossier_result + '/energy_methods_summary.csv')
    power_df = pd.read_csv('./' + dossier_result + '/power_methods_summary.csv')
    
    # Concatenate energy_df and power_df vertically
    combined_df = pd.concat([energy_df, power_df], axis=0)
    # Write combined_df to joularJX.csv
    combined_df.to_csv('jx_results/joularJX_methods.csv', index=False)
    
    
    
    # Exporter les données en CSV avec un délimiteur spécifique (par exemple, ';')
    pd_energy_1.to_csv("./" + dossier_result + "/energy_calltrees_summary.csv", index=False, sep=';')
    pd_power_1.to_csv("./" + dossier_result + "/power_calltrees_summary.csv", index=False, sep=';')

    # Read energy_summary.csv and power_summary.csv into dataframes with the same delimiter
    energy_df_1 = pd.read_csv('./' + dossier_result + '/energy_calltrees_summary.csv', sep=';')
    power_df_1 = pd.read_csv('./' + dossier_result + '/power_calltrees_summary.csv', sep=';')

    # Concatenate energy_df and power_df vertically
    combined_df = pd.concat([energy_df_1, power_df_1], axis=0)
    # Write combined_df to joularJX.csv with the same delimiter
    combined_df.to_csv('jx_results/joularJX_calltrees.csv', index=False, sep=';')
