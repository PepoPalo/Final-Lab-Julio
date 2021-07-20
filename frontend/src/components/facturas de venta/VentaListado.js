import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

var ventas = [
    {
        id: 1,
        numero: 123466,
        cliente: 'Mario Castañeda',
        tipo: 'A',
        fecha_limite: '30-07-2021'
    }
]

export default function VentaListado() {
    const [lista, setLista] = useState([]);

    useEffect(() =>{
        getVentas();
    }, [])

    function getVentas() {
        /*axios.get("http://localhost:5000/ventas/")
          .then((response) => setLista(response.data))
          .catch((error) => alert(error))*/
          setLista(ventas)
      }
    
    
      function borrar(id) {
        axios.put(`http://localhost:5000/ventas/baja/${id}`)
          .then((response) => {
            getVentas()
          })
          .catch(error => alert(error))
      }

    return(
        <>
            <div className="bg-white rounded-bottom rounded-right">
                <div>
                    <Link to="/ventas/nuevo" className="btn btn-primary my-3">Nuevo</Link>
                    <form >
                    {/* <div className="row"> */}
                        <label htmlFor="start">Desde:</label>
                        <input 
                            type="date"
                            min="2018-01-01" 
                            max="2023-12-31" 
                            // onChange={(event) => handleOnChange(event, 'desde')}
                        >
                        </input>

                        <label htmlFor="start">Hasta:</label>
                        <input 
                            type="date"
                            min="2018-01-01" 
                            max="2023-12-31" 
                            // onChange={(event) => handleOnChange(event, 'hasta')}
                            >
                        </input>
                        
                        {/* <button onClick={(event) => getFiltradas(event)}> BUSCAR</button> */}
                    {/* </div> */}
                </form>
                </div>
                <table className="table table-hover">
                    <thead>
                        <tr>
                            <th className="text-center" scope="col">Ventas</th>
                        </tr>
                    </thead>
                    <thead className="bg-info">
                        <tr>
                        <th className="text-center" scope="col">Número</th>
                        <th className="text-center" scope="col">Cliente</th>
                        <th className="text-center" scope="col">Tipo</th>
                        <th className="text-center" scope="col">Fecha Límite</th>
                        <th className="text-center" scope="col">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {lista.length > 0 && (
                            lista.map(venta => (
                                <>
                                <tr key={venta.numero}>
                                    <th className="text-center" scope="row">{venta.numero}</th>
                                    <td className="text-center">{venta.cliente}</td>
                                    <td className="text-center">{venta.tipo}</td>
                                    <td className="text-center">{venta.fecha_limite}</td>
                                    <td className="text-center">
                                        <Link 
                                            className="btn btn-outline-primary mr-2" 
                                            to={"/ventas/ficha/" + venta.id}
                                            data-toggle="tooltip" data-placement="bottom" title="Ficha del venta"
                                            >Ver
                                        </Link>
                                        <Link 
                                            className="btn btn btn-outline-warning mr-2" 
                                            to={"/ventas/" + venta.id}
                                            data-toggle="tooltip" data-placement="bottom" title="Editar información personal"
                                            >Editar
                                        </Link>
                                        <button className="btn btn-outline-danger mr-2" onClick={() => borrar(venta.id)}>Dar Baja</button>
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