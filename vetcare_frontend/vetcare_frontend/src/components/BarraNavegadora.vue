<template>
    <nav class="navbar is-fixed-top has-shadow" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
            <RouterLink class="navbar-item" to="/">
                <img src="@/assets/17074032.jpg" alt="VetCare Logo">
            </RouterLink>
            <h1 class="navbar-item">Historial Mascotero</h1>
            <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" @click="isActive = !isActive">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
            </a>
        </div>

        <div class="navbar-menu" :class="{ 'is-active': isActive }">
            <div class="navbar-start">
                <a class="navbar-item" @click="mostrarModalCliente = !mostrarModalCliente">Agregar Cliente</a>
            </div>

            <div class="navbar-end">
                <RouterLink class="navbar-item" to="/" @click="logOut">Salir</RouterLink>
            </div>
        </div>
    </nav>
   
   
    <div class="modal" :class="{ 'is-active': mostrarModalCliente }">
      <div class="modal-background" @click="mostrarModalCliente = false"></div>
        <div class="modal-content">
          <div class="box">
            <form @submit.prevent="agregarCliente">
              <div class="field">
                <label class="label">Nombre</label>
                <div class="control">
                  <input class="input" type="text" v-model="model.cliente.nombre" required>
                </div>
              </div>

              <div class="field">
                <label class="label">Apellido</label>
                <div class="control">
                  <input class="input" type="text" v-model="model.cliente.apellido" required>
                </div>
              </div>

              <div class="field">
                <label class="label">Email</label>
                <div class="control">
                  <input class="input" type="email" v-model="model.cliente.email" required>
                </div>
              </div>

              <div class="field">
                <label class="label">Localidad</label>
                <div class="control">
                  <input class="input" type="text" v-model="model.cliente.localidad" required>
                </div>
              </div>

              <div class="field">
                <label class="label">Provincia</label>
                <div class="control">
                  <input class="input" type="text" v-model="model.cliente.provincia" required>
                </div>
              </div>

              <div class="field">
                <label class="label">Direccion</label>
                <div class="control">
                  <input class="input" type="text" v-model="model.cliente.direccion" required>
                </div>
              </div>

              <div class="field">
                <label class="label">Telefono</label>
                <div class="control">
                  <input class="input" type="number" v-model="model.cliente.telefono" required>
                </div>
              </div>

            <div class="field is-grouped">
              <div class="control">
                <button class="button is-primary" type="submit">Agregar</button>
              </div>
              <div class="control">
                <button class="button is-link" @click="mostrarModalCliente = false">Cancelar</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
      

</template>

<script>
import axios from "axios";

export default {
  name: "BarraNavegadora",
  data() {
    return {
      isActive: false,
      model: {
        cliente: {
          nombre: "",
          apellido: "",
          email: "",
          localidad: "",
          provincia : "",
          direccion: "",
          telefono: "",
          mascota: []
        },
      },
      mostrarModalCliente: false,
    };
  },
  methods: {
    async mostrarFormCliente(){
      this.mostrarModalCliente = true;
    },
    agregarCliente() {
      axios.post("http://localhost:8000/api/v1.0/cliente/", this.model.cliente)
      .then(resp => {
        console.log(resp.data)
        alert("Cliente agregado a la base de datos")
        this.model.cliente ={
          nombre: "",
          apellido: "",
          email: "",
          localidad: "",
          provincia: "",
          direccion: "",
          telefono: "",
          mascota: []
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
    logOut(){
      localStorage.removeItem("token");
    }

  },
};
</script>

<style scoped>
.navbar {
  background-color: #fff;
  color: #363636;
  font-size: 1.2rem;
}

.navbar-item {
  color: #363636;
}

.navbar-burger {
  color: #363636;
}

@media screen and (max-width: 1023px) {
  .navbar {
      background-color: #fff;
      color: #363636;
      font-size: 1.2rem;
  }
}
</style>