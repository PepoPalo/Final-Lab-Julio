import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

var presupuestos = [
    {
        id: 1,
        numero: 123466,
        cliente: 'Mario Castañeda',
        tipo: 'A',
        fecha_limite: '30-07-2021'
    }
]

export default function PresupuestoListado() {
    const [lista, setLista] = useState([]);

    useEffect(() =>{
        getPresupuestos();
    }, [])

    function getPresupuestos() {
        /*axios.get("http://localhost:5000/presupuestos/")
          .then((response) => setLista(response.data))
          .catch((error) => alert(error))*/
          setLista(presupuestos)
      }
    
    
      function borrar(id) {
        axios.put(`http://localhost:5000/presupuestos/baja/${id}`)
          .then((response) => {
            getPresupuestos()
          })
          .catch(error => alert(error))
      }

    return(
        <>
            <div className="bg-white rounded-bottom rounded-right">
                <div>
                    <Link to="/presupuestos/nuevo" className="btn btn-primary my-3">Nuevo</Link>
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
                            lista.map(presupuesto => (
                                <>
                                <tr key={presupuesto.numero}>
                                    <th className="text-center" scope="row">{presupuesto.numero}</th>
                                    <td className="text-center">{presupuesto.cliente}</td>
                                    <td className="text-center">{presupuesto.tipo}</td>
                                    <td className="text-center">{presupuesto.fecha_limite}</td>
                                    <td className="text-center">
                                        <Link 
                                            className="btn btn-outline-primary mr-2" 
                                            to={"/presupuestos/ficha/" + presupuesto.id}
                                            data-toggle="tooltip" data-placement="bottom" title="Ficha del presupuesto"
                                            >Ver
                                        </Link>
                                        <Link 
                                            className="btn btn btn-outline-warning mr-2" 
                                            to={"/presupuestos/" + presupuesto.id}
                                            data-toggle="tooltip" data-placement="bottom" title="Editar información personal"
                                            >Editar
                                        </Link>
                                        <button className="btn btn-outline-danger mr-2" onClick={() => borrar(presupuesto.id)}>Dar Baja</button>
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