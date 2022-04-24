<template>
  <div class="flex justify-center items-center gap-20 mt-60">
    <div class="h-80 w-80">
      <vs-card type="3" @click="createClinicHistory()">
        <template #title>
          <h3>Nueva historia clinica</h3>
        </template>
        <template #img>
          <img
            src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Add_document_icon_%28the_Noun_Project_27896%29_blue.svg/1024px-Add_document_icon_%28the_Noun_Project_27896%29_blue.svg.png"
            height="80%"
            width="100%"
          />
        </template>
        <template #text>
          <p class="text-paragraph">
            Creación de una nueva historia clinica para un usuario no existente.
          </p>
        </template>
      </vs-card>
    </div>

    <div class="h-80 w-80">
      <vs-card type="3" @click="searchClinicHistory()">
        <template #title>
          <h3>Buscar historia clinica</h3>
        </template>
        <template #img>
          <img
            src="https://www.pngitem.com/pimgs/m/75-750898_user-search-find-icon-search-customer-icon-png.png"
            height="100%"
            width="100%"
          />
        </template>
        <template #text>
          <p class="text-paragraph">
            Buscar una historia clinica de un paciente existente.
          </p>
        </template>
      </vs-card>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  methods: {
    createClinicHistory() {
      this.$router.push("/management");
    },
    searchClinicHistory() {
      this.$router.push("/search");
    },
    goToHome() {
      this.$router.push("/");
    },
  },
};
</script>
<style>
.text-paragraph {
  text-align: left;
}
</style>
