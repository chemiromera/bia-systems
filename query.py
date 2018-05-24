import json
import datetime


def loadqpxfromjson(o,d,salida):
	tarifas=[]
	fechas=[]
	vuelta=(salida + datetime.timedelta(days = 7))
	fichero='/home/chemiromera/biatravel/tarifas_qpx/' + o + '-' + d + '-' + str(salida) + '.json'
	fa = open(fichero, "r")
	for line in fa:
		l = json.loads(line)
		for i in range(0,len(l["trips"]["tripOption"])-1):
			ob=l['observacion']
			saleTotal=l["trips"]["tripOption"][i]["saleTotal"]
			cia=l["trips"]["tripOption"][i]["slice"][0]["segment"][0]["flight"]["carrier"]
			numero=l["trips"]["tripOption"][i]["slice"][0]["segment"][0]["flight"]["number"]
			origen=l["trips"]["tripOption"][i]["slice"][0]["segment"][0]["leg"][0]["origin"]
			origen_terminal=l["trips"]["tripOption"][i]["slice"][0]["segment"][0]["leg"][0]["originTerminal"]
			departureTime=l["trips"]["tripOption"][i]["slice"][0]["segment"][0]["leg"][0]["departureTime"]
			destination=l["trips"]["tripOption"][i]["slice"][0]["segment"][0]["leg"][0]["destination"]
			destinationTerminal=l["trips"]["tripOption"][i]["slice"][0]["segment"][0]["leg"][0]["destination"]
			aircraft=l["trips"]["tripOption"][i]["slice"][0]["segment"][0]["leg"][0]["aircraft"]
			cabin=l["trips"]["tripOption"][i]["slice"][0]["segment"][0]["cabin"]
			arrivalTime=l["trips"]["tripOption"][i]["slice"][0]["segment"][0]["leg"][0]["arrivalTime"]
			cadena = str(ob) + ' ' + str(origen) + ' ' + str(origen_terminal) + ' ' + str(destination) + ' ' + str(destinationTerminal) + ' '+ str(cia) + ' '+ str(numero)  + ' '+ str(departureTime) + ' ' + str(arrivalTime) + ' ' + str(aircraft)  + ' ' + str(cabin) +  ' ' + str(saleTotal) 

	fa.close()
	return cadena
