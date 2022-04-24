<template>
  <div>
    <div class="text-center mt-5 mx-20">
      <vs-button size="xl" danger type="filled" @click="goToHome">
        Volver
      </vs-button>
    </div>
    <div class="text-center mt-48 bg-blue-100 rounded-xl mx-20 py-10">
      <h1 class="text-3xl font-bold text-gray-600 capitalize mb-6">
        Buscar historia clínica
      </h1>
      <div class="flex justify-center text-center gap-5 my-auto">
        <vs-select placeholder="Selecione tipo de documento" v-model="searchId">
          <vs-option label="Cedula" value="1"> Cedula </vs-option>
          <vs-option label="Tarjeta de identidad" value="2">
            Tarjeta de identidad
          </vs-option>
          <vs-option label=" Cedula de extrangería" value="3">
            Cedula de extrangería
          </vs-option>
          <vs-option label="Registro civil" value="4">
            Registro civil
          </vs-option>
        </vs-select>

        <vs-input
          label-placeholder="Buscar historia clinica..."
          type="number"
          v-model="searchValue"
        >
        </vs-input>
        <vs-button primary @click="search"
          ><box-icon name="search-alt-2" color="#fff"></box-icon
          >Buscar</vs-button
        >
      </div>
    </div>
    <div v-if="found.length > 0">
      <ViewClinicHistory :clinicHistory="found[0]" />
    </div>
  </div>
</template>
<script>
import ViewClinicHistory from "@/components/ClinicHistory/ViewClinicHistory.vue";
export default {
  components: { ViewClinicHistory },
  data() {
    return {
      searchId: "",
      searchValue: "",
      data: [],
      found: [],
    };
  },
  created() {
    this.loadClinicHistory();
  },
  methods: {
    search() {
      if (this.searchValue !== "") {
        this.found = this.data.filter((item) => {
          if (
            item.node.data.userData?.identificationNumber === this.searchValue
          ) {
            return item.node;
          }
        });
      }
    },
    loadClinicHistory() {
      this.$apollo
        .query({
          query: require("@/graphql/SearchClinicHistory.gql"),
        })
        .then((response) => {
          this.data = response.data.allClinicsHistories.edges;
        });
    },
    goToHome() {
      this.$router.push("/");
    },
  },
};
</script>
