import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { useHistory } from "react-router";

export default function ClienteForm() {
    const [cliente, setCliente] = useState({
        id: null,
        cuit: '',
        nombre: '',
        direccion: '',
        telefono: '',
        localidad: ''
    });
    const [lista, setLista] = useState([
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
    ]);
    const { id } = useParams();
    const history = useHistory();

    useEffect(() => {
        GetCliente();
    }, [])

    function GetCliente() {
        let ids = lista.map(cliente => cliente.id);
        setCliente(lista[ids.indexOf(parseInt(id))]);
    }

    function guardar(event) {

        event.preventDefault()
        event.stopPropagation()
        /*if (id) {
            axios.put(`http://localhost:5000/clientes/${id}`, cliente)
                .then(response => {
                    alert("se ha modificado el registro")
                    history.push("/clientes/")
                })
                .catch(error => alert(error))
        }
        else {
            axios.post("http://localhost:5000/clientes/", cliente)
                .then(response => {
                    alert("se ha agregado el registro")
                    history.push("/clientes/")
                }).catch(error => alert(error))
        }*/
    }

    function handleOnChange(event, campo) {
        setCliente({
            ...cliente,
            [campo]: event.target.value
        })
    }

    return(
        <>
            <h3>Editando a {cliente.nombre}</h3>
            <div className="container bg-white py-3">
                {!id && <h1>Nuevo cliente</h1>}
                <form onSubmit={(event) => guardar(event)}>
                    <div className="form-row">
                        <div className="col-1 text-center align-self-center">
                            <label>Nombre</label>
                        </div>
                        <div className="col-4">
                            <input 
                                type="text" 
                                className="form-control" 
                                value={cliente.nombre} 
                                onChange={(event) => handleOnChange(event, 'nombre')} 
                                placeholder="Nombre"/>
                        </div>
                        <div className="col-1 text-center align-self-center">
                            CUIT
                        </div>
                        <div className="col-2">
                            <input 
                                type="text" 
                                className="form-control text-center" 
                                value={cliente.cuit} 
                                onChange={(event) => handleOnChange(event, 'nombre')} 
                                placeholder="Nombre"/>
                        </div>
                        <div className="col-1 text-center align-self-center">
                            <label>Teléfono</label>
                        </div>
                        <div className="col-2">
                            <input 
                                type="text" 
                                className="form-control text-center" 
                                value={cliente.telefono} onChange={(event) => handleOnChange(event, 'telefono')} />
                        </div>
                    </div>
                    <div className="form-row mt-3">
                        <div className="col-1 text-center align-self-center">
                            <label>Dirección</label>
                        </div>
                        <input 
                            type="text" 
                            className="form-control col-4" 
                            value={cliente.direccion} 
                            onChange={(event) => handleOnChange(event, 'direccion')} />
                        <div className="col-1 text-center align-self-center">
                            <label>Localidad</label>
                        </div>
                        <input 
                            type="text" 
                            className="form-control col-4" 
                            value={cliente.localidad} 
                            onChange={(event) => handleOnChange(event, 'localidad')} />    
                        <div className="col-2"></div>
                        <div className="col-4 justify-content-end">
                            <button type="submit" className="btn btn-primary mr-2">Aceptar</button>
                            <button onClick={() => history.push("/clientes/")} className="btn btn-danger">Cancelar</button>
                        </div>
                    </div>  
                </form>
            </div>
        </>
    )
}