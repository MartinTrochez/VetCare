<template>
  <section class="hero is-fullheight">
    <Logo />
    <div class="hero-body">
      <div class="container">
        <h1 class="title has-text-centered">Ingreso al Historial Mascotero</h1>
        <form class="box" @submit.prevent="submitForm">
          <div class="field">
            <label class="label">Usuario</label>
            <div class="control has-icons-left">
              <input class="input" type="text" placeholder="Usuario" v-model="username">
              <span class="icon is-small is-left">
                <i class="fas fa-user"></i>
              </span>
            </div>
          </div>
            <div class="field">
              <label class="label">Contraseña</label>
              <div class="control has-icons-left">
                <input class="input" type="password" placeholder="Contraseña" v-model="password">
                <span class="icon is-small is-left">
                  <i class="fas fa-lock"></i>
                </span>
              </div>
            </div>
            <button class="button is-primary is-fullwidth">Log In</button>
        </form>
        <div v-if="mensajeErrorUsuario" class="error-message">{{ mensajeErrorUsuario }}</div>
        </div>
    </div>
  </section>
</template>

<script>
import Logo from "@/components/Logo.vue";
import axios from "axios";

export default {
    name: "LoginView",
    components: {
        Logo,
    },
    data() {
        return {
            username: "",
            password: "",
            errors: [],
            mensajeErrorUsuario: ""
        };
    },
    methods: {
      async submitForm() {
        try {
          axios.defaults.headers.common["Authorization"] = "";
          localStorage.removeItem("token");
          const formData = {
            password: this.password,
            username: this.username
          };
          const response = await axios.post("http://localhost:8000/api/v1.0/token/login", formData);
          const token = response.data.auth_token;
          axios.defaults.headers.common["Authorization"] = "Token " + token;
          localStorage.setItem("token", token);
          const path = this.$route.query.to || "/historial-mascotero";
          this.$router.push(path);
        } catch (error) {
            if (error.response) {
              const errorData = error.response.data;
              if (error.response.status === 400) {
                this.mensajeErrorUsuario = "El usuario o la contraseña son incorrectos."
              } else {
                for (const property in errorData) {
                  this.errors.push(`${property}: ${errorData[property]}`);
                }
              }
            } else {
              this.errors.push("Algo salio mal. Intente de vuelta");
              console.log(JSON.stringify(error));
            }
        }
      } 
    },
};
</script>

<style scoped>
.hero {
  background-color: #f5f5f5;
}

.box {
  margin-top: 30px;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
}

.button {
  margin-top: 20px;
}
</style>