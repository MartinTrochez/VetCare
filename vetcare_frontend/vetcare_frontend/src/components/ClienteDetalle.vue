<template>
    <div id="cliente-informacion">
        <div class="container mt-3">
            <div class="columns"> 
                <!-- Información del Cliente -->
                <div class="column is-one-quarter">
                    <div class="card">
                        <div class="car-content">
                            <p class="title is-5">
                                Información del Cliente
                            </p>
                            <table>
                                <tbody>
                                    <tr>
                                        <th>Nombre</th>
                                        <td>{{ cliente.nombre }}</td>
                                    </tr>
                                    <tr>
                                        <th>Apellido</th>
                                        <td>{{ cliente.apellido }}</td>
                                    </tr>
                                    <tr>
                                        <th>Email</th>
                                        <td>{{ cliente.email }}</td>
                                    </tr>
                                    <tr>
                                        <th>Telefono</th>
                                        <td>{{ cliente.telefono }}</td>
                                    </tr>
                                    <tr>
                                        <th>Direccion</th>
                                        <td>{{ cliente.direccion }}</td>
                                    </tr>
                                    <tr>
                                        <td><button class="button is-info is-small center-block" @click="mostrarModalAnimal = !mostrarModalAnimal">Agregar Animal</button></td>
                                        <td><button class="button is-info is-small center-block ml-3" @click="generarPDF">PDF</button></td>
                                    </tr>
                                </tbody>
                                <div>
                                </div>        
                            </table>
                        </div>
                    </div>
                </div>
                <!-- Información del Animal -->
                <div id= "mascota-informacion" class="column" v-if="cliente.mascota.length > 0">
                    <div class="card">
                        <div class="card-content">
                            <p class="title is-5">
                                Historial de Visitas
                            </p>
                            <div >
                                <table class="table is-striped is-fullwidth" v-for="(mascota, idMascota) in cliente.mascota" :key="idMascota">
                                    <thead>
                                        <td colspan="3" class="has-text-centered has-background-grey-ligther"> 
                                            <strong>{{ mascota.nombre }} - {{ mascota.raza }} - {{ mascota.edad }} Meses</strong>
                                            <br>
                                            <button  class="button is-black is-small" @click="mostrarModalConsulta = !mostrarModalConsulta; animalId = mascota.id">Agregar Visita</button>
                                        </td>
                                        <tr>
                                            <th>Fecha</th>
                                            <th>Peso (Kg)</th>
                                            <th>Diagnostico</th>
                                        </tr>
                                    </thead>
                                    <tbody >
                                        <template v-if="mascota.visita.length > 0">
                                            <tr v-for="(visita, indexVisita) in mascota.visita" :key="indexVisita">
                                                <td>{{ formatDate(visita.fecha) }}</td>
                                                <td>{{ visita.peso }}</td>
                                                <td>{{ visita.diagnostico }}</td>
                                            </tr>
                                        </template>
                                    </tbody>
                                </table>
                            </div>
                        </div>   
                    </div>
                </div>
                <div v-else>
                    <p class="title is-5">El cliente no tiene registrado animales</p>
                </div>
            </div>
        </div>
    </div>


    <!-- Carga de Animales que no estan en la base de datos -->
    <div class="modal" :class="{ 'is-active': mostrarModalAnimal }">
      <div class="modal-background" @click="mostrarModalAnimal = false"></div>
        <div class="modal-content">
          <div class="box">
            <form @submit.prevent="agregarAnimal">
                <p class="title"> Carga de Datos de Mascota </p>
                <div class="field">
                    <label class="label">Nombre</label>
                    <div class="control">
                    <input class="input" type="text" v-model="modelAnimal.animal.nombre" required>
                    </div>
                </div>
                <div class="field">
                    <label class="label">Especie</label>
                    <div class="control">
                    <input class="input" type="text" v-model="modelAnimal.animal.especie" required>
                    </div>
                </div>
                <div class="field">
                    <label class="label">Raza</label>
                    <div class="control">
                    <input class="input" type="text" v-model="modelAnimal.animal.raza" required>
                    </div>
                </div>
                <div class="field">
                    <label class="label">Color</label>
                    <div class="control">
                    <input class="input" type="text" v-model="modelAnimal.animal.color" required>
                    </div>
                </div>
                <div class="field">
                    <label class="label">Edad (Meses)</label>
                    <div class="control">
                        <input class="input" type="number" v-model="modelAnimal.animal.edad" required>
                    </div>
                </div>
                
            <div class="field is-grouped">
              <div class="control">
                <button class="button is-primary" type="submit">Agregar</button>
              </div>
              <div class="control">
                <button class="button is-link" @click="mostrarModalAnimal = false">Cancelar</button>
              </div>
            </div>
            </form>
        </div>
      </div>
    </div>

    <!-- Carga de Visita que no estan en la base de datos -->
    <div class="modal" :class="{ 'is-active': mostrarModalConsulta }">
      <div class="modal-background" @click="mostrarModalConsulta = false"></div>
        <div class="modal-content">
          <div class="box">
            <form @submit.prevent="agregarVisita()">
                <div class="field">
                    <label class="label">Peso</label>
                    <div class="control">
                    <input class="input" type="number" v-model="modelConsulta.visita.peso" required>
                    </div>
                </div>
                <div class="field">
                    <label class="label">Diagnótico</label>
                    <div class="control">
                    <input class="input" type="text" v-model="modelConsulta.visita.diagnostico" required>
                    </div>
                </div>    
                <div class="field is-grouped">
                <div class="control">
                    <button class="button is-primary" type="submit">Agregar</button>
                </div>
                <div class="control">
                    <button class="button is-link" @click="mostrarModalConsulta = false">Cancelar</button>
                </div>
                </div>
            </form>
        </div>
      </div>
    </div>
</template>


<script>
import axios from "axios";
/* import jsPDF from "jspdf";
import html2canvas from "html2canvas"; */
import html2pdf from "html2pdf.js";


export default {
    name: "ClienteDetalle",
    props: {
        cliente: Object
    },
    data() {
        return {
            modelAnimal: {
                animal: {
                  nombre: "",
                  especie: "",
                  raza: "",
                  color: "",
                  edad: "",
                  cliente: this.cliente.id,
                  visita: [],
                },
            }, 
            modelConsulta: {
                visita: {
                    animal: "",
                    peso: "",
                    diagnostico: "",
                    fecha: "",
                },
            },
            mostrarModalAnimal: false,
            mostrarModalConsulta: false,
            animalId: this.cliente.mascota
        }
    },
    methods: {
        formatDate(date) {
            const options = {
                year: "numeric", 
                month: "numeric", 
                day:"numeric", 
                hour: "numeric", 
                minute: "numeric"
            };
            return new Date(date).toLocaleDateString("es-Ar", options);
        },
        agregarAnimal() {
            console.log(this.modelAnimal.animal.cliente);
            axios.post("http://localhost:8000/api/v1.0/animal/", this.modelAnimal.animal)
            .then(resp => {
                console.log(resp.data)
                alert("Animal agregado a la base de datos")
                this.modelAnimal.animal ={
                    nombre: "",
                    especie: "",
                    raza: "",
                    color: "",
                    edad: "",
                    cliente: this.cliente.id,
                    visita: [],
                }
            })
            .catch(function (error) {
                if (error.response) {
                console.log(error.response.data);
                console.log(error.response.status);
                console.log(error.response.headers);
                } else if (error.request) {
                console.log(error.request);
                } else {
                console.log('Error', error.message);
                }
                console.log(error.config);
            });
        },
        agregarVisita() {
            console.log(this.animalId);

            this.modelConsulta.visita.animal = this.animalId;
            axios.post("http://localhost:8000/api/v1.0/visita/", this.modelConsulta.visita)
            .then(resp => {
                console.log(resp.data)
                alert("Visita agregado a la base de datos")
                this.modelConsulta.visita ={
                    animal: null,
                    peso: "",
                    diagnostico: "",
                    fecha: "",
                }
            })
            .catch(function (error) {
                if (error.response) {
                console.log(error.response.data);
                console.log(error.response.status);
                console.log(error.response.headers);
                } else if (error.request) {
                console.log(error.request);
                } else {
                console.log('Error', error.message);
                }
                console.log(error.config);
            });
        },
        generarPDF(){
            const nombre = this.cliente.nombre;
            const apellido = this.cliente.apellido;
            const informacionCliente = document.getElementById('cliente-informacion');
            const opciones = {
                margin: 1,
                image: {type: 'png', quality: 0.98},
                filename: "Informe " + nombre + ", " + apellido + ".pdf", 
                html2canvas: { scale: 3},
                jsPDF: {unit: 'in', format: 'a4', orientation: 'portrait'},
                autoPaging: true,
                pagebreak: {mode: 'avoid-all', before: '#mascota-animal'}
            }
            html2pdf().set(opciones).from(informacionCliente).save();
        },

    },
};
</script>