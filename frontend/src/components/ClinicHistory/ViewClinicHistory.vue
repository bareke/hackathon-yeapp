<template>
  <div class="flex gap-6">
    <vs-button danger flat class="absolute right-4 my-4" @click="generateReport"
      >Generar reporte</vs-button
    >
    <AccoredeonComponent
      class="mt-16"
      ref="user"
      title="Información del paciente"
    >
      <div class="flex gap-3 nowrap mb-1">
        <span for="name"> <b>Nombres del paciente:</b></span>
        <span>{{ clinicHistory.node.data.userData.name }}</span>
      </div>
      <div class="flex gap-3 nowrap mb-1">
        <span for="name"> <b>Apellidos del paciente:</b></span>
        <span>{{ clinicHistory.node.data.userData.lastname }}</span>
      </div>
      <div class="flex gap-3 nowrap mb-1">
        <span for="name"> <b>Identificación del paciente:</b></span>
        <span>{{ clinicHistory.node.data.userData.identificationNumber }}</span>
      </div>
      <div class="flex gap-3 nowrap mb-1">
        <span for="name"> <b>Dirección del paciente:</b></span>
        <span>{{ clinicHistory.node.data.userData.address }}</span>
      </div>
    </AccoredeonComponent>
    <AccoredeonComponent
      class="mt-16"
      id="consult"
      title="Información de la consulta"
    >
      <div class="flex gap-3 nowrap mb-1">
        <span for="name"> <b>Descripción:</b></span>
        <span>{{ clinicHistory.node.data.consultData.description }}</span>
      </div>
      <div class="flex gap-3 nowrap mb-1">
        <span for="name"> <b>Enfermedades:</b></span>
        <span>{{ clinicHistory.node.data.consultData.actualSicks }}</span>
      </div>
      <div class="flex gap-3 nowrap mb-1">
        <span for="name"> <b>Antecedentes:</b></span>
        <span>{{ clinicHistory.node.data.consultData.past }}</span>
      </div>
    </AccoredeonComponent>
    <AccoredeonComponent class="mt-16" id="annexes" title="Anexos">
      <h1>No hay anexos</h1></AccoredeonComponent
    >
  </div>
</template>
<script>
import AccoredeonComponent from "@/components/AccordeonComponent.vue";
export default {
  components: { AccoredeonComponent },
  props: ["clinicHistory"],
  data() {
    return {};
  },
  methods: {
    generateReport() {
      this.launchNotification(
        "success",
        "Generando reporte ...",
        "",
        '<box-icon color="rgb(20,255,20)" type="solid" name="newUser-check"></box-icon>'
      );
    },
    launchNotification(color = "success", title = "", body = "", icon = "") {
      this.$vs.notification({
        position: "top-right",
        color,
        flat: true,
        icon,
        progress: "auto",
        title,
        text: body,
      });
    },
  },
};
</script>
