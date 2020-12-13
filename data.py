# -*- coding: utf-8 -*-
products = [
    
    {
     "name":"Julian", 
     "last_name": "Soto",
     "email":"jdsoto@gmail.com"},  
    {
     "name":"julian ",
     "last_name": "correa",
     "email":"jcorrea@gmail.com"},
    {
     "name":"Oliver ", 
     "last_name": "charry",
     "email":"ofcharry@gmail.com"},  
    {
     "name":"Mateo ",
     "last_name": "Garcia",
     "email":"mgarcia@gmail.com"},
    {
     "name":"Emilio ", 
     "last_name": "Peña",
     "email":"ejpena@gmail.com"},  
    {
     "name":"Juan ",
     "last_name": "Patiño",
     "email":"jmpatino@gmail.com"}  
    ]

Rutas = [
    {
      "URL":"/",
      "Description": "Bienvenida y Rutas",
      "Parameter": "No",
      "Method": "[GET]"
    },

    {
      "URL":"/data",
      "Description": "Informacion a cerca de los integrantes de la    banda",
      "Parameter": "No",
      "Method": "[GET]"
      },

    {
      "URL":"/data/{id}", 
      "Description": "Informacion a cerca de un integrante de la banda",
      "Parameter": "Si",
      "Method": "[GET]"},

    {
      "URL":"/create",
      "Description": "Crea un integrante de la banda",
      "Parameter": "No",
      "Method": "[POST]"
     },

    {
      "URL":"/modify/{id}",
      "Description": "modifica un integrante de la banda",
      "Parameter": "Si",
      "Method": "[PATCH]"
     }
      
    ]
