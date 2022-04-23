<template>
  <div
    class="flex justify-center gap-10 flex-col mt-4 rounded shadow-xl bg-blue-100 p-8 w-1/3"
  >
    <h1 class="text-sm sm:text-xl font-bold">Registrar Historia Médica</h1>
    <div>
      <step-progress
        :steps="['step 1', 'step 2']"
        current-step="step 1 "
        icon-class="fa fa-check"
      ></step-progress>
    </div>
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
    <div class="flex justify-center gap-4">
      <vs-radio success v-model="form.genre" val="1"> Masculino </vs-radio>
      <vs-radio success v-model="form.genre" val="2"> Femenino </vs-radio>
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
};
</script>

<style scoped></style>
<style>
.vs-input-content {
  width: 100%;
}
.vs-input {
  width: 100% !important;
}
.vs-select {
  width: 100% !important;
  max-width: 100% !important;
}
.vs-select-content {
  width: 100% !important;
  max-width: 100% !important;
}
</style>
