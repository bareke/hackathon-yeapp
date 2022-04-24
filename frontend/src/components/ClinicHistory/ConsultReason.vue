<template>
  <div class="rounded shadow-xl bg-blue-100 p-8 w-1/2">
    <h1 class="text-sm sm:text-xl font-bold mb-5">
      Registrar datos de la consulta
    </h1>

    <div class="flex flex-col" @change="emitConsultReason">
      <label for="decription" class="text-left text-xs mb-0 text-gray-500"
        >Descripción de la consulta</label
      >
      <textarea
        name="description"
        id="decription"
        cols="20"
        placeholder="Descripción"
        rows="2"
        v-model="form.description"
        class="mb-4"
      ></textarea>
      <label for="decription" class="text-left text-xs mb-0 text-gray-500"
        >Descripción de las enfermedades actuales
      </label>
      <textarea
        name="actualSicks"
        id=""
        cols="20"
        placeholder="Enfermedades"
        rows="2"
        v-model="form.actualSicks"
        class="mb-4"
      ></textarea>
      <label for="decription" class="text-left text-xs mb-0 text-gray-500"
        >Descripción de los antedecentes</label
      >
      <textarea
        name="past"
        id=""
        placeholder="Antecedentes"
        cols="20"
        rows="2"
        v-model="form.past"
      ></textarea>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        description: "",
        actualSicks: "",
        past: "",
      },
    };
  },
  methods: {
    emitConsultReason() {
      this.$emit("consult-data", this.form);
    },
  },
};
</script>
<style scoped>
textarea {
  border-radius: 0.7em;
  padding: 0.2em 1em;
  margin-top: 3px;
  font-size: 12px;
}

textarea:focus {
  border: solid 1px blue;
}
</style>
