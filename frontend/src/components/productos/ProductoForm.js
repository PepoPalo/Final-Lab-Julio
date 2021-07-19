import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { useHistory } from "react-router";

export default function ProductoForm() {
    const [producto, setProducto] = useState({
        id: null,
        codigo: '',
        descripcion: '',
        precio_unitario: 0.00
    });
    const [lista, setLista] = useState([
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
    ]);
    const { id } = useParams();
    const history = useHistory();

    useEffect(() => {
        GetProducto();
    }, [])

    function GetProducto() {
        let ids = lista.map(producto => producto.id);
        setProducto(lista[ids.indexOf(parseInt(id))]);
    }

    function guardar(event) {

        event.preventDefault()
        event.stopPropagation()
        /*if (id) {
            axios.put(`http://localhost:5000/productos/${id}`, producto)
                .then(response => {
                    alert("se ha modificado el registro")
                    history.push("/productos/")
                })
                .catch(error => alert(error))
        }
        else {
            axios.post("http://localhost:5000/productos/", producto)
                .then(response => {
                    alert("se ha agregado el registro")
                    history.push("/productos/")
                }).catch(error => alert(error))
        }*/
    }

    function handleOnChange(event, campo) {
        setProducto({
            ...producto,
            [campo]: event.target.value
        })
    }

    return(
        <>
            <h3>Editando {producto.descripcion}</h3>
            <div className="container bg-white py-3">
                {!id && <h1>Nuevo producto</h1>}
                <form onSubmit={(event) => guardar(event)}>
                    <div className="form-row">
                        <div className="col-1 text-center align-self-center">
                            <label>Descripción</label>
                        </div>
                        <div className="col-4">
                            <input 
                                type="text" 
                                className="form-control" 
                                value={producto.descripcion} 
                                onChange={(event) => handleOnChange(event, 'descripcion')} 
                                placeholder="Descripcion"/>
                        </div>
                        <div className="col-1 text-center align-self-center">
                            Código
                        </div>
                        <div className="col-2">
                            <input 
                                type="text" 
                                className="form-control text-center" 
                                value={producto.codigo} 
                                onChange={(event) => handleOnChange(event, 'codigo')} 
                                placeholder="Código"/>
                        </div>
                        <div className="col-1 text-center align-self-center">
                            <label>Precio Unitario</label>
                        </div>
                        <div className="col-2">
                            <input 
                                type="text" 
                                className="form-control text-center" 
                                value={producto.precio_unitario.toFixed(2)} onChange={(event) => handleOnChange(event, 'precio_unitario')} />
                        </div>
                        <div className="col-4 justify-content-end">
                            <button type="submit" className="btn btn-primary mr-2">Aceptar</button>
                            <button onClick={() => history.push("/proveedores/")} className="btn btn-danger">Cancelar</button>
                        </div>
                    </div>
                </form>
            </div>
        </>
    )
}