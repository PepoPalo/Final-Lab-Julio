import React, { useState, useEffect} from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

var listaEjemplo = [
    {
        'id': 1,
        'cuit': '20390380071',
        'nombre': 'Pedro Palomino',
        'direccion': 'Av Crespo 1072',
        'telefono': '3435182886',
        'localidad': 'San Benito'
    },
    {
        'id': 2,
        'cuit': '20320180231',
        'nombre': 'Oscar Schneider',
        'direccion': '25 de mayo 1072',
        'telefono': '3434172899',
        'localidad': 'San Agustín'
    },
    {
        'id': 3,
        'cuit': '20290382171',
        'nombre': 'Juan Pastor',
        'direccion': 'Av Ramirez 1072',
        'telefono': '3435120126',
        'localidad': 'Paraná'
    }
]

export default function ClienteListado() {
    const [lista, setLista] = useState([])

    useEffect(() => {
      getClientes();
    }, [])
  
    function getClientes() {
      /*axios.get("http://localhost:5000/clientes/")
        .then((response) => setLista(response.data))
        .catch((error) => alert(error))*/
        setLista(listaEjemplo)
    }

    function borrar(id) {
        /*axios.put(`http://localhost:5000/clientes/baja/${id}`)
          .then((response) => {
            alert("Registro borrado correctamente")
            getClientes()
          })
          .catch(error => alert(error))*/
    }

    return(
        <>
            <div className="bg-white rounded-bottom rounded-right">
                <div>
                    <Link to="/clientes/nuevo" className="btn btn-primary my-3">Nuevo</Link>
                    
                </div>
                <table className="table table-hover">
                    <thead className="bg-info">
                        <tr>
                            <th className="text-center">Clientes</th> 
                        </tr>
                    </thead>
                    <thead className="bg-info">
                        <tr>
                        <th className="text-center" scope="col">CUIT</th>
                        <th className="text-center" scope="col">Nombre</th>
                        <th className="text-center" scope="col">Dirección</th>
                        <th className="text-center" scope="col">Teléfono</th>
                        <th className="text-center" scope="col">Localidad</th>
                        <th className="text-center" scope="col">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {lista.length > 0 && (
                            lista.map(cliente => (
                                <>
                                <tr key={cliente.id}>
                                    <td className="text-center">{cliente.cuit}</td>
                                    <td className="text-center">{cliente.nombre}</td>
                                    <td className="text-center">{cliente.direccion}</td>
                                    <td className="text-center">{cliente.telefono}</td>
                                    <td className="text-center">{cliente.localidad}</td>
                                    <td className="text-center">
                                        <Link 
                                            className="btn btn-outline-warning mr-2" 
                                            to={"/clientes/" + cliente.id}
                                            data-toggle="tooltip" data-placement="bottom" title="Editar información personal"
                                            >Editar
                                        </Link>
                                        <button className="btn btn-outline-danger mr-2" onClick={() => borrar(cliente.id)}>Dar Baja</button>
                                    </td>
                                </tr>
                                
                            </>))
                        )}
                        {lista.length === 0 && (
                            <tr>
                                <td colSpan="3">
                                    <h2>No hay datos</h2>
                                </td>
                            </tr>
                        )}
                    </tbody>
                </table>

            </div>
        </>
    )
}