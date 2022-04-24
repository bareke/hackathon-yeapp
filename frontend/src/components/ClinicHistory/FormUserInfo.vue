<template>
  <div class="rounded shadow-xl bg-blue-100 p-8 w-3/5">
    <h1 class="text-sm sm:text-xl font-bold">Registrar datos del usuario</h1>
    <div class="mt-4 grid grid-cols-2 gap-10 inputs" @change="emitFormData">
      <vs-input
        class="w-full"
        primary
        v-model="form.name"
        label-placeholder="Nombres"
      >
      </vs-input>
      <vs-input
        class="w-full"
        primary
        v-model="form.lastname"
        label-placeholder="Apellidos"
      >
      </vs-input>
      <vs-select
        class="w-full"
        placeholder="Selecione tipo de documento"
        v-model="form.identificationType"
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

      <vs-input
        class="w-full"
        primary
        v-model="form.identificationNumber"
        label-placeholder="Número de identificación"
      >
      </vs-input>
      <vs-input
        class="w-full"
        primary
        v-model="form.address"
        label-placeholder="Dirección"
      >
      </vs-input>
      <div class="flex justify-center gap-4 relative">
        <label for="" class="text-center absolute text-xs text-gray-500"
          >Genero</label
        >
        <vs-radio v-model="form.genre" val="1" class="mt-4 text-gray-500">
          Masculino
        </vs-radio>
        <vs-radio v-model="form.genre" val="2" class="mt-4 text-gray-500">
          Femenino
        </vs-radio>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        name: "",
        lastname: "",
        identificationType: "",
        identificationNumber: "",
        address: "",
        genre: "",
      },
    };
  },
  methods: {
    emitFormData() {
      this.$emit("user-data", this.form);
    },
  },
};
</script>

<style scoped></style>
<style>
.inputs .vs-input-content {
  width: 100%;
}
.inputs .vs-input {
  width: 100% !important;
}
.inputs .vs-select {
  width: 100% !important;
  max-width: 100% !important;
}
.inputs .vs-select-content {
  width: 100% !important;
  max-width: 100% !important;
}
</style>
