from sodapy import Socrata

# Paths
path_in1_AUT = r"" #Folder to stored process AUT IDEAM data.
#path_in2_AMSC=r"" #Folder where raw AMSC data stored.
#path_out1_AMSC=r"" #Folder to stored process AMSC data.

# Client
client = Socrata( #
    "www.datos.gov.co", 
    "",
    username="", 
    password="",
    timeout=60)
#variables
dicc1_variables = {
    #1: ["ysq6-ri4e", "Calidad Aire"],
    2: ["kiw7-v9ta", "direccion", "wind_direction",'deg',1],
    3: ["uext-mhny", "humedad", "humidity",'%',1],
    #4: ["ia8x-22em", "nivelmar", "sea_level", 'm'],
    #5: ["vfth-yucv", "nivelmax", "max_level",'m'],
    6: ["s54a-sgyg", "precipitacion", "precipitation",'mm',1],
    7: ["62tk-nxj5", "presionatm", "atmospheric_pressure",'hpa',1],
    8: ["sgfv-3yp8", "velocidad", "wind_speed",'m/s',1],
    9: ["sbwg-7ju4", "temperatura", "temperature",'°C',1]
}

StationsCodeAMSC = {
    "oriente": "102030101",
    "turbo": "102002102",
    "sonson": "102056603",
    "yarumal": "102098804",
    "santafe": "102021505",
    "caucasia": "102082706",
    "itm": "102056507",
    "andes": "102047408",
    "arboletes": "102067509",
    "pb": "102009310"
}