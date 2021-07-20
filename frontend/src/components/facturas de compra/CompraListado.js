import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

var compras = [
    {
        id: 1,
        numero: 123466,
        cliente: 'Mario Castañeda',
        tipo: 'A',
        fecha_limite: '30-07-2021'
    }
]

export default function CompraListado() {
    const [lista, setLista] = useState([]);

    useEffect(() =>{
        getCompras();
    }, [])

    function getCompras() {
        /*axios.get("http://localhost:5000/compras/")
          .then((response) => setLista(response.data))
          .catch((error) => alert(error))*/
          setLista(compras)
      }
    
    
      function borrar(id) {
        axios.put(`http://localhost:5000/compras/baja/${id}`)
          .then((response) => {
            getCompras()
          })
          .catch(error => alert(error))
      }

    return(
        <>
            <div className="bg-white rounded-bottom rounded-right">
                <div>
                    <Link to="/compras/nuevo" className="btn btn-primary my-3">Nuevo</Link>
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
                            <th className="text-center" scope="col">Compras</th>
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
                            lista.map(compra => (
                                <>
                                <tr key={compra.numero}>
                                    <th className="text-center" scope="row">{compra.numero}</th>
                                    <td className="text-center">{compra.cliente}</td>
                                    <td className="text-center">{compra.tipo}</td>
                                    <td className="text-center">{compra.fecha_limite}</td>
                                    <td className="text-center">
                                        <Link 
                                            className="btn btn-outline-primary mr-2" 
                                            to={"/compras/ficha/" + compra.id}
                                            data-toggle="tooltip" data-placement="bottom" title="Ficha del compra"
                                            >Ver
                                        </Link>
                                        <Link 
                                            className="btn btn btn-outline-warning mr-2" 
                                            to={"/compras/" + compra.id}
                                            data-toggle="tooltip" data-placement="bottom" title="Editar información personal"
                                            >Editar
                                        </Link>
                                        <button className="btn btn-outline-danger mr-2" onClick={() => borrar(compra.id)}>Dar Baja</button>
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