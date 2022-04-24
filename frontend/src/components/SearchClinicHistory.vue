<template>
  <div class="text-center mt-48 bg-blue-100 rounded-xl mx-20 py-10">
    <h1 class="text-3xl font-bold text-gray-600 capitalize mb-6">
      Buscar historia clínica
    </h1>
    <div class="flex justify-center text-center gap-5 my-auto">
      <vs-select
        placeholder="Selecione tipo de documento"
        v-model="searchValue"
      >
        <vs-option label="Cedula" value="1"> Cedula </vs-option>
        <vs-option label="Tarjeta de identidad" value="2">
          Tarjeta de identidad
        </vs-option>
        <vs-option label=" Cedula de extrangería" value="3">
          Cedula de extrangería
        </vs-option>
        <vs-option label="Registro civil" value="4"> Registro civil </vs-option>
      </vs-select>

      <vs-input label-placeholder="Buscar historia clinica..." type="number">
      </vs-input>
      <vs-button primary @click="search"
        ><box-icon name="search-alt-2" color="#fff"></box-icon>Buscar</vs-button
      >
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      searchValue: "",
    };
  },
  methods: {
    search() {},
  },
};
</script>
