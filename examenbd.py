import mysql.connector
import json

def insertardatos():
    datos = {}
    datos=  [{"idProducto": 1850,
            "productoNombreCorto": "William Lawsons Std"
            ,"productoNombreLargo": "Whisky William Lawsons Std 750 ml"
            ,"productoDescripcion": "Es un whisky afrutado de cuerpo ligero, se caracteriza por su aroma a pastel de manzana y su sabor a cereal tostado y al tofee, con un final suave."
            ,"productoTipo": 1
            ,"productoPresentacion": "Botella"
            ,"productoCosto": 170.5
            ,"productoGanancia":15
            ,"productoDescuento": 0
            ,"productoExistencia": 1000,
            "productoImagen": "Whisky-1850.webp"}
            ,{"idProducto": 1450
            ,"productoNombreCorto": "Outer Space"
            ,"productoNombreLargo": "Vodka Outer Space 750 ml"
            ,"productoDescripcion": "Es un vodka hecho con maíz 100 americano, sin gluten, el diseño de su botella es único y llamativo. Tiene aromas y sabores a frutos secos."
            ,"productoTipo": 1,"productoPresentacion": "Botella","productoCosto": 700.5
            ,"productoGanancia": 15,"productoDescuento": 0,"productoExistencia": 1000
            ,"productoImagen": "Vodka-1450.webp"}
            ,{"idProducto": 850
            ,"productoNombreCorto": "Ron Antillano Blanco"
            ,"productoNombreLargo": "Ron Antillano Blanco C/Vaso/Macerador 1L"
            ,"productoDescripcion": "","productoTipo": 1
            ,"productoPresentacion": "Botella","productoCosto": 150.5
            ,"productoGanancia": 15
            ,"productoDescuento": 0
            ,"productoExistencia": 1000
            ,"productoImagen": "Ron-850.webp"}]
    data1 = json.dumps(datos, indent=11, sort_keys=True)
    jsondata = json.loads(data1)
    return jsondata

def conectarmysql(host,user, pwd, bd):
    try:
        conexion = mysql.connector.connect(host=host,user=user,password=pwd, database=bd)
    except Exception as error:
        print("ERROR: ", error)
    else:
        # Crear consulta a la Base de Datos
        mi_cursor = conexion.cursor()
        
        try:
            for j in insertardatos():
                mi_cursor.execute(f"""INSERT INTO `examen`
                                    (`idProducto`,
                                    `productoNombreCorto`,
                                    `productoNombreLargo`,
                                    `productoDescripcion`,
                                    `productoTipo`,
                                    `productoPresentacion`,
                                    `productoCosto`,
                                    `productoGanancia`,
                                    `productoDescuento`,
                                    `productoExistencia`,
                                    `productoImagen`)
                                    VALUES
                                    ({j["idProducto"]},
                                    {j["productoNombreCorto"]},
                                    {j["productoNombreLargo"]},
                                    {j["productoDescripcion"]},
                                    {j["productoTipo"]},
                                    {j["productoPresentacion"]},
                                    {j["productoCosto"]},
                                    {j["productoGanancia"]},
                                    {j["productoDescuento"]},
                                    {j["productoExistencia"]},
                                    {j["productoImagen"]});""")
        except mysql.connector.errors.ProgrammingError as e:
            print("Error en la consulta ", e)
        except Exception as error:
            print("ERROR: ", error)
        else:
            for reg in mi_cursor:
                print(reg)
            mi_cursor.close()
        conexion.close()  # Checar
conectarmysql("localhost","root", "root", "examen")
