<template>
    <div>
        <div>
            <BarraNavegadora />
        </div>

        <!-- Barra de Busqueda -->
        <div class="container mt-3">
            <div class="field">
                <div class="control has-icons-left">
                    <input class="input" type="text" placeholder="Busqueda Cliente" v-model="searchQuery">
                    <span class="icon is-small is-left">
                        <i class="fas fa-search"></i>
                    </span>
                </div>
            </div>

            <!-- Listado de clientes que crea la lista de acuerdo a la lista de clientes -->
            <div class="columns" v-if="filteredClientes.length > 0">
                <div class="column is-10 is-offset-1">
                    <div class="card">
                        <div class="card-content">
                            <div class="content" >
                                <div class="list is-hoverable">
                                    <a class="list-item" v-for="cliente in filteredClientes" :key="cliente.id" @click="clienteElegido = (clienteElegido === cliente) ? null : cliente">
                                    <p>{{ cliente.apellido }}, {{ cliente.nombre }}</p>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="columns" v-else>
                <div class="column is-10 is-offset-1">
                    <div class="card">
                        <div class="card-content">
                            <div class="content">
                                <p>No se encontraron resultados</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Detalles del cliente elegido -->
            <div v-if="clienteElegido">
                <ClienteDetalle :cliente="clienteElegido" />
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import BarraNavegadora from "@/components/BarraNavegadora.vue";
import ClienteDetalle from "@/components/ClienteDetalle.vue";
export default {
    name: "HistorialMascotero",
    components: {
        BarraNavegadora,
        ClienteDetalle
    },
    data() {
        return {
            clientes: [],
            searchQuery: "",
            clienteElegido: "",
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/v1.0/cliente/')
            .then((response) => {
                console.log(response.data);
                this.clientes = response.data;
            })
            .catch((error) => {
                console.log(error);
            });
    },
    methods: {
        mostrarDetallesCliente(cliente) {
            this.clienteElegido = cliente
        }
    },
    computed: {
        filteredClientes() {
            if (!this.searchQuery) {
                return this.clientes;
            }
            const query = this.searchQuery.toLowerCase();
            console.log(query);
            return this.clientes.filter(cliente => {
                 return cliente.nombre.toLowerCase().includes(query) || cliente.apellido.toLowerCase().includes(query);
            });
        },
    }
};
</script>

<style scoped>
.section {
    margin-top: 3.25rem; /* Height of the navbar */
    padding: 1.5rem;
    background-color: #f5f5f5;
    color: #363636;
    font-size: 1.2rem;
}
</style>