import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

var listaEjemplo = [
    {
        'id': 1,
        'codigo': "PA",
        'descripcion': "Producto A",
        'precio_unitario': 68.90
    },
    {
        'id': 2,
        'codigo': "PB",
        'descripcion': "Producto B",
        'precio_unitario': 89.99
    },
    {
        'id': 1,
        'codigo': "POT",
        'descripcion': "Potasio",
        'precio_unitario': 140.90
    }
]

export default function ProductoListado() {
    const [lista, setLista] = useState([]);

    useEffect(() => {GetProductos()}, [])

    function GetProductos() {
        setLista(listaEjemplo)
    }

    function Borrar(id) {
        console.log(`Borraste el producto ${id}`);
    }

    return(
        <>
            <div className="bg-white rounded-bottom rounded-right">
                <div>
                    <Link to="/productos/nuevo" className="btn btn-primary my-3">Nuevo</Link>
                    
                </div>
                <table className="table table-hover">
                    <thead className="bg-info">
                        <tr>
                            <th className="text-center">Productos</th> 
                        </tr>
                    </thead>
                    <thead className="bg-info">
                        <tr>
                            <th className="text-center" scope="col">Código</th>
                            <th className="text-center" scope="col">Descripción</th>
                            <th className="text-center" scope="col">Precio Unitario</th>
                            <th className="text-center" scope="col">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {lista.length > 0 && (
                            lista.map(producto => (
                                <>
                                <tr key={producto.id}>
                                    <td className="text-center">{producto.codigo}</td>
                                    <td className="text-center">{producto.descripcion}</td>
                                    <td className="text-center">$ {producto.precio_unitario.toFixed(2)}</td>
                                    <td className="text-center">
                                        <Link 
                                            className="btn btn-outline-warning mr-2" 
                                            to={"/productos/" + producto.id}
                                            data-toggle="tooltip" data-placement="bottom" title="Editar información personal"
                                            >Editar
                                        </Link>
                                        <button className="btn btn-outline-danger mr-2" onClick={() => Borrar(producto.id)}>Dar Baja</button>
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