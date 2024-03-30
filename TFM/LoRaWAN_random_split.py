#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Es necesario tener el dataset lorawan descargado. Se puede encontrar en zenodo (https://zenodo.org/records/1193563)
lorawan = pd.read_csv('lorawan_dataset_antwerp.csv')

# Eliminar campos no necesarios
lorawan.columns = lorawan.columns.str.replace("'", "")
lorawan.drop(['RX Time', 'SF', 'HDOP'], axis=1, inplace=True)

# Convertir las coordenadas de grados a radianes
lorawan['Latitude'] = np.radians(lorawan['Latitude'])
lorawan['Longitude'] = np.radians(lorawan['Longitude'])

# Dividir el dataset en conjuntos de entrenamiento y validación para las potencias RSSI
train_rss_random, val_rss_random = train_test_split(lorawan.drop(['Latitude', 'Longitude'], axis=1), test_size=0.3, random_state=42)

# Dividir el dataset en conjuntos de entrenamiento y validación para las coordenadas en radianes
train_crd_random, val_crd_random = train_test_split(lorawan[['Longitude', 'Latitude']], test_size=0.3, random_state=42)

# Guardar train_rss_random en un archivo CSV
train_rss_random.to_csv('train_rss_random.csv', index=False)

# Guardar val_rss_random en un archivo CSV
val_rss_random.to_csv('val_rss_random.csv', index=False)

# Guardar train_crd_random en un archivo CSV
train_crd_random.to_csv('train_crd_random.csv', index=False)

# Guardar val_crd_random en un archivo CSV
val_crd_random.to_csv('val_crd_random.csv', index=False)

