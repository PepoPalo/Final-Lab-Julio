import './App.css';

import { Link, Switch, Route, BrowserRouter as Router } from "react-router-dom";

import VentaListado from './components/facturas de venta/VentaListado';

import CompraListado from './components/facturas de compra/CompraListado';

import PresupuestoListado from './components/presupuestos/PresupuestoListado';

import ProductoListado from './components/productos/ProductoListado';
import ProductoForm from './components/productos/ProductoForm';

import ClienteListado from './components/clientes/ClienteListado';

import ProveedorListado from './components/proveedores/ProveedorListado';
import ProveedorForm from './components/proveedores/ProveedorForm';

import VendedorListado from './components/vendedores/VendedorListado';

export default function App() {
  return (
    <div className="container bg-transparent">
      <Router>
        <div className="App mt-3">
          <ul className="nav nav-tabs" id="myTab" role="tablist">

            <li className="nav-item dropdown rounded-top" id="fondo" role="presentation">
              <button className="nav-link dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Facturas</button>
              <ul className="dropdown-menu">
                <li>
                  <Link className="dropdown-item" to="/ventas">Venta</Link>
                </li>
                <li>
                  <Link className="dropdown-item" to="/compras">Compra</Link>
                </li>
              </ul>
            </li>

            <li className="nav-item rounded-top" id="fondo" role="presentation">
              <Link 
                className="nav-link" 
                id="presupuesto-tab" 
                data-toggle="tab"
                role="tab" 
                aria-controls="presupuesto" 
                aria-selected="false" 
                to="/presupuestos">Presupuestos
              </Link>
            </li>

            <li className="nav-item rounded-top" id="fondo" role="presentation">
              <Link 
                className="nav-link" 
                id="producto-tab" 
                data-toggle="tab"
                role="tab" 
                aria-controls="producto" 
                aria-selected="false" 
                to="/productos">Productos
              </Link>
            </li>

            <li className="nav-item-dropdown rounded-top" id="fondo" role="presentation">
              <button className="nav-link dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Personas</button>
              <ul className="dropdown-menu">
                <li>
                  <Link className="dropdown-item" to="/clientes">Cliente</Link>
                </li>
                <li>
                  <Link className="dropdown-item" to="/vendedores">Vendedor</Link>
                </li>
                <li>
                  <Link className="dropdown-item" to="/proveedores">Proveedor</Link>
                </li>
              </ul>
            </li>

          </ul>
        </div>

        <Switch>

          <Route path="/ventas" component={VentaListado}></Route>

          <Route path="/compras" component={CompraListado}></Route>

          <Route path="/presupuestos" component={PresupuestoListado}></Route>

          <Route path="/productos/:id" component={ProductoForm} />
          <Route path="/productos" component={ProductoListado}></Route>

          <Route path="/clientes" component={ClienteListado}></Route>

          <Route path="/proveedores/:id" component={ProveedorForm} />
          <Route path="/proveedores" component={ProveedorListado}></Route>

          <Route path="/vendedores" component={VendedorListado}></Route>

          {/* Clientes 
          <Route path="/clientes/nuevo" component={ClienteForm}></Route>
          <Route path="/clientes/ficha/:id" component={ClienteFicha}></Route>
          <Route path="/clientes/:id" component={ClienteForm}></Route>
          <Route path="/clientes" component={ClienteListado}></Route>

         
          <Route path="/lep/nuevo/:id" component={LepForm}></Route>
          <Route path="/lep/<int:cliente>/<int:id>" component={LepForm}></Route>
          <Route path="/leps/:id" component={LepListado} ></Route>

          
          <Route path="/equipos/nuevo" component={EquipoForm}></Route>
          <Route path="/equipos/:imei" component={EquipoForm} ></Route>
          <Route path="/equipos" component={EquipoListado}></Route>

         
          <Route path="/lineas/nueva" component={LineaForm}></Route>
          <Route path="/lineas/:id" component={LineaForm}></Route>
          <Route path="/lineas/buscar/:desde/:hasta" component={LineaListado}></Route>
          <Route path="/lineas/buscar/:desde/:hasta/:mozo" component={LineaListado}></Route>
          <Route path="/lineas" component={LineaListado}></Route>

          
          <Route path="/planes/nuevo" component={PlanForm}></Route>
          <Route path="/planes/:id" component={PlanForm} ></Route>
          <Route path="/planes" component={PlanListado}></Route>*/}

        </Switch>
      </Router >
    </div>
  );
}
