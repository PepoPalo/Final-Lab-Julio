import React, { useEffect, useState} from "react";
import { useParams } from "react-router-dom";
import { useHistory } from "react-router";

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

export default function ProveedorForm() {
    const [proveedor, setProveedor] = useState({
        id: null,
        cuit: '',
        nombre: '',
        direccion:'',
        telefono:'',
        localidad:''
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
        setLista(listaEjemplo);
    })
    useEffect(() => {
        GetProveedor();
    }, [])

    function GetProveedor() {
        let ids = lista.map(proveedor => proveedor.id);
        setProveedor(lista[ids.indexOf(parseInt(id))]);
    }

    function guardar(event) {

        event.preventDefault()
        event.stopPropagation()
        /*if (id) {
            axios.put(`http://localhost:5000/proveedores/${id}`, proveedor)
                .then(response => {
                    alert("se ha modificado el registro")
                    history.push("/proveedores/")
                })
                .catch(error => alert(error))
        }
        else {
            axios.post("http://localhost:5000/proveedores/", proveedor)
                .then(response => {
                    alert("se ha agregado el registro")
                    history.push("/proveedores/")
                }).catch(error => alert(error))
        }*/
    }

    function handleOnChange(event, campo) {
        setProveedor({
            ...proveedor,
            [campo]: event.target.value
        })
    }

    return(
        <>
            <h3>Editando a {proveedor.nombre}</h3>
            <div className="container bg-white py-3">
                {!id && <h1>Nuevo proveedor</h1>}
                <form onSubmit={(event) => guardar(event)}>
                    <div className="form-row">
                        <div className="col-1 text-center align-self-center">
                            <label>Nombre</label>
                        </div>
                        <div className="col-4">
                            <input 
                                type="text" 
                                className="form-control" 
                                value={proveedor.nombre} 
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
                                value={proveedor.cuit} 
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
                                value={proveedor.telefono} onChange={(event) => handleOnChange(event, 'telefono')} />
                        </div>
                    </div>
                    <div className="form-row mt-3">
                        <div className="col-1 text-center align-self-center">
                            <label>Dirección</label>
                        </div>
                        <input 
                            type="text" 
                            className="form-control col-4" 
                            value={proveedor.direccion} 
                            onChange={(event) => handleOnChange(event, 'direccion')} />
                        <div className="col-1 text-center align-self-center">
                            <label>Localidad</label>
                        </div>
                        <input 
                            type="text" 
                            className="form-control col-4" 
                            value={proveedor.localidad} 
                            onChange={(event) => handleOnChange(event, 'localidad')} />    
                        <div className="col-2"></div>
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